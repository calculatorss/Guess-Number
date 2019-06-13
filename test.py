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

    print("A", A, "B", B)


while True:
    a = random.randint(0, 9999)
    s = "{:0>4d}".format(a)
    if is_different(s):
        break

print(s)

x = input("please enter four number\n")


while True:
    if len(x) == 4:
        score(x)
        break
    elif is_different(x):
        x = input("please enter four number\n")

    else:
        print("please enter four number")
