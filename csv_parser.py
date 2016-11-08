'''
Created on Oct 28, 2016

@author: Klint

Module for Parsing CSV file
'''
import csv
from collections import defaultdict

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
                print row
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
                        raise CSVParseRowError
                else:
                    bStarted = bCheckStarted(row)
        except CSVParseRowError:
            print 'Row {} is invalid'.format(csvreader.line_num)
            return {}
        except:
            print 'CSV is invalid'
            return {}
    if(bCheckRequired(dictCSV, setRequired)):
        return dictCSV
    else:
        raise MissingRequiredKeyError

## private functions
def bCheckStarted(row):
    return len(row) >= 3 and row[0] == 'KEY' and row[1] == 'VAL' and row[2] == 'NOTE'

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

if __name__ == '__main__':
    print dictReadCsv('test.csv')
    try:
        pass
    #   print dictReadCsv('test.csv', {'STANDBY'})    
    except MissingRequiredKeyError:
        print 'MissingRequiredKeyError'
    print listReadCsv('test.csv')
    #print dictReadCsv('test.csv', {'PAPS_ACTIVE'})
    #print dictReadCsv('test.csv', {'PAPS_ACTIVE', 'PAPS_STANDBY'})    
	
## COMMENT: Please remove obsolete print lines or comment as to what they did and why they are commented out	
