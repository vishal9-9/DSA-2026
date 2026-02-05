array = [1, 2, 3, 4, 5]

print("Left Rotate the Array by One")


def solution(arr: list):
    temp = arr[0]

    for i in range(
        0, len(arr) - 1
    ):  # Because if we at last element index will be 4 and 4 + 1 = 5 which will cause out of bounds error.
        arr[i] = arr[i + 1]

    arr[-1] = temp

    return arr


print(solution(arr=array))


array = [1, 2, 3, 4, 5, 6, 7]

print()
print("Rotate array by K elements")


def solution(arr: list, k: set):
    k[0] = k[0] % len(
        arr
    )  # if k = 10 so 10 / 7 we will get 3 as we move array by 7 times(len of array) we get same array so we take modulo and only do iteration that many times.

    if k[1] == "right":
        temp = [*arr[(len(arr)) - k[0] : len(arr)]]
    else:
        temp = [*arr[0 : k[0]]]

    count = 0

    for i in range(k[0], len(arr)):
        arr[count] = arr[i]
        count += 1

    count = 0
    for j in range(len(arr) - k[0], len(arr)):
        arr[j] = temp[count]
        count += 1

    return arr


print(solution(arr=array, k=[15, "left"]))

array = [1, 2, 0, 1, 0, 4, 0]

print()
print("Move all Zeros to the end of the array")


def solution(arr: list):
    write = 0

    for i in range(0, len(array)):
        if arr[i] != 0:
            arr[write], arr[i] = arr[i], arr[write]
            write += 1

    return arr


print(solution(arr=array))

array = [1, 2, 0, 1, 0, 4, 0]

print()
print("Reverse a Array In a Range")


def solution(arr: list, start: int, end: int):
    if start < 0 or end >= len(arr) or start >= end:
        return arr

    left_pointer = start
    right_pointer = end

    while left_pointer < right_pointer:
        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
        left_pointer += 1
        right_pointer -= 1

    return arr


print(solution(arr=array, start=1, end=5))
