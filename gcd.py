import sys


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


value = gcd(int(sys.argv[1]), int(sys.argv[2]))
print(value)

exit()



