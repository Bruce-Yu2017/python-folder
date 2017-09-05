def typelist(thing):
	number = 0
	string = ''
	for loop in thing:
		if isinstance(loop, int) or isinstance(loop, float):
			number += loop
		elif isinstance(loop, str):
			string += (" " + loop)
	if number and string:
		print "The list you entered is of mixed type"
		print "string: " + string
		print "Sum: ",number
	elif number:
		print "The list you entered is of integer type"
		print "Sum: ",number
	elif string:
		print "The list you entered is of string type"
		print "string: " + string



			
l = ['magical unicorns',19,'hello',98.98,'world']
typelist(l)