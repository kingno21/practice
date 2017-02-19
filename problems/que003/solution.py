# first look brute force

import math
max_value = 600851475143
final = 0
for i in range(2, int(math.sqrt(max_value)), 1):
	while max_value % i == 0:
		max_value = max_value / i
		final = i

print final

# found solution
num = 600851475143
i = 2
while i * i < num:
     while num % i == 0:
         num = num / i
     i = i + 1
print(num)

# lambda