from PIL import Image, ImageFilter
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def match(recallKey):
	# fileName is in string
	# recallKey in string
	key = []
	info = []
	with open("KeynInfo.txt") as f:
		for line in f:
			line_elts = line.strip(" \n").split(";")
			try:
				key.append(line_elts[0])
				info.append(line_elts[1].strip("\n"))
			except ValueError:
				pass
	n = len(key)
	for i in range(0, n):
		if recallKey == key[i]:
			return info[i]
	fuzzSample = []
	for i in range(0, n):
		fuzzSample.append(fuzz.ratio(recallKey, key[i]))
	fuzzMax = max(fuzzSample)
	if(fuzzMax > 40):
		maxIndex = fuzzSample.index(fuzzMax)
		return info[maxIndex]
	else:
		return "sample.jpg"
