from sys import argv
script, filename = argv
txt = open(filename) #creates a file object that later can be read by .read()

print "Here's your file %r:" % filename
print txt.read() # gives the opened a file (the txt file object) a command to \n
#read its contents and prints them
print "Type the filename again:"
file_again=raw_input("> ")
txt_again = open(file_again) #has to be the same file since the path is \n
#only provided in the commandline argument

print txt_again.read()

txt.close()#closes the file
txt_again.close() #wondering if this is needed - it points to the same file as\n
# txt, right?
