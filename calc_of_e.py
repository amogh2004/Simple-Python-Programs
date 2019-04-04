import sys
import math

#name = sys.argv[0]
n = int(sys.argv[1])
x = int(sys.argv[2])

sum1 = 1.0
term = 1.0

for i in range(1, n):
    term = pow(x, i) / math.factorial(i)
    sum1 += term

print(sum1)
