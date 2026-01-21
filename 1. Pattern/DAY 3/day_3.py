n = 5

print()
print("Pattern 12")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(0, n - i):
        print("  ", end="")
    for l in range(i, 0, -1):
        print(l, end="")
    print()

print()
print("Pattern 13")

num = 1
for i in range(1, n + 1):
    for j in range(0, i):
        print(num, end="")
        num += 1
    print()

print()
print("Pattern 14")

for i in range(0, n):
    for j in range(0, i + 1):
        print(chr(ord("A") + j), end="")
    print()

print()
print("Pattern 15")

for i in range(0, n):
    for j in range(0, n - i):
        print(chr(ord("A") + j), end="")
    print()

print()
print("Pattern 16")

for i in range(0, n):
    for j in range(0, i + 1):
        print(chr(ord("A") + i), end="")
    print()
    
print()
print("Pattern 17")

for i in range(0, n):
    for j in range(0, (n - i) - 1):
        print(" ", end="")
    for k in range(0, i + 1):
        print(chr(ord("A") + k), end="")
    for j in range(0, (n - i) - 1):
        print(" ", end="")
    print()
