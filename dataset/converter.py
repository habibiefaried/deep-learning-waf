# This class is converting string to input array of features
import csv
from pprint import pprint
import re
import random

def countfeature(str, isattack):
	#if is attack is 0, then it's normal
	input_features = [0] * 37
	pattern = re.compile("^[a-zA-Z0-9]+$")

	#~ ! @ # $ % ^ & * ( ) _ + { } | : " < > ? ` - = [ ] \ ; ', . / <<<SPACE>>>
	for c in str:
		if pattern.match(c): #for alphabet
			input_features[0] += 1
		elif (c == "~"):
			input_features[1] += 1
		elif (c == "!"):
			input_features[2] += 1
		elif (c == "@"):
			input_features[3] += 1
		elif (c == "#"):
			input_features[4] += 1
		elif (c == "$"):
			input_features[5] += 1
		elif (c == "%"):
			input_features[6] += 1
		elif (c == "^"):
			input_features[7] += 1
		elif (c == "&"):
			input_features[8] += 1
		elif (c == "*"):
			input_features[9] += 1
		elif (c == "("):
			input_features[10] += 1
		elif (c == ")"):
			input_features[11] += 1
		elif (c == "_"):
			input_features[12] += 1
		elif (c == "+"):
			input_features[13] += 1
		elif (c == "{"):
			input_features[14] += 1
		elif (c == "}"):
			input_features[15] += 1
		elif (c == "|"):
			input_features[16] += 1
		elif (c == ":"):
			input_features[17] += 1
		elif (c == "\""):
			input_features[18] += 1
		elif (c == "<"):
			input_features[19] += 1
		elif (c == ">"):
			input_features[20] += 1
		elif (c == "?"):
			input_features[21] += 1
		elif (c == "`"):
			input_features[22] += 1
		elif (c == "-"):
			input_features[23] += 1
		elif (c == "="):
			input_features[24] += 1
		elif (c == "["):
			input_features[25] += 1
		elif (c == "]"):
			input_features[26] += 1
		elif (c == "\\"):
			input_features[27] += 1
		elif (c == ";"):
			input_features[28] += 1
		elif (c == "'"):
			input_features[29] += 1
		elif (c == ","):
			input_features[30] += 1
		elif (c == "."):
			input_features[31] += 1
		elif (c == "/"):
			input_features[32] += 1
		elif (c == " "):
			input_features[33] += 1
		else: #For chars outside alphabet and symbol
			input_features[34] += 1  
		input_features[35] += 1 #counting length

	if (isattack):
		input_features[36] = 1
	return input_features

lists = []
for line in open('normal_string'):
	lists.append(countfeature(line, False))

for line in open('attack_string'):
	lists.append(countfeature(line, True))

random.shuffle(lists)

with open("dataset.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(lists)