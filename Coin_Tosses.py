import random
def coin_toss():
		head = 0
		tail = 0
		print 'Starting the program...'
		for num in range(1,5001):
			coin = random.randint(0,1)
			if coin == 0:
				coin = 'head'
				head += 1
			else:
				coin = 'tail'
				tail += 1
			print "Attempt #" + str(num) + ": Throwing a coin... It's a " + coin + "! ... Got " + str(head) + " head(s) so far and " + str(tail) + " tail(s) so far"
		print 'Ending the program, thank you!'
coin_toss()
