import random


def is_different(s):
    if len(s) == len(set(s)):
        return True
    else:
        return False


def score(x):
    A = 0
    B = 0
    for i, x in enumerate(x):

        if x == s[i]:
            A += 1
        elif x in s:
            B += 1

    return A, B


while True:
    a = random.randint(0, 9999)
    s = "{:0>4d}".format(a)
    if is_different(s):
        break

x = input("please enter four number\n")
while True:
    if len(x) == 4:
        A, B = score(x)
        print("A", A, "B", B)
        if A == 4:
            print("good")
            break

    elif is_different(x):
        print("please enter four different number")

    else:
        print("please enter number")

    x = input("please enter four number\n")
