'''
Created on Nov 7, 2016

@author: Klint
'''

from collections import namedtuple

DeviceDetails = namedtuple('DeviceDetails', ['apsControl', 'connected', 'used', 'priSource'], verbose=False)
class Scenario(object):
    '''
    class that models the scenario
    
    interface
    
    addDevice = adds device into model with the associated details
    getAllDevices = returns list of all devices in Scenario
    
    the following four methods return the devices that are in that specific mode of operation in the scenario
    
    getDevicesAPSControl = devices under APS control
    getDevicesConnected = devices connected
    getDevicesUsed = devices ON
    getDevicesPRISrc = devices used as Control
    '''


    def __init__(self):
        '''
        Constructor takes in no values only initializes internal representation of devices
        '''
        self._devices_details = {} # internal representation of how the device is used in this scenario
        
    def addDevice(self, device_name, details):
        '''
        device_name is the name of the device as str
        details is an tuple representing whether or not a device is (APS_CONTROL  CONNECTED  USED PRI_SOURCE) as
        specified in data_in_scenarios.csv
        '''
        self._devices_details[device_name] = DeviceDetails(*details)
        
    def _getDevicesBool(self, filter_function):
        result = []
        for device, details in self._devices_details.items():
            if filter_function(details):
                result.append(device)
        return result
        
    ###
    # interface for the class
    # these four functions return the device details as specified in data_in_scenarios.csv
    ###
    
    def getAllDevices(self):
        return list(self._devices_details.keys())
    
    def getDevicesAPSControl(self):
        return self._getDevicesBool(lambda details: details.apsControl)
    
    def getDevicesConnected(self):
        return self._getDevicesBool(lambda details: details.connected)
    
    def getDevicesUsed(self):
        return self._getDevicesBool(lambda details: details.used)

    def getDevicesPRISource(self):
        return self._getDevicesBool(lambda details: details.priSource)
    
    def __str__(self):
        return 'Scenario: ' + '\n'.join('{}:{}'.format(k,v) for k,v in self._devices_details.items())
    
    def __repr__(self, *args, **kwargs):
        return self.__str__()
        