import sys
import math

#name = sys.argv[0]
r = int(sys.argv[1])
sum1 = 0

for k in range(0,r):
    sum1 += pow(-1, k) * ((math.factorial(r)) / (math.factorial(k)))

print(int(sum1))


