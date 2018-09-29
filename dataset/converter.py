# This class is converting string to input array of features
import csv
from pprint import pprint
import random

def countfeature(str, isattack):
	#if is attack is 0, then it's normal
	input_features = [0] * 70
	for c in str:
		#if pattern.match(c): #for alphabet
		#	input_features[0] += 1
		if (c.lower() == 'a'):
			input_features[0] += 1
		elif (c.lower() == 'b'):
			input_features[1] += 1
		elif (c.lower() == 'c'):
			input_features[2] += 1
		elif (c.lower() == 'd'):
			input_features[3] += 1
		elif (c.lower() == 'e'):
			input_features[4] += 1
		elif (c.lower() == 'f'):
			input_features[5] += 1
		elif (c.lower() == 'g'):
			input_features[6] += 1
		elif (c.lower() == 'h'):
			input_features[7] += 1
		elif (c.lower() == 'i'):
			input_features[8] += 1
		elif (c.lower() == 'j'):
			input_features[9] += 1
		elif (c.lower() == 'k'):
			input_features[10] += 1
		elif (c.lower() == 'l'):
			input_features[11] += 1
		elif (c.lower() == 'm'):
			input_features[12] += 1
		elif (c.lower() == 'n'):
			input_features[13] += 1
		elif (c.lower() == 'o'):
			input_features[14] += 1
		elif (c.lower() == 'p'):
			input_features[15] += 1
		elif (c.lower() == 'q'):
			input_features[16] += 1
		elif (c.lower() == 'r'):
			input_features[17] += 1
		elif (c.lower() == 's'):
			input_features[18] += 1
		elif (c.lower() == 't'):
			input_features[19] += 1
		elif (c.lower() == 'u'):
			input_features[20] += 1
		elif (c.lower() == 'v'):
			input_features[21] += 1
		elif (c.lower() == 'x'):
			input_features[22] += 1
		elif (c.lower() == 'y'):
			input_features[23] += 1
		elif (c.lower() == 'z'):
			input_features[24] += 1
		elif (c == '0'):
			input_features[25] += 1
		elif (c == '1'):
			input_features[26] += 1
		elif (c == '2'):
			input_features[27] += 1
		elif (c == '3'):
			input_features[28] += 1
		elif (c == '4'):
			input_features[29] += 1
		elif (c == '5'):
			input_features[30] += 1
		elif (c == '6'):
			input_features[31] += 1
		elif (c == '7'):
			input_features[32] += 1
		elif (c == '8'):
			input_features[33] += 1
		elif (c == '9'):
			input_features[34] += 1
		elif (c == "~"):
			input_features[35] += 1
		elif (c == "!"):
			input_features[36] += 1
		elif (c == "@"):
			input_features[37] += 1
		elif (c == "#"):
			input_features[38] += 1
		elif (c == "$"):
			input_features[39] += 1
		elif (c == "%"):
			input_features[40] += 1
		elif (c == "^"):
			input_features[41] += 1
		elif (c == "&"):
			input_features[42] += 1
		elif (c == "*"):
			input_features[43] += 1
		elif (c == "("):
			input_features[44] += 1
		elif (c == ")"):
			input_features[45] += 1
		elif (c == "_"):
			input_features[46] += 1
		elif (c == "+"):
			input_features[47] += 1
		elif (c == "{"):
			input_features[48] += 1
		elif (c == "}"):
			input_features[49] += 1
		elif (c == "|"):
			input_features[50] += 1
		elif (c == ":"):
			input_features[51] += 1
		elif (c == "\""):
			input_features[52] += 1
		elif (c == "<"):
			input_features[53] += 1
		elif (c == ">"):
			input_features[54] += 1
		elif (c == "?"):
			input_features[55] += 1
		elif (c == "`"):
			input_features[56] += 1
		elif (c == "-"):
			input_features[57] += 1
		elif (c == "="):
			input_features[58] += 1
		elif (c == "["):
			input_features[59] += 1
		elif (c == "]"):
			input_features[60] += 1
		elif (c == "\\"):
			input_features[61] += 1
		elif (c == ";"):
			input_features[62] += 1
		elif (c == "'"):
			input_features[63] += 1
		elif (c == ","):
			input_features[64] += 1
		elif (c == "."):
			input_features[65] += 1
		elif (c == "/"):
			input_features[66] += 1
		elif (c == " "):
			input_features[67] += 1
		else: #For chars outside alphabet and symbol
			input_features[68] += 1  

	if (isattack):
		input_features[69] = 1

	return input_features

lists = []
for line in open('normal_string'):
	lists.append(countfeature(line, False))

for line in open('attack_string'):
	lists.append(countfeature(line, True))

with open("dataset.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(lists)