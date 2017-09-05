#part 1
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def dict_1(dic_name):
# 	data_group = ""
# 	for n in range(len(dic_name)):
		
# 		for data in dic_name[n].itervalues():
# 			data_group += data + " "
# 		data_group += "\n"
# 	print data_group
# dict_1(students)

#part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def dict_2(dic_name2):
	
 	group = ""
 	for key, value in dic_name2.iteritems():
 		group += key + "\n"
 		for secvalue in range(len(value)):
 			group += (str(secvalue + 1) + " - ")
 			length = 0
 			for thivalue in value[secvalue].itervalues():	
 				group += thivalue + " "
 				length += len(thivalue)
 			group += " - " + str(length)
 			group += "\n"
 		
 	print group		
dict_2(users)








