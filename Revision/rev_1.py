# Pattern 1
# ***
# ***
# ***


def pattern_1(n: int = 4):
    for i in range(0, n):
        for j in range(0, n):
            print("*", end="")
        print()


pattern_1()


# Pattern 2
# *
# **
# ***

print()


def pattern_2(n: int = 4):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end="")
        print()


pattern_2()

# Pattern 3
# 1
# 12
# 123

print()


def pattern_3(n: int = 4):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(j + 1, end="")
        print()


pattern_3()


# Pattern 4
# 1
# 22
# 333

print()


def pattern_4(n: int = 4):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(i + 1, end="")
        print()


pattern_4()

# Pattern 5
# ***
# **
# *

print()


def pattern_5(n: int = 4):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end="")
        print()


pattern_5()

# Pattern 6
# 123
# 12
# 1

print()


def pattern_6(n: int = 4):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end="")
        print()


pattern_6()

# Pattern 7
#   *
#  ***
# *****

print()


def pattern_7(n: int = 5):
    for i in range(0, n):
        for j in range(0, (n - 1) - i):
            print(" ", end="")
        for k in range(0, (2 * i) + 1):
            print("*", end="")
        print()


pattern_7()


# Pattern 8
# *********
#  *******
#   *****
#    ***
#     *

print()


def pattern_8(n: int = 5):
    for i in range(n, 0, -1):
        for j in range(0, n - i):
            print(" ", end="")
        for k in range(0, (2 * i) - 1):
            print("*", end="")
        print()


pattern_8()


# Pattern 9
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

print()


def pattern_9(n: int = 5):
    for i in range(0, n):
        for j in range(0, (n - 1) - i):
            print(" ", end="")
        for k in range(0, (2 * i) + 1):
            print("*", end="")
        print()
    for i in range(n, 0, -1):
        for j in range(0, n - i):
            print(" ", end="")
        for k in range(0, (2 * i) - 1):
            print("*", end="")
        print()


pattern_9()

# Pattern 10
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


print()


def pattern_10(n: int = 5):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end="")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            print("*", end="")
        print()


pattern_10()

# Pattern 11
# 1
# 01
# 101
# 0101
# 10101


print()


def pattern_11(n: int = 5):
    for i in range(1, n + 1):
        start = i % 2
        for j in range(0, i):
            print(start, end="")
            start = abs(start - 1)
        print()


pattern_11()


# Pattern 12
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

print()


def pattern_12(n: int = 5):
    for i in range(1, n + 1):
        for j in range(0, i):
            print(j + 1, end="")
        for k in range(n - i, 0, -1):
            print("  ", end="")
        for k in range(0, i):
            print(k + 1, end="")
        print()


pattern_12()


# Pattern 13
# 1
# 23
# 456
# 78910
# 1112131415

print()


def pattern_13(n: int = 5):
    start = 1
    for i in range(1, n + 1):
        for j in range(0, i):
            print(start, end="")
            start += 1
        print()


pattern_13()


# Pattern 14
# A
# AB
# ABC
# ABCD
# ABCDE

print()


def pattern_14(n: int = 5):
    for i in range(1, n + 1):
        for j in range(0, i):
            print(chr(ord("A") + j), end="")
        print()


pattern_14()

# Pattern 15
# ABCDE
# ABCD
# ABC
# AB
# A

print()


def pattern_15(n: int = 5):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print(chr(ord("A") + j), end="")
        print()


pattern_15()

# Pattern 16
# A
# BB
# CCC
# DDDD
# EEEEE

print()


def pattern_15(n: int = 5):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(chr(ord("A") + i), end="")
        print()


pattern_15()

# Pattern 17
#     A
#    AB
#   ABC
#  ABCD
# ABCDE

print()


def pattern_16(n: int = 5):
    for i in range(0, n):
        for k in range(0, n - i - 1):
            print(" ", end="")
        for j in range(0, i + 1):
            print(chr(ord("A") + j), end="")
        print()


pattern_16()


# Pattern 17
#    A
#   ABA
#  ABCBA
# ABCDCBA


print()


def pattern_17(n: int = 5):
    for i in range(0, n):
        for k in range(0, n - i - 1):
            print(" ", end="")
        current_charcter = ord("A") - 1
        for j in range(0, (2 * i) + 1):
            if j <= ((2 * i) + 1) // 2:
                current_charcter = current_charcter + 1
            else:
                current_charcter = current_charcter - 1
            print(chr(current_charcter), end="")
        print()


pattern_17()


# Pattern 18
# E
# DE
# CDE
# BCDE
# ABCDE


print()


def pattern_18(n: int = 5):
    for i in range(n, 0, -1):
        start_chr = ord("A") + n - 1
        for j in range((n - i), -1, -1):
            print(chr(start_chr - j), end="")
        print()


pattern_18()


# Pattern 19
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


print()


def pattern_19(n: int = 5):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end="")
        for k in range(0, n - i):
            print("  ", end="")
        for l in range(0, i):
            print("*", end="")
        print()
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end="")
        for k in range(0, n - i - 1):
            print("  ", end="")
        for l in range(0, i + 1):
            print("*", end="")
        print()


pattern_19()


# Pattern 20
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


print()


def pattern_20(n: int = 5):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end="")
        for k in range(0, n - i - 1):
            print("  ", end="")
        for l in range(0, i + 1):
            print("*", end="")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            print("*", end="")
        for k in range(0, n - i):
            print("  ", end="")
        for l in range(0, i):
            print("*", end="")
        print()


pattern_20()

# Pattern 20
# ****
# *  *
# *  *
# ****


print()


def pattern_21(n: int = 5):
    for i in range(0, n):
        for j in range(0, n):
            if j == 0 or i == 0 or j == n - 1 or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


pattern_21()


# Pattern 22
# 555555555
# 544444445
# 543333345
# 543222345
# 543212345
# 543222345
# 543333345
# 544444445
# 555555555


print()


def pattern_22(n: int = 5):
    for i in range(0, 2 * n - 1):
        for j in range(0, 2 * n - 1):
            top = i
            left = j
            bottom = (2 * n) - 1 - i - 1
            right = (2 * n) - 1 - j - 1
            print(n - min(min(top, left), min(bottom, right)), end="")
        print()


pattern_22()
