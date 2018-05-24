#!/usr/bin/env python3
# coding: utf-8

import pandas

#read baby names

import json, urllib.request

if __name__ == "__main__":
	with urllib.request.urlopen("https://data.cityofnewyork.us/api/views/25th-nujf/rows.json") as jsonFile:
	    data = json.loads(jsonFile.read().decode())

	#create data dataframe from json
	df = pandas.DataFrame(data['data'])

	#create columns datafra,e from json
	df2=pandas.DataFrame(data['meta']['view']['columns'])

	#name columns in the data dataframe
	df.columns = df2['name']

	#create copy with relevant columns
	df3=df[["Child's First Name", 'Gender', 'Ethnicity', 'Year of Birth', 'Rank', 'Count']]

	#save data as json to file
	df3.to_json('ny_baby_names.json')

	#filter based on year of birth
	df4 = df3[(df3['Year of Birth'].astype(int) >= 2012) & (df['Year of Birth'].astype(int) <= 2014)]

	#create count by grouping of child's first name and ethnicity
	df5=df4[["Child's First Name", 'Ethnicity', 'Count']]
	grouped=df5.groupby(["Child's First Name", 'Ethnicity']).sum()

	#wite aggregated data as json
	grouped.to_json('ny_baby_names_by_name_and_ethnicity.json')

	#wite aggregated data as csv
	grouped.to_csv('ny_baby_names_by_name_and_ethnicity.csv')

