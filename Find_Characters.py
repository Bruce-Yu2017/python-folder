word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
for word in word_list:
	for subword in word:
		if 	subword == char:
			new_list.append(word)
print new_list