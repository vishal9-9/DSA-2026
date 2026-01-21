N = 5

print("Print 1 to N using Recursion")

def print_till_n(current_count: int, n: int):
    print(current_count, end="")
    if current_count == N:
        print()
        return
    print(end=", ")
    print_till_n(current_count=current_count + 1, n=n)

print_till_n(current_count=1, n=N)

print()

print("Print N to 1 using Recursion")

def print_to_n(current_count: int):
    print(current_count, end="")
    if current_count == 1:
        print()
        return
    print(end=", ")
    print_to_n(current_count=current_count - 1)
    
print_to_n(current_count=N)

print()

print("Sum of first N Natural Numbers i) Parameterized, ii) Functional Recursion")

print("i) Parameterized Recursion")

def sum_till_n(current_sum: int, n: int):
    current_sum += n
    if n == N:
        print(current_sum)
        return
    sum_till_n(current_sum=current_sum, n=n+1)

sum_till_n(current_sum=0, n=1)

print()
print("ii) Functional Recursion")

def sum_till_n_(n: int):
    if n == 0:
        return 0
    return n + sum_till_n_(n - 1)  # 5 + sum_(4) [5 + 4 + sum_(3) [5 + 4 + 3 + sum_(2) [5 + 4 + 3 + 2 + sum_(1) [5 + 4 + 3 + 2 + 1 + sum_(0) [5 + 4 + 3 + 2 + 1 + 0{base condition make the function ot return.} ] ] ] ] ]

print(sum_till_n_(n=N))

print()
print("Factorial of a Number Recursive")

def factorial(n: int):
    if n == 0:
        return 1
    if n < 0:
        return "undefined"

    return n * factorial(n - 1)

print(factorial(N))
