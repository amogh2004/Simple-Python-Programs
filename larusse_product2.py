import sys

#name = sys.argv[0]
a = int(sys.argv[1])
b = int(sys.argv[2])

product = 0

while a > 0:
    if a % 2 == 1:
        product = product + b
    a = a // 2
    b = b * 2

print(product)
