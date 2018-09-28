import string
from random import *
min_char = 10
max_char = 1000

for i in range(1,5000):
	allchar = string.ascii_letters + string.punctuation + " " + "_" + string.digits
	print "".join(choice(allchar) for x in range(randint(min_char, max_char)))

#IP atau domain
for i in range(1,1000):
	allchar = string.ascii_letters
	alldigit = string.digits
	print "".join(choice(allchar) for x in range(4)) + "." + "".join(choice(allchar) for x in range(4)) + "." + "".join(choice(allchar) for x in range(4)) + "." + "".join(choice(allchar) for x in range(4)) 
	print "".join(choice(alldigit) for x in range(3)) + "." + "".join(choice(alldigit) for x in range(3)) + "." + "".join(choice(alldigit) for x in range(3)) + "." + "".join(choice(alldigit) for x in range(3)) 
