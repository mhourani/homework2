#!/usr/bin/env python3
# coding: utf-8
import json, urllib.request
import os
import pandas

#store contants
class Config:
    path_seperator="//"
    directory="/tmp"
    json_file="converter_input.json"
    csv_file="converter_input.csv"
    input_file="http://mysafeinfo.com/api/data?list=englishmonarchs&format=json" 

#create directoy if needed
if not os.path.exists(Config.directory):
    os.makedirs(Config.directory)

#read input file
with urllib.request.urlopen(Config.input_file) as jsonFile:
    jsonContent = json.loads(jsonFile.read().decode())

#write json file
with open(Config.directory+Config.path_seperator+Config.json_file, 'w') as fp:
    json.dump(jsonContent, fp, indent=0)

#load json into dataframe
df = pandas.DataFrame(jsonContent)

#write csv
df.to_csv(Config.directory+Config.path_seperator+Config.csv_file, index=False)

