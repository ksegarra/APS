'''
Created on Oct 28, 2016

@author: Klint

main module
'''

DEFAULT_POWER_FILE = 'datain_power.csv'
DEFAULT_TIME_FILE = 'datain_time.csv'
DEFAULT_OUTPUT_FILE = 'output.csv'

from collections import namedtuple
from csv_parser import dictReadCsv
from keyconstants import *
from energycalc import *


Config = namedtuple('Config', ['powerinfile', 'timeinfile', 'outputfile'])

def run_calculations(dictPowerVals, dictTimeVals):
    energyAPS = fCalcEnergyAPSHypothetical(dictPowerVals[APS_STBY], dictPowerVals[APS_ACT], dictTimeVals[TV_ON])
    print 'Energy APS: ', energyAPS
    
    energy_T2_T = fCalcEnergyTier2_TV(dictPowerVals[TV_ABS_1], dictTimeVals[TV_ABS], dictTimeVals[T_SENSOR])
    print 'Energy save t2 (TV)', energy_T2_T
    
    energy_T2_TAX = fCalcEnergyTier2_TV_DVD_AUDIO(dictPowerVals[XBOX_ABS], dictPowerVals[TV_ABS_2], dictPowerVals[TV_ABS_2], dictPowerVals[AUDIO_ABS], dictTimeVals[TV_ABS], dictTimeVals[XBOX_ABS], dictTimeVals[T_SENSOR])
    print 'Energy save t2 (TV, DVD, AUDIO)', energy_T2_TAX
    
    energy_T2_TDX = fCalcEnergyTier2_TV_DVD_XBOX(dictPowerVals[XBOX_ABS], dictPowerVals[TV_ABS_2], dictPowerVals[TV_ABS_2], dictPowerVals[DVD_ABS], dictTimeVals[TV_ABS], dictTimeVals[XBOX_ABS], dictTimeVals[T_SENSOR])
    print 'Energy save t2 (TV, DVD, XBOX)', energy_T2_TDX
    
    print(CALPLUG_DATA)
    energy_T2_TDX_long = fCalcEnergyTier2_LongSensorTime(dictPowerVals[XBOX_ABS], dictPowerVals[TV_ABS_1], dictPowerVals[TV_ABS_2], dictPowerVals[DVD_ABS], dictTimeVals[TV_ABS], dictTimeVals[XBOX_ABS], dictTimeVals[T_SENSOR_LONG], CALPLUG_DATA)
    print 'Energy save t2 long (TV, DVD, XBOX)', energy_T2_TDX_long
    
    energy_T2_TDX_long_act = fCalcEnergyTier2_LongSensorTimeAct(dictPowerVals[XBOX_ABS], dictPowerVals[TV_ABS_1], dictPowerVals[TV_ABS_2], dictPowerVals[DVD_ABS], dictTimeVals[TV_ABS], dictTimeVals[XBOX_ABS], dictTimeVals[T_SENSOR_LONG], CALPLUG_DATA)
    print 'Energy save t2 long act (TV, DVD, XBOX)', energy_T2_TDX_long_act
    
    


def tupleGetData(config):
    return (dictReadCsv(config.powerinfile, REQUIRED_POWER_CONSTANTS), dictReadCsv(config.timeinfile, REQUIRED_TIME_CONSTANTS))

if __name__ == '__main__':
    config = Config(DEFAULT_POWER_FILE, DEFAULT_TIME_FILE, DEFAULT_OUTPUT_FILE)
    
    dictPowerVals, dictTimeVals = tupleGetData(config)
    run_calculations(dictPowerVals, dictTimeVals)