import io
import json

"""
	Student: David Huynh
	Module: gladysSatellite
	Description: This module opens and reads the four data files on the disc based on the satellite name using the readSat funciton. It then finds and returns the value based on the x and y coordinates of that specific satellite.
"""


def readSat(sat, pathToJSONDataFiles):
	"""
		reads satellite data from a json file
		Students do NOT need to change the readSat function.
	"""

	# data file path
	fileName = sat + "-satellite.json"
	filePath = pathToJSONDataFiles + "/" + fileName

	# open the file
	try:
		fileHandle = open(filePath)
	except IOError:
		print("ERROR: Unable to open the file " + filePath)
		raise IOError

	# print("filePath = ", filePath)

	# read the file
	data = json.load(fileHandle)

	return data


def gpsValue(x, y, sat):
	"""
		1) creating a path for the readSat function to pull the right JSON file
		2)given x and y, outputs value based on whatever is saved in the JSON file
	"""
	pathToJSONDataFiles = "/Users/frankbernal/Documents/GitHub/newGladysWestUpdates/src/JSONs"
	dataValue = 0
	# read the satellite data
	data = readSat(sat, pathToJSONDataFiles)

	#creating dictionary
	satelitteDictionary = {}

	#loop to assign JSON with classes
	for elem in data:
		xVal = elem["x"]
		yVal = elem["y"]
		value = elem["value"]

	#finalizing value from x and y
		satelitteDictionary[(xVal,yVal)] = value
		
		#find the key and return value
		# if x or y is out of bounds throw error
		if (x, y) in satelitteDictionary:
			dataValue = satelitteDictionary[(x, y)]
		else:
			dataValue = "Error: NO DATA FOUND WITH THOSE VALUES"

	return dataValue
#print(gpsValue(99, 45, "latitude"))
#print(gpsValue(99, 46, "longitude"))
#print(gpsValue(99, 46, "altitude"))
#print(gpsValue(99, 46, "time"))