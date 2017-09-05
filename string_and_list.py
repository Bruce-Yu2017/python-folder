# #Find and Replace
# words = "It's thanksgiving day. It's my birthday,too!"
# print words.find('day')
# new_words = words.replace('day', 'month', 1)
# print new_words

# #Min and Max
# x = [2,54,-2,7,12,98]
# print min(x)
# print max(x)

# #First and Last
# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0]
# print x[len(x) - 1]
# x_new = []
# x_new.append(x[0])
# x_new.append(x[len(x) - 1])
# print x_new

#New List
import collections
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
x_new2 = []
for num in range(0,6):
	x_new2.append(x.pop(0))
print x_new2
print x
x.insert(0,x_new2)
print x


