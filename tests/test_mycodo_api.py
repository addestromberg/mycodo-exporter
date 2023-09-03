import unittest
import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'src'))
from mycodo_api import MycodoApi
from pprint import pprint



class Test_MycodoApi(unittest.TestCase):
    
    api: MycodoApi
    
    def setUp(self):
        self.api = MycodoApi()
        
    
    def test_get_inputs(self):
        """ Test Get all Inputs """
        devices = self.api.get_input_devices()
        pprint(devices["input settings"])
        self.assertIsNotNone(devices)
        self.assertTrue("input settings" in devices.keys())
        
    def test_get_outputs(self):
        """ Test Get all Inputs """
        devices = self.api.get_output_devices()
        pprint(devices["output devices"])
        self.assertIsNotNone(devices)
        self.assertTrue("output devices" in devices.keys())
        
    def test_pids(self):
        """ Test Get all Inputs """
        pids = self.api.get_pids()
        pprint(pids)
        #self.assertIsNotNone(devices)
        #self.assertTrue("output devices" in devices.keys())
    
    def test_get_input(self):
        uid = "5d5f8e99-bb0f-46b8-9e5e-2bf0861d2baa"
        device = self.api.get_input_device(uid=uid)
        pprint(device)
    
    def test_get_output(self):
        uid = "6a6f810d-7873-429d-ac6b-8b72741c360e"
        device = self.api.get_output_device(uid=uid)
        pprint(device)
        
    def test_get_measurement(self):
        uid = "2c80e36e-f505-4444-9853-6f0bb7382a0e"
        unit = "C"
        channel = 0
        measurement = self.api.get_measurements(uid, channel, unit)
        pprint(measurement)

