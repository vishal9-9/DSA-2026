n = 3

print("Pattern 1", end="\n")

for i in range(0, n):
    for j in range(0, n):
        print("*", end="")
    print(end="\n")

print()
print("Pattern 2")

for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    print(end="\n")

print()
print("Pattern 3")

for i in range(0, n):
    for j in range(0, i + 1):
        print(j + 1, end="")
    print(end="\n")

print()
print("Pattern 4")

for i in range(0, n):
    for j in range(0, i + 1):
        print(i + 1, end="")
    print(end="\n")

print()
print("Pattern 5")

for i in range(0, n):
    for j in range(n - i, 0, -1):
        print("*", end="")
    print(end="\n")

print()
print("Pattern 6")

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()



#   *         [2,1,2] [Space, Star, Space]
#  ***        [1,3,1]
# *****       [0,5,0]

print()
print("Pattern 7")

for i in range(n, 0, -1):
    for j in range(i - 1, 0, -1):
        print(" ", end="")
    for k in range(0, (2 * (n - i) + 1)):
        print("*", end="")
    print()