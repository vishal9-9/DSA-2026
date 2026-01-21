n = 4

print("Pattern 17")

for i in range(0, n):
    for j in range(0, (n - i) - 1):
        print(" ", end="")
    char = "A"
    for k in range(0, (2 * i) + 1):
        if k < i:
            print(char, end="")
            char = chr(ord(char) + 1)
        else:
            print(char, end="")
            char = chr(ord(char) - 1)
    print()
