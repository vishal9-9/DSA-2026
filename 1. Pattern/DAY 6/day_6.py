n = 4

print("Pattern 20")

for i in range(0,  n):
    for j in range(0, n):
        if i == 0 or i == (n - 1) or j == 0 or j == (n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()
print("Pattern 21")

to_sub = 2
compare = 0
to_print = 4
for i in range(0,  (2 * n) - 1):
    for j in range(0, (2 * n) - 1):
        if i == compare or j == compare or i == ((2 * n) - to_sub) or j == ((2 * n) - to_sub):
            print(to_print, end="")
    to_print -= 1
    compare += 1
    to_sub -= 1
    print()
