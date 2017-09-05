def filter(thing):
	if type(thing) == int and thing >= 100:
		print "That's a big number!"
	elif type(thing) == int and thing <= 100:
		print "That's a small number"
	elif type(thing) == str and len(thing) >= 50:
		print "Long sentence"
	elif type(thing) == str and len(thing) <= 50:
		print "Short sentence"
	elif type(thing) == list and len(thing) >= 10:
		print "Big list"
	elif type(thing) == list and len(thing) <= 10:
		print "Short list"

filter(300)
filter('good day how')
filter(['name','address','phone number','social security number']
)