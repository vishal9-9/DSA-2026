array = [1, 2, 3, 4, 5]
to_search = 5

print("Linear Search")


def solution(arr: list, to_search: int):
    for i in range(0, len(arr)):
        if arr[i] == to_search:
            return i

    return -1


print(solution(arr=array, to_search=to_search))


array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array_2 = [2, 3, 4, 4, 5, 11, 12]
print()
print("Union of Two Sorted Arrays")


def solution(array_1: list[int], array_2: list[int]):
    merged_array = []
    left_pointer = 0
    right_pointer = 0

    while left_pointer < len(array_1) and right_pointer < len(array_2):
        if array_1[left_pointer] < array_2[right_pointer]:
            if (
                not merged_array or merged_array[-1] != array_1[left_pointer]
            ):  # On the first insertion, there is no merged_array [] Accessing merged_array[-1] on an empty list would crash and Is the current element different from the last one we added.
                merged_array.append(array_1[left_pointer])
            left_pointer += 1
        elif array_1[left_pointer] > array_2[right_pointer]:
            if not merged_array or merged_array[-1] != array_2[right_pointer]:
                merged_array.append(array_2[right_pointer])
            right_pointer += 1
        else:  # Equal
            if not merged_array or merged_array[-1] != array_1[left_pointer]:
                merged_array.append(array_1[left_pointer])
            left_pointer += 1
            right_pointer += 1

    while left_pointer < len(array_1):
        if not merged_array or merged_array[-1] != array_1[left_pointer]:
            merged_array.append(array_1[left_pointer])
        left_pointer += 1

    while right_pointer < len(array_2):
        if not merged_array or merged_array[-1] != array_2[right_pointer]:
            merged_array.append(array_2[right_pointer])
        right_pointer += 1

    return merged_array


print(solution(array_1=array_1, array_2=array_2))


array = [0, 1, 2]

print()
print(
    "Find the missing number in an array"
)  # Below More Optimal Solution is Provided O(n) Time Complexity This one is O(n log n)


def sort_(arr: list, start_index, middle_index: int, end_index: int):
    left_pointer = start_index
    right_pointer = middle_index + 1
    temp = []

    while left_pointer <= middle_index and right_pointer <= end_index:
        if arr[left_pointer] <= arr[right_pointer]:
            temp.append(arr[left_pointer])
            left_pointer += 1
        else:
            temp.append(arr[right_pointer])
            right_pointer += 1

    while left_pointer <= middle_index:
        temp.append(arr[left_pointer])
        left_pointer += 1

    while right_pointer <= end_index:
        temp.append(arr[right_pointer])
        right_pointer += 1

    for i in range(start_index, end_index + 1):
        arr[i] = temp[i - start_index]


def merge_sort(arr: list, start_index: int, end_index: int):
    if start_index >= end_index:
        return

    middle_index = (start_index + end_index) // 2
    merge_sort(arr=arr, start_index=start_index, end_index=middle_index)
    merge_sort(arr=arr, start_index=middle_index + 1, end_index=end_index)
    sort_(
        arr=arr, start_index=start_index, middle_index=middle_index, end_index=end_index
    )


def solution(arr: list):
    merge_sort(arr=arr, start_index=0, end_index=len(arr) - 1)

    if arr[0] != 0:
        return 0

    for i in range(0, len(arr) - 1):
        if arr[i + 1] != arr[i] + 1:
            return arr[i] + 1

    return arr[len(arr) - 1] + 1


print(solution(arr=array))


# We know that the summation of the first N numbers is (N*(N+1))/2. We can say this S1. Now, in the given array, every number between 1 to N except one number is present. So, if we add the numbers of the array (say S2), the difference between S1 and S2 will be the missing number. Because, while adding all the numbers of the array, we did not add that particular number that is missing.

array = [0, 1, 2]

print()
print("Find the missing number in an array")


def solution(arr: list):
    n = len(arr)

    sum_of_n_natural_numbers = (n * (n + 1)) / 2

    actual_sum = 0

    for i in arr:
        actual_sum += i

    return int(sum_of_n_natural_numbers - actual_sum)


print(solution(arr=array))


array = [1, 1, 0, 1, 1, 1]

print()
print("Count Maximum Consecutive One's in the array")


def solution(arr: list):
    max_ = 0
    current_max = 0

    for i in range(0, len(arr)):
        if arr[i] == 1:
            current_max += 1
            max_ = max(current_max, max_)
        else:
            current_max = 0
    return max_


print(solution(arr=array))
