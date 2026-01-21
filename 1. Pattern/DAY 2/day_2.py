n = 5

print("Pattern 8")

for i in range(n, 0, -1):
    for j in range(0, n - i):
        print(" ", end="")
    for k in range((2 * i) - 1):
        print("*", end="")
    for l in range(0, n - i):
        print(" ", end="")
    print()


print()
print("Pattern 9")

for i in range(0, n):
    for j in range(0, (n - i) - 1):
        print(" ", end="")
    for k in range(0, ((2 * i) + 1)):
        print("*", end="")
    for l in range(0, (n - i) - 1):
        print(" ", end="")
    print()
for i in range(n, 0, -1):
    for j in range(0, n - i):
        print(" ", end="")
    for k in range((2 * i) - 1):
        print("*", end="")
    for l in range(0, n - i):
        print(" ", end="")
    print()
    

print()
print("Pattern 10")

for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()
    

print()
print("Pattern 11")

for i in range(1, n + 1):
    start = 1
    if i % 2 != 0:
        start = 1
    else:
        start = 0
    for j in range(1, i + 1):
        print(start, end="")
        start = 1 - start
    print()
