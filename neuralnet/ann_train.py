# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint

# Importing the dataset
dataset = pd.read_csv('../dataset/dataset.csv')
X = dataset.iloc[:, 1:36].values
y = dataset.iloc[:, 36].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 15)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 18, kernel_initializer = 'uniform', activation = 'relu', input_dim = 35))
classifier.add(Dropout(0.5))

# Adding the second hidden layer
classifier.add(Dense(units = 18, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dropout(0.5))

# Adding the second hidden layer
classifier.add(Dense(units = 18, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dropout(0.5))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 50, epochs = 100)

# serialize model to JSON
classifier_json = classifier.to_json()
with open("classifier.json", "w") as json_file:
    json_file.write(classifier_json)
# serialize weights to HDF5
classifier.save_weights("classifier.h5")
print("Saved model to disk")

# Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

pprint(cm)

def countfeature(str):
	#if is attack is 0, then it's normal
	import re
	input_features = [0] * 35
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

	return input_features

