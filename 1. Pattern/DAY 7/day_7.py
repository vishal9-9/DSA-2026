n = 5

print("Pattern 22")

for i in range(0, (2 * n) - 1):
    for j in range(0, (2 * n) - 1):
        top = i
        left = j
        right = ((2 * n) - 2) - j
        bottom = ((2 * n) - 2) - i
        value = n - min(min(top, bottom), min(left, right))
        print(value, end="")
    print()
