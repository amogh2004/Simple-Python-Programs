import sys

name = sys.argv[0]
n = int(sys.argv[1])

sum1 = 1.0
term = 1.0

for i in range(1, n):
    term = term/i
    sum1 += term

print(name)
print(sum1)
