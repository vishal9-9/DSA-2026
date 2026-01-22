print("Check if the given String is Palindrome or not using Recursion")

word = "ABCDCBA"

def is_palindrome(string: str, l: int, r: int):
    if len(string) <= 0 or not string[l] == string[r]:
        return "Not a Palindrome"
    elif l >= r:
        return "Palindrome"
    return is_palindrome(string=string, l=l + 1, r=r - 1)

print(is_palindrome(string=word, l=0, r=len(word)-1))

print()

print("Print Fibonacci Series up to Nth term")

N = 10

print(0, 1, end=" ")
def print_fibbonacci_till_n(n: int, first_: int, second_: int, current_iteration: int):
    if current_iteration == N:
        print()
        return 
    print(first_ + second_, end=" ")
    print_fibbonacci_till_n(n=n, first_=second_, second_=first_+second_,current_iteration=current_iteration+1)

print_fibbonacci_till_n(n=N, first_=0, second_=1, current_iteration=1)    

print()
print("ii) using 2 recursion call")

def print_fib_of_n(n: int):
    if n <= 1:
        return n
    last = print_fib_of_n(n - 1)
    s_last = print_fib_of_n(n - 2)
    return last + s_last

print(print_fib_of_n(n=N))


print()
print("Array Subsequence using Recursion")

array = [3, 1, 2]


def find_all_subsequence(arr: list, index: int):
    if len(array) <= index:
        print(arr)
        return

    # Take
    arr.append(array[index])
    find_all_subsequence(arr=arr, index=index + 1)

    # Remove the taken element and proceed further eg arr = [3, 1, 2] this line causes arr = [3, 1] and index is already 2 so in Not take part base condtition hits and we get [3, 1]. next time It will be [3, 1] then this line casuses arr = [3] and next line (Not Take) will proceed with index = 2 and [3, 2] and then in next loop base condition hits we gett [3, 2].
    arr.pop()

    # Not Take
    find_all_subsequence(arr=arr, index=index + 1)


find_all_subsequence(arr=[], index=0)
