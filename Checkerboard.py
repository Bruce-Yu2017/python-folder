#My answer
def checkerboard():
	for check in range(1, 5):
		print "* * * *\n" + ' ' + "* * * *"
checkerboard()

#standard answer
def checkerboard():
    for i in range(0, 8):
        if i%2 == 0:
            print "* " * 4
        else:
            print " *" * 4
