def make_dict(arr1, arr2):
	new_dict = {}
	if len(arr1) >= len(arr2):
		new_dict = zip(arr1, arr2)
	return dict(new_dict)

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print make_dict(favorite_animal, name)