# first look
def sum1(n, max_value):
	MAX = max_value
	total_value = 0
	for i in range(MAX):
		if i * n < MAX:
			total_value += i * n
		else:
			return total_value

print sum1(3, 1000) + sum1(5, 1000) - sum1(15, 1000)

# no extra variable
max_value = 1000
def sum2(n, p):
	if (n + p) >= max_value:
		return n

	return n + sum2(n + p, p)

print sum2(0, 3) + sum2(0, 5) - sum2(0, 15)

# short hand
def sum3(x):
	if max_value % x != 0:
		return sum([(i+1) * x for i in range(max_value/x)])
	else:
		return sum([(i+1) * x for i in range(max_value/x - 1)])

print  sum3(3) + sum3(5) - sum3(15)