def ndigits(n):
    r = len(str(abs(n)))
    return r


def nwords(s):
    words = s.split(" ")
    return len(words)


def nsentense(s):
    return s.count(".")+s.count("?")+s.count("!")


def largest(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c


def panagram(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in letters:
        if i not in s:
            print(f"{i} is missing")
            return False
    return True


def dumpfile(fname):
    f = open(fname)
    for i in f:
        print(i)
    f.close()
