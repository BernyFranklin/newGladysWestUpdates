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
	pathToJSONDataFiles = "C:\Users\d17hu\OneDrive\Documents\SJCC2022\Python\GitHub\SJCC2022Python\gladysProject\satelliteJSON"

	# read the satellite data
	data = readSat(sat, pathToJSONDataFiles)

	#creating dictionary
	satelitteDictionary = {}

	#loop to assign JSON with classes
	for elem in data:
		x = elem["x"]
		y = elem["y"]
		value = elem["value"]

	#finalizing value from x and y
		satelitteDictionary[x,y] = value

	return value
