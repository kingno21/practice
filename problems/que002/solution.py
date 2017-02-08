# first look
def sum1():
	fibo = [1, 2]
	while True:
		if (fibo[-2] + fibo[-1]) > 4000000:
			break
		fibo.append(fibo[-2] + fibo[-1])

	return fibo

print sum([i for i in sum1() if i % 2 == 0])

# found solution
prev, cur = 0, 1
total = 0
while True:
    prev, cur = cur, prev + cur
    if cur >= 4000000:
        break
    if cur % 2 == 0:
        total += cur

print(total)

# filter
fibo = [1, 2]
def sum2(a, b):
	if a + b >= 4000000:
		return
	fibo.append(a + b)
	sum2(b, a + b)

sum2(*fibo)
print sum(filter(lambda x: x % 2 == 0, fibo))
