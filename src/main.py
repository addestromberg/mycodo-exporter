from utility import get_logger
from mycodo_api import MycodoApi
import config

logger = get_logger()
mycodo = MycodoApi()
devices = {}


def main():
    logger.info("Initializing Mycodo Prometheus Exporter")

    get_devices()
    
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
        
    if "PIDS" in config.EXPORT_MEASUREMENTS:
        logger.info("Get all pid regulators...")
        try:
            pid_devices = mycodo.get_pids()
            if pid_devices == None:
                raise Exception("API call for pid regulators returned None.")
            
            pid_devices = pid_devices["pid settings"]
            for device in pid_devices:
                devices[device["unique_id"]] = {"type": "pid",
                                                "name": device["name"],
                                                "channels": []}

            pass
        except Exception as e:
            logger.error(f"Failed to get output devices. - {e}")

main()

if __file__ == "__main__":
    main()
    

    