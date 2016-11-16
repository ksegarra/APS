'''
Created on Oct 28, 2016

@author: Klint

Contains sets of constants that are required in the CSV files

Ignore this file for now since a lot of this is still in flux but this will eventually contain all the necessary constants
that are required once those are straightened out

'''

TV_ABS_1 = 'TV_ABSENT_1'
TV_ABS_2 = 'TV_ABSENT_2'
TV_ABS_3 = 'TV_ABSENT_3'
TV_ABS   = 'TV_ABSENT'

TV_ACT_1 = 'TV_ACTIVE_1'
TV_ACT_2 = 'TV_ACTIVE_2'
TV_ACT_3 = 'TV_ACTIVE_3'

TV_ON = 'TV_ON'

XBOX_ABS = 'XBOX_ABSENT'
XBOX_ACT = 'XBOX_ACTIVE'

DVD_ABS = 'DVD_ABSENT'
DVD_ACT = 'DVD_ACTIVE'

AUDIO_ABS = 'AUDIO_ABSENT'
AUDIO_ACT = 'AUDIO_ACTIVE'

STB_ABS = 'STB_ABSENT'
STB_ACT = 'STB_ACTIVE'

APS_ACT = 'APS_ACTIVE'
APS_STBY = 'APS_STANBY'

T_SENSOR = 'TIMER_SENSOR'
T_SENSOR_LONG = 'TIMER_SENSOR_LONG'

REQUIRED_POWER_CONSTANTS = {TV_ABS_1, TV_ABS_2, TV_ABS_3, TV_ACT_1, TV_ACT_2, TV_ACT_3,
                   XBOX_ABS, XBOX_ACT, DVD_ABS, DVD_ACT, AUDIO_ABS, AUDIO_ACT, STB_ABS,
                   STB_ACT, STB_ACT, APS_ACT, APS_STBY}

REQUIRED_TIME_CONSTANTS = {TV_ON, TV_ABS, XBOX_ABS, T_SENSOR, T_SENSOR_LONG}

if __name__ == '__main__':
    ## Testing
    for k in sorted(REQUIRED_TIME_CONSTANTS):
        print k + ',' + '0' + ','
    