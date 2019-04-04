import sys
import math

#name = sys.argv[0]
x = float(sys.argv[1])
y = float(sys.argv[2])

max1 = (x + y + math.fabs(x-y)) / 2
min1 = (x + y - math.fabs(x-y)) / 2

print("Max=%f" %max1)
print("Min=%f" %min1)


