def odd_even():
	for num in range(1, 2001):
		if num % 2 == 0:
			print 'Number is ' + str(num) + '. This is an even number'
		else:
			print 'Number is ' + str(num) + '. This is an odd number.'
odd_even()

def multiply(arr, num):
	for x in range(0, len(arr)):
		arr[x] *= num
	return arr
a = [2,4,10,16]
b = multiply(a, 5)
print b

def layered_multiples(arr):
	lis = []
	for num in range(0, len(arr)):
		lis.append([1] * arr[num])
	return lis
x = layered_multiples(multiply([2,4,5],3))
print x

