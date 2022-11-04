import time
import csv
from datetime import datetime
import DVLAextract as DVLA

mycsv = 'cpdata.csv'

def WhatTime():
    now = datetime.now()
    return now.strftime('%d/%m/%Y %H:%M:%S')

def WriteToCSV(newline):
    with open(mycsv, 'a', newline='') as f_object:
        writer = csv.writer(f_object)
        writer.writerow(newline)
        f_object.close()