from sys import argv

script, filename = argv

print "We're going to earse %r." % filename
print "If you don't want that hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."

target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(3*("%s\n") % (line1, line2, line3))

print"Let's see how it looks when you read the file now."

target = open(filename, 'r')
print target.read()

print "Well, it all looks very good!"

print "And finally, we close it."

target.close()
