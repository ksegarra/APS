'''
Created on Oct 28, 2016

@author: Klint

main module
'''

DEFAULT_POWER_FILE = 'workbooks/datain_power.csv'
DEFAULT_TIME_FILE = 'workbooks/datain_time.csv'
DEFAULT_OUTPUT_FILE = 'outputs/output.csv'
DEFAULT_LIST_FILE = 'workbooks/datain_listtimes.csv'
DEFAULT_SCENARIOS_FILE = 'workbooks/datain_scenarios.csv'

from collections import namedtuple
from csv_parser import dictReadCsv, listReadCsv, parseScenarios
from keyconstants import *
from energycalc import *


Config = namedtuple('Config', ['powerinfile', 'timeinfile', 'outputfile'])

def run_calculations(dictPowerVals, dictTimeVals):
    '''
    function to run based in inputted scenarios, power values and time values
    
    remains unimplemented for now but the backbone (ie the equations) are already ready to be plugged in
    '''
    print dictPowerVals, dictTimeVals
    
    
    ##### Mike Pls help implement this not 100% how we are gonna determine which equation to use and when### 
#     energyAPS = fCalcEnergyAPSHypothetical(dictPowerVals[APS_STBY], dictPowerVals[APS_ACT], dictTimeVals[TV_ON])
#     print 'Energy APS: ', energyAPS
#     
#     energy_T2_T = fCalcEnergyTier2_TV(dictPowerVals[TV_ABS_1], dictTimeVals[TV_ABS], dictTimeVals[T_SENSOR])
#     print 'Energy save t2 (TV)', energy_T2_T
#     
#     energy_T2_TAX = fCalcEnergyTier2_TV_DVD_AUDIO(dictPowerVals[XBOX_ABS], dictPowerVals[TV_ABS_2], dictPowerVals[TV_ABS_2], dictPowerVals[AUDIO_ABS], dictTimeVals[TV_ABS], dictTimeVals[XBOX_ABS], dictTimeVals[T_SENSOR])
#     print 'Energy save t2 (TV, DVD, AUDIO)', energy_T2_TAX
#     
#     energy_T2_TDX = fCalcEnergyTier2_TV_DVD_XBOX(dictPowerVals[XBOX_ABS], dictPowerVals[TV_ABS_2], dictPowerVals[TV_ABS_2], dictPowerVals[DVD_ABS], dictTimeVals[TV_ABS], dictTimeVals[XBOX_ABS], dictTimeVals[T_SENSOR])
#     print 'Energy save t2 (TV, DVD, XBOX)', energy_T2_TDX
#     
#     lData = list(x/60 for x in listReadCsv(DEFAULT_LIST_FILE))
#     #print(CALPLUG_DATA)
#     
#     energy_T2_TDX_long = fCalcEnergyTier2_LongSensorTime(dictPowerVals[XBOX_ABS], dictPowerVals[TV_ABS_1], dictPowerVals[TV_ABS_2], dictPowerVals[DVD_ABS], dictTimeVals[TV_ABS], dictTimeVals[XBOX_ABS], dictTimeVals[T_SENSOR_LONG], lData)
#     print 'Energy save t2 long (TV, DVD, XBOX)', energy_T2_TDX_long
#     
#     energy_T2_TDX_long_act = fCalcEnergyTier2_LongSensorTimeAct(dictPowerVals[XBOX_ABS], dictPowerVals[TV_ABS_1], dictPowerVals[TV_ABS_2], dictPowerVals[DVD_ABS], dictTimeVals[TV_ABS], dictTimeVals[XBOX_ABS], dictTimeVals[T_SENSOR_LONG], lData)
#     print 'Energy save t2 long act (TV, DVD, XBOX)', energy_T2_TDX_long_act
    
    


def tupleGetData(config):
    '''
    helper function that runs the parsing component of the program
    '''
    return (dictReadCsv(config.powerinfile), dictReadCsv(config.timeinfile))

if __name__ == '__main__':
    '''
    functions that implement parsing are dictReadCsv reads the values of time and power into a dictionary with the format
    
    for power:
    {
        DEVICE1 : {STATE1: POWER1, STATE2:POWER2....}
        DEVICE2 : {STATE1: POWER1, STATE2:POWER2....}
        ..... 
    }
    
    for time:
    {
        DEVICE1 : {STATE1: TIME1, STATE2:TIME2....}
        DEVICE2 : {STATE1: TIME1, STATE2:TIME2....}
        ..... 
    }
    
    for Scenarios use parse Scenarios which returns a list of Scenario objects (see scenario.py for more info)
    
    All the parsing is meant to be extremely flexible so we can put an arbritrary number of devices/states and Scenarios
    into the csv files as long as they follow the prescribed format
    
    '''
    config = Config(DEFAULT_POWER_FILE, DEFAULT_TIME_FILE, DEFAULT_OUTPUT_FILE)
    
    dictPowerVals, dictTimeVals = tupleGetData(config)
    run_calculations(dictPowerVals, dictTimeVals)
    
    l = parseScenarios(DEFAULT_SCENARIOS_FILE)
    print(l)
    