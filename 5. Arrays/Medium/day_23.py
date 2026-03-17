print("Leaders in an Array")

arr = [4, 7, 1, 0]


def solution_1(arr: list[int]):
    max_ = float("-inf")
    leaders = []

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_:
            leaders.append(arr[i])
            max_ = arr[i]
    return leaders


print(solution_1(arr=arr))

print()
print("Longest Consecutive Sequence in an Array")

nums = [100, 4, 200, 1, 3, 2, 1, 5, 6, 7]


def solution_2(arr: list[int]):
    set_ = set()
    for i in arr:
        set_.add(i)

    current_longest = 1
    longest = 1
    for i in set_:
        if i - 1 not in set_:
            while i + 1 in set_:
                current_longest += 1
                i += 1
            longest = max(current_longest, longest)
            current_longest = 1
    return longest


print(solution_2(arr=nums))
