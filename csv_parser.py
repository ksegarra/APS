'''
Created on Oct 28, 2016

@author: Klint

Module for Parsing CSV file
'''
import csv
from collections import defaultdict
from scenario import Scenario

CSV_EXT = '.csv'

class MissingRequiredKeyError(Exception):
    pass

class CSVParseRowError(Exception):
    pass

# public functions

def listReadCsv(sFilename):
    '''
    return a list from a two column csv
    '''
    with open(sFilename, 'r') as csvfile:
        l = []
        bStarted = False
        csvreader = csv.reader(csvfile, delimiter=',', dialect='excel')
        try:
            for row in csvreader:
                # print row
                if bStarted: 
                    l.append(fSafeCastFloat(row[1]))
                else:
                    bStarted = row[0] == 'START'
        except:
            print 'bad line {}'.format(csvreader.line_num)
        return l
    return []

def dictReadCsv(sFilename, setRequired=set()):
    '''
    returns a dictionary that matches variable names to value in CSV
    '''
    dictCSV = defaultdict(dict)
    bStarted = False
    if not sFilename.endswith(CSV_EXT):
        return
    with open(sFilename, 'r') as csvfile:
        try:
            csvreader = csv.reader(csvfile, delimiter=',', dialect='excel')
            for row in csvreader:
                if bStarted:
                    device, key, value = tupleProcessRow(row)
                    value = fSafeCastFloat(value)
                    if value >= 0:
                        dictCSV[device].update([(key, value)])
                    else:
                        dictCSV[device].update([(key, row[2])])
                else:
                    bStarted = bCheckStarted(row)
        except CSVParseRowError:
            print 'Row {} is invalid in file {}'.format(csvreader.line_num, sFilename)
            return {}
        except:
            print 'CSV is invalid'
            return {}
    if(bCheckRequired(dictCSV, setRequired)):
        return dictCSV
    else:
        raise MissingRequiredKeyError

def parseScenarios(sFilename):
    '''
    parses scenarios file into a list of Scenario Objects 
    '''
    with open(sFilename, 'r') as csvfile:
        l = [Scenario()]
        curr_scenario = 1 # keeps track of the scenario we are in
        bStarted = False
        csvreader = csv.reader(csvfile, delimiter=',', dialect='excel')
        try:
            for row in csvreader:
                #print row
                if bStarted:
                    device, scenario_index, aps_control, connected, used, pri_source = processRowScenario(row)
                    # print scenario_index, curr_scenario
                    if scenario_index > curr_scenario:
                        curr_scenario += 1
                        l.append(Scenario())
                    details = [aps_control, connected, used, pri_source]
                    #print details
                    l[curr_scenario -1].addDevice(device, list(map(lambda x: bool(x), details)))
                    #print(l)
                else:
                    bStarted = row[0] == 'START'
        except:
            print 'bad line {}'.format(csvreader.line_num)
        return l
    return []

## private functions
def processRowScenario(row):
    return tuple(fSafeCastInt(row[i]) for i in range(6))
    
def bCheckStarted(row):
    return len(row) >= 3 and row[0] == 'DEVICE' and row[1] == 'KEY' and row[2] == 'VAL'

def tupleProcessRow(row):
    if len(row) >= 3:
        return (row[0], row[1], row[2])
    else:
        raise MissingRequiredKeyError

def bCheckRequired(dictCSV, setRequired):
    return setRequired.issubset(dictCSV.keys())

def fSafeCastFloat(s):
    try:
        return float(s)
    except ValueError:
        return -1
    
def fSafeCastInt(s):
    try:
        return int(s)
    except ValueError:
        return s
    
if __name__ == '__main__':
    pass
