from utility import get_logger, format_name
from mycodo_api import MycodoApi
import config
import prometheus_client
from prometheus_client import start_http_server, Gauge

import time

logger = get_logger()
mycodo = MycodoApi()
devices = {}

prometheus_client.REGISTRY.unregister(prometheus_client.GC_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)



def main():
    logger.info("Initializing Mycodo Prometheus Exporter")
    get_devices()
    get_device_channels()
    logger.info(f"Found {len(devices)} device(s) on network.")
    logger.info("Started the exporter...")
    while True:
        # TODO: Create the exports here... 
        logger.debug("Updating...")
        get_measurements()
        try:
            update_gauges()
        except Exception as e:
            logger.warning("Had an error updating gauges. Trying to reload devices...")
            devices = {}
            get_devices()
            get_device_channels()
        time.sleep(config.INTERVAL_SECONDS)


def update_gauges():
    for uid, device in devices.items():
        for index, channel in enumerate(device["channels"]):
            if "value" in channel:
                if "gauge" not in channel:
                    name = format_name(device["name"])
                    channel_id = index
                    type = device["type"]
                    if type == "input":
                        measurement = f"_{channel['measurement']}"
                    else:
                        measurement = ""
                    devices[uid]["channels"][index]["gauge"] = Gauge(f"{config.GAUGE_PREFIX}_{name}_{type}{measurement}", f"{type} device channel")
                
                if channel["value"] != None:
                    channel["gauge"].set(channel["value"])
            
        
        

def get_device_channels():
    """ Get all channels for registered device """
    for uid, item in devices.items():
        if item["type"] == "input":
            # TODID: Inputs here
            response = mycodo.get_input_device(uid=uid)
            response = response["device measurements"]
            
            for channel in response:
                params = {"uid": channel["unique_id"],
                          "name": channel["name"],
                          "measurement": channel["measurement"],
                          "unit": channel["unit"],
                          "channel": channel["channel"]}
                devices[uid]["channels"].append(params)
            
        elif item["type"] ==  "output":
            # TODID: Outputs here
            response = mycodo.get_output_device(uid=uid)
            response = response["output device channels"]
            
            for channel in response:
                params = {"uid": channel["unique_id"],
                          "name": channel["name"],
                          "channel": channel["channel"]}
                devices[uid]["channels"].append(params)
        # elif item["type"] == "pids":
        #     # TODID: Pids here
        #     # Skipping becouse the pid settings is accessed from get all pids
        #     pass
            
def get_devices():
    """
    Get all devices connected to mycodo
    """
    if "INPUTS" in config.EXPORT_MEASUREMENTS:
        logger.info("Get all input devices...")
        try:
            input_devices = mycodo.get_input_devices()
            if input_devices == None:
                raise Exception("API call for input devices returned None.")
            
            input_devices = input_devices["input settings"]
            for device in input_devices:
                devices[device["unique_id"]] = {"type": "input",
                                                "interface": device["interface"],
                                                "name": device["name"],
                                                "channels": []}
                
        except Exception as e:
            logger.error(f"Failed to get input devices. - {e}")
        
        
    if "OUTPUTS" in config.EXPORT_MEASUREMENTS:
        logger.info("Get all output devices...")
        try:
            output_devices = mycodo.get_output_devices()
            if output_devices == None:
                raise Exception("API call for input devices returned None.")
            
            output_devices = output_devices["output devices"]
            for device in output_devices:
                devices[device["unique_id"]] = {"type": "output",
                                                "interface": device["interface"],
                                                "name": device["name"],
                                                "channels": []}
                
        except Exception as e:
            logger.error(f"Failed to get output devices. - {e}")
        
    # if "PIDS" in config.EXPORT_MEASUREMENTS:
    #     try:
    #         pid_devices = mycodo.get_pids()
    #         if pid_devices == None:
    #             raise Exception("API call for pid regulators returned None.")
            
    #         pid_devices = pid_devices["pid settings"]
    #         for device in pid_devices:
    #             devices[device["unique_id"]] = {"type": "pid",
    #                                             "name": device["name"],
    #                                             "channels": []}

    #         pass
    #     except Exception as e:
    #         logger.error(f"Failed to get output devices. - {e}")

def get_measurements():
    """ Fetch latest measurements from all devices channels """
    for dev_uid, dev_item in devices.items():
        if dev_item["type"] == "input":
            # TODID: Inputs measurements here
            for index, channel in enumerate(dev_item["channels"]):
                measurement = mycodo.get_measurements(uid=dev_uid, channel=channel["channel"], unit=channel["unit"])
                if "value" in measurement:
                    if measurement["value"] != None:
                        devices[dev_uid]["channels"][index]["value"] = float(measurement["value"])
                    else:
                        devices[dev_uid]["channels"][index]["value"] = None

        elif dev_item["type"] == "output":
            # TODO: Output measurements here
            output_channels = mycodo.get_output_device(uid=dev_uid)
            states = output_channels["output device channel states"]
            for index, channel in enumerate(dev_item["channels"]):
                if str(channel["channel"]) in states:
                    state = states[str(channel["channel"])]
                    if state == "on":
                        state = float(1)
                    elif state == "off":
                        state = float(0)
                    else:
                        state = float(state)
                        
                    devices[dev_uid]["channels"][index]["value"] = state

start_http_server(8000)
main()
        
    

    