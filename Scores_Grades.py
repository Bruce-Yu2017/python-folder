import random
def score_grade():
	print 'Scores and Grades'
	
	
	
	for count in range(0,10):
		score = random.randint(60,100)
		grade = 'A'
		if score >= 60 and score <70:
			grade = 'D'
		elif score >= 70 and score <80:
			grade = 'C'
		elif score >= 80 and score <90:
			grade = 'B'
		elif score >= 90 and score <101:
			grade = 'A'
		print "Score: " + str(score) + "; Your grade is " + grade
	print 'End of the program. Bye!'
score_grade()

