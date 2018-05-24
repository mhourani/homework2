#!/usr/bin/env python3
# coding: utf-8

#Import json from monarch file
import json, urllib.request

if __name__ == "__main__":
	with urllib.request.urlopen("http://mysafeinfo.com/api/data?list=englishmonarchs&format=json") as jsonFile:
	    jsonContent = json.loads(jsonFile.read().decode())

	'''
	Note: the instructions did not say to sort so I did not

	if you want to sort the groups you coudl do the following:
	houses = sorted(list(set([x['hse'] for x in jsonContent])))
	cities = sorted(list(set([x['cty'] for x in jsonContent])))
	'''

	#create a set of the houses
	houses = list(set([x['hse'] for x in jsonContent]))

	#create a set of the cities
	cities = list(set([x['cty'] for x in jsonContent]))


	result = {}
	clist = set()
	house_dict = {}

	for c in cities:
	    for h in houses:
	        names = [d['nm'] for d in jsonContent if d['cty'] == c and d['hse'] == h]
	        house_dict[h] = names
	    result[c] = house_dict     

	#We could sort the names if we wanted
	json_string=json.dumps(result, indent=0, sort_keys=False)

	print(json_string)

