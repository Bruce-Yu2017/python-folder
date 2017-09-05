x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(arr):
	star = "*"
	for n in range(0,len(arr)):
		if type(arr[n]) == int:
			print star * arr[n]
		elif type(arr[n]) == str:
			print arr[n][0].lower() * len(arr[n])
draw_stars(x)