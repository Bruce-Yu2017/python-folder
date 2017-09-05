Multiples
for num in range(1,1001):
	if num % 2 != 0:
		print num

for num2 in range(5,1000001):
	if num2 % 5 == 0:
		print num2

Sum List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
	sum += num
print sum

Average List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
	sum += num
average = sum / len(a)
print average