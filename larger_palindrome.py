import sys

variable = int(sys.argv[1])


def reverse(a):
    rev = 0
    while a > 0:
        dig = a % 10
        rev = rev * 10 + dig
        a = a / 10
    return rev


i = variable+1
while i != 0:
    number = reverse(i)
    if i == number:
        print("The nearest larger palindrome number is: ")
        print(i)
        exit()
    else:
        i += 1

exit()









