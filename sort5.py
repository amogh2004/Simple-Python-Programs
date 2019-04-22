import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

if a < b:
    if b < c:
        if d < b:
            if d < a:
                print(d, " ", a, " ", b, " ", c)
            else:
                print(a, " ", d, " ", b, " ", c)
        else:
            if d < c:
                print(a, " ", b, " ", d, " ", c)
            else:
                print(a, " ", b, " ", c, " ", d)
    else:
        if a < c:
            if d < c:
                if d < a:
                    print(d, " ", a, " ", c, " ", b)
                else:
                    print(a, " ", d, " ", c, " ", b)
            else:
                if d < b:
                    print(a, " ", c, " ", d, " ", b)
                else:
                    print(a, " ", c, " ", b, " ", d)
        else:
            if d < a:
                if d < c:
                    print(d, " ", c, " ", a, " ", b)
                else:
                    print(c, " ", d, " ", a, " ", b)
            else:
                if d < b:
                    print(c, " ", a, " ", d, " ", b)
                else:
                    print(c, " ", a, " ", b, " ", d)
else:
    if a < c:
        if d < a:
            if d < b:
                print(d, " ", b, " ", a, " ", c)
            else:
                print(b, " ", d, " ", a, " ", c)
        else:
            if d < c:
                print(b, " ", a, " ", d, " ", c)
            else:
                print(b, " ", a, " ", c, " ", d)
    else:
        if b < c:
            if d < c:
                if d < b:
                    print(d, " ", b, " ", c, " ", a)
                else:
                    print(b, " ", d, " ", c, " ", a)
            else:
                if d < a:
                    print(b, " ", c, " ", d, " ", a)
                else:
                    print(b, " ", c, " ", a, " ", d)
        else:
            if d < b:
                if d < c:
                    print(d, " ", c, " ", b, " ", a)
                else:
                    print(c, " ", d, " ", b, " ", a)
            else:
                if d < a:
                    print(c, " ", b, " ", d, " ", a)
                else:
                    print(c, " ", b, " ", a, " ", d)

exit()
