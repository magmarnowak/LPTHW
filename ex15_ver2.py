print "Type the filename again:"
file_again=raw_input("> ") # either provide just the filename if it's in the\n
# same directory as the script, or provide the full path if it's in another\n
# folder.
txt_again = open(file_again)

print txt_again.read()

txt_again.close()
