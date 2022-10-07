#!/bin/env/python
import pandas as pd
import numpy as np
import json
from datetime import datetime
from zat.log_to_dataframe import LogToDataFrame
import glob
import os
import sys


logFile = sys.argv[1]
baseName =  sys.argv[2]
s3Bucket = sys.argv[3]

# Zat hangs if the file is not in ascii or if it is a conn-summary file
if baseName == 'conn-summary':
    print("conn-summary detected, exiting")
    sys.exit()

current_date = datetime.now()
dateDay = current_date.strftime('%d')
dateMonth = current_date.strftime('%m')
dateYear = current_date.strftime('%Y')
dateStr = current_date.strftime('%Y-%m-%d-%H')

print(logFile)
log_to_df = LogToDataFrame()
df = log_to_df.create_dataframe(logFile)
# add a type to make analysis easier in combined dataframes
df['type']=baseName

df.to_parquet(s3Bucket + dateYear + '/' + dateMonth + '/' + dateDay + '/' + baseName + '-' + dateStr + '.parquet',engine='fastparquet', compression='gzip')
