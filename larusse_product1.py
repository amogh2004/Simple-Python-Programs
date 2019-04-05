import sys

#name = sys.argv[0]
a = int(sys.argv[1])
b = int(sys.argv[2])

product = 0

while b > 0:
    if b & 1:
        product += a
    a = a << 1
    b = b >> 1

print(product)
