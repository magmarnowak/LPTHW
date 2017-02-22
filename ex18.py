def print_two(*args): # *args works like argv but for functions,\n
# it's a placeholder for arguments, might come in handy when we can't specify\n
# the number ofparameters exactly
    arg1, arg2 = args #unpacks the arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
