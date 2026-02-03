array = [8, 10, 5, 7, 9]

print("Find the Largest element in an array")


def find_max(array: list):
    max_ = array[0]

    for i in range(1, len(array)):
        max_ = max(array[i], max_)

    return max_


print(find_max(array=array))


array = [1, 2, 4, 7, 7, 5]


print()
print("Find Second Smallest and Second Largest Element in an array")


def solution(array: list):
    min_ = float("inf")
    max_ = float("-inf")
    s_min_ = float("inf")
    s_max_ = float("-inf")

    for x in array:
        # minimum
        if x < min_:
            s_min_ = min_
            min_ = x
        elif min_ < x < s_min_:
            s_min_ = x

        # maximum
        if x > max_:
            s_max_ = max_
            max_ = x
        elif s_max_ < x < max_:
            s_max_ = x

    return (s_min_, s_max_)


print(solution(array=array))


print()
print("Check if an Array is Sorted")

array = [1, 2, 4, 7, 7, 5]


def solution(arr: list):
    for i in range(1, len(arr)):
        if not arr[i - 1] <= arr[i]:
            return False
    return True


print(solution(arr=array))

print()
print("Remove Duplicates in-place from Sorted Array")

array = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]


def solution(arr: list):
    if not arr:
        return arr

    write = 1

    for i in range(1, len(arr)):
        if arr[i - 1] != arr[i]:
            arr[write] = arr[i]
            write += 1

    for i in range(write, len(arr)):
        arr[i] = "_"

    return arr


print(solution(arr=array))
