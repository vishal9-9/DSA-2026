import math


print("Given two integers N1 and N2, find their greatest common divisor")

# My Solution Find MIN and find all divisors of it once done store all divisors of min number then iterate over the divisors & see if other number is divisible by all divisors of min divisors and find the MAX

N1 = 20
N2 = 15

MIN = min(N1, N2)
MAX = max(N1, N2)
min_divisor = []

for i in range(1, int(math.sqrt(MIN)) + 1):
    if MIN % i == 0:
        min_divisor.append(i)
        if MIN // i != i:
            min_divisor.append(MIN // i)

GCD = 1

for j in min_divisor:
    if MAX % j == 0:
        GCD = max(GCD, j)

print("GCD is: ", GCD)
