import string
from random import *
min_char = 1
max_char = 200

#word
for i in range(1,1500):
	allchar = string.ascii_letters
	print "".join(choice(allchar) for x in range(randint(min_char, max_char)))

#filename
for i in range(1,1500):
	allchar = string.ascii_letters
	a =  "".join(choice(allchar) for x in range(randint(min_char, max_char)))
	a =  a + ".".join(choice(allchar) for x in range(randint(1, 3)))

#sentence
for i in range(1,3000):
	allchar = string.ascii_letters + "!" + " " + "_" + string.digits
	print "".join(choice(allchar) for x in range(randint(min_char, max_char)))

#IP atau domain
for i in range(1,1500):
	allchar = string.ascii_letters
	alldigit = string.digits
	print "".join(choice(allchar) for x in range(4)) + "." + "".join(choice(allchar) for x in range(4)) + "." + "".join(choice(allchar) for x in range(4)) + "." + "".join(choice(allchar) for x in range(4)) 
	print "".join(choice(alldigit) for x in range(3)) + "." + "".join(choice(alldigit) for x in range(3)) + "." + "".join(choice(alldigit) for x in range(3)) + "." + "".join(choice(alldigit) for x in range(3)) 
