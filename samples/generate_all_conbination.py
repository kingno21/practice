# All possible combinations of strings from char array in Python

def pop_return_arr(array, val):
	tmp = array
	tmp.pop(array.index(val))
	return tmp

def gen(array):
	if len(array) == 1:
		return array[0]

	list = []
	for i in array:
		for j in gen(pop_return_arr(array[:], i)):
			list.append(i + j)

	return list

