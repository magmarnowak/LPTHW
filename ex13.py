#Parameters, unpacking, variables
# running the script in powershell requires specifying the arguments, eg. > python <scriptfilename.py> <argument_1> <argument_2> <argument_3>
#note that command line arguments are returned as strings
from sys import argv #adding the argv module/library to the script from the Python module set (library)
#argv - arugument variable, it holds the arguments to be passed to the Python script when it is run
# in pro words: it imports the argv module from the sys package
script, first, second, third = argv #unpacks argv, it justs says: "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order"

fourth = raw_input("Name of your fourth variable: ") #added raw_input to combine both input methods

print "The script is called:", script
print "Your first variable is called:", first
print "Your second variable is called:", second
print "Your third variable is:", third
print "Your fourth variable is called:", fourth
