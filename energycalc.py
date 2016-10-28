'''
Created on Oct 28, 2016

@author: Klint

Module for Calculating Energy Savings of APS based on Calplug Cyber Power Report
'''

P_TV_ABS = 40.2
P_AUDIO_ABS = 64.2
P_XBOX_ABS = 90.85

T_XBOX_ABS = 7.46
T_SENSOR_TIMER = 1.25

HOURS_DAY = 24.0
DAYS_YEAR = 365.25
WATTS_KW  = 1.0/1000.0

##HELPER FUNCTIONS

def fCalcAnnualEnergy(fPower, fDailyTime):
    return fPower * fDailyTime * DAYS_YEAR * WATTS_KW
##

#Eq 1
def fCalcEnergyTier1(listSDW):
    return

#Eq 2
def fCalcEnergyTier2Total(fEnergyTier2_2, fEnergyTier1, fEnergyAPS):
    return fEnergyTier2_2 + fEnergyTier1 - fEnergyAPS

#Eq 3
def fCalcEnergyTier1Device(fPowerStandby, fTimeOn):
    return fCalcAnnualEnergy(fPowerStandby, HOURS_DAY - fTimeOn)

#Eq 4
def fCalcEnergyAPSGeneral():
    return 

#Eq 5
def fCalcEnergyAPSHypothetical(fPowerAPStandby, fPowerAPSActive, fTimeTVOn):
    fAnnualAPSStandbyEnergy = fCalcAnnualEnergy(fPowerAPStandby, HOURS_DAY - fTimeTVOn)
    fAnnualAPSActiveEnergy = fCalcAnnualEnergy(fPowerAPSActive,  fTimeTVOn)
    return fAnnualAPSStandbyEnergy + fAnnualAPSActiveEnergy

#Eq 6
def fCalcEnergyTier2_TV_DVD_AUDIO(fPowerXbox_Absent, fPowerTV_Absent, fPowerTv_Absent2, fPowerDVD_Absent, fTimeTV_Absent, fTimeXbox_Absent, fTimeSensorTimer):
    fTotPower = fPowerXbox_Absent + fPowerTv_Absent2 + fPowerDVD_Absent
    return fCalcAnnualEnergy(fTotPower, fTimeXbox_Absent - fTimeSensorTimer)

#Eq 7
def fCalcEnergyTier2_TV(fPowerTV_Absent, fTimeTV_Absent, fTimeSensorTimer):
    return fCalcAnnualEnergy(fPowerTV_Absent, fTimeTV_Absent - fTimeSensorTimer)

#Eq 8
def fCalcEnergyTier2_TV_DVD_XBOX(fPowerXbox_Absent, fPowerTV_Absent, fPowerTv_Absent2, fPowerAudio_Absent, fTimeTV_Absent, fTimeXbox_Absent, fTimeSensorTimer):
    #print fPowerXbox_Absent, fPowerTV_Absent, fPowerTv_Absent2, fPowerAudio_Absent, fTimeTV_Absent, fTimeXbox_Absent, fTimeSensorTimer
    fTotPower = fPowerXbox_Absent + fPowerTV_Absent + fPowerAudio_Absent
    return fCalcAnnualEnergy(fTotPower, fTimeXbox_Absent - fTimeSensorTimer)

#Eq 9a
def fCalcEnergyTier2_LongSensorTime(fPowerXbox_Absent, fPowerTV_Absent, fPowerTV_Absent2, fPowerDVD_Absent, fTimeTV_Absent, fTimeXbox_Absent, fTimeSensorTimer, listTVTimeAbsent):
    print(listTVTimeAbsent)
    avg_time = sum((max(tTVAbs - fTimeSensorTimer, 0) for tTVAbs in listTVTimeAbsent))/float(len(listTVTimeAbsent)) # sum from 1 to 20
    print avg_time

    fTotPowerAbs1 = fPowerXbox_Absent + fPowerTV_Absent + fPowerDVD_Absent
    fTotPowerAbs2 = fPowerXbox_Absent + fPowerTV_Absent2 + fPowerDVD_Absent
#     print 'avg', avg_time
#     print fTotPowerAbs1
#     print fTotPowerAbs2
    
    return fCalcAnnualEnergy(fTotPowerAbs1, avg_time)
    
#Eq 9b
def fCalcEnergyTier2_LongSensorTimeAct(fPowerXbox_Absent, fPowerTV_Absent, fPowerTV_Absent2, fPowerDVD_Absent, fTimeTV_Absent, fTimeXbox_Absent, fTimeSensorTimer, listTVTimeAbsent):
    avg_time = sum((tTVAbs - fTimeSensorTimer for tTVAbs in listTVTimeAbsent))/float(len(listTVTimeAbsent)) # sum from 1 to 20
    print avg_time
    fTotPowerAbs1 = fPowerXbox_Absent + fPowerTV_Absent + fPowerDVD_Absent
    #fTotPowerAbs2 = fPowerXbox_Absent + fPowerTV_Absent2 + fPowerDVD_Absent
    return fCalcAnnualEnergy(fTotPowerAbs1, avg_time)

#Eq 10 & 11
def fCalcEnergyTier2_PerCycle(totEnergySave, yearlyUses):
    return totEnergySave/yearlyUses

def fCalcEnergyAPS_PerCycle(totEnergyAPS, yearlyUses):
    return totEnergyAPS/yearlyUses

#Eq12
def fCalcEnergySavings_OS(E, totEnergySave, totEnergyAPS, yearlyUses):
    adjustedUses = yearlyUses/2.0
    energySavingsPerCycle = fCalcEnergyTier2_PerCycle(totEnergySave, yearlyUses)
    energyAPSPerCycle = fCalcEnergyAPS_PerCycle(totEnergyAPS, yearlyUses)
    return  adjustedUses * (energySavingsPerCycle + energySavingsPerCycle * (1 - E)) - adjustedUses * E * energyAPSPerCycle
    
if __name__ == '__main__':
    print fCalcEnergyAPSHypothetical(1.5, 2.2, 4.88)
    #fCalcEnergyTier2_TV_DVD_AUDIO(fPowerXbox_Absent, fPowerTV_Absent, fPowerTv_Absent2, fPowerAudio_Absent, fTimeTV_Absent, fTimeXbox_Absent, fTimeSensorTimer):
    print fCalcEnergyTier2_TV_DVD_XBOX(P_XBOX_ABS, P_TV_ABS, 0, P_AUDIO_ABS, 1.5, T_XBOX_ABS, T_SENSOR_TIMER)
