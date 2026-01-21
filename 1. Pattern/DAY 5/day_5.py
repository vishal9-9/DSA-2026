n = 5

print("Pattern 18")
for i in range(n, 0, -1):
    char = chr(ord("A") + (n - 1))
    for j in range((n - i) + 1, 0, -1):
        print(chr(ord(char) - (j - 1)), end="")
    print()


print()
print("Pattern 19")

for i in range(0, n):
    for k in range(0, n - i):
        print("*", end="")
    for j in range(0, i):
        print(2 * " ", end="")
    for k in range(0, n - i):
        print("*", end="")
    print()
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    for k in range(0, (n - i) - 1):
        print(2 * " ", end="")
    for j in range(0, i + 1):
        print("*", end="")
    print()
    

print()
print("Pattern 20")

for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    for k in range(0, (n - i) - 1):
        print(2 * " ", end="")
    for j in range(0, i + 1):
        print("*", end="")
    print()
for i in range(0, n - 1):
    for j in range(0, (n - i) - 1):
        print("*", end="")
    for k in range(0, i + 1):
        print(2 * " ", end="")
    for j in range(0, (n - i) - 1):
        print("*", end="")
    print()
