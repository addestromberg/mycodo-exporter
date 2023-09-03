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
    