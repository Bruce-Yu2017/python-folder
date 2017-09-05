my_dict = {
	"name": "Anna",
	"age": "101",
	"country": "United States",
	"favority language": "python"
}

def dict(dict_name):
	for key, data in dict_name.iteritems():
		print 'My ' + key + ' is ' + data
dict(my_dict)

# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python