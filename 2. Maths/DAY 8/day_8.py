import math


N = 12345

print("Reverse Digits of A Number")

reverse = 0

while N > 0:
    remainder = N % 10
    reverse = (
        reverse * 10
    ) + remainder  # At start reverse is 0. 0 * 10 = 0 + lastDigit gives us 5 as revnum now again when we multiply by 10 add 0 at unit place and adding lastDigit to that we get reverse till get < 0.
    N = N // 10

print(reverse)

print()

print("Check if a number is Palindrome or Not")

N = 123321
copy_of_n = N * 1

reverse = 0

while N > 0:
    last_digit = N % 10
    N = N // 10
    reverse = (reverse * 10) + last_digit

if reverse == copy_of_n:
    print("Palindrome")
else:
    print("Not a Palindrome")

print()

print("Check if a number is Armstrong Number or not")

N = 371
to_compare = N * 1

armstrong_check = 0

while N > 0:
    last_digit = N % 10
    armstrong_check += last_digit**3
    N = N // 10

if armstrong_check == to_compare:
    print("Armstrong")
else:
    print("Not Armstrong")


print()

print("Print all Divisors of a given Number")

N = 36

divisors = [1]

for i in range(2, N):
    if N % i == 0:
        if i in divisors or N // i in divisors:
            break
        divisors.append(i)
        if i != N // i:
            divisors.append(N // i)

divisors.append(N)

print(divisors)

print()

print("Check if a number is prime or not")

N = 17

divisors = []

for i in range(
    1, int(math.sqrt(N) + 1)
):  # After sqrt the Number repeats if N = 4 [1 x 4, 2 x 2, 4 x 1(here 1st one is repeating just digits are interchanged)] so we just find till sqrt and add also add both i as well as N // i if it is not same as i eg 6 x 6.
    if N % i == 0:
        divisors.append(i)
        if N // i != i:
            divisors.append(N // i)

if len(divisors) == 2:
    print("Prime")
else:
    print("Not Prime")
