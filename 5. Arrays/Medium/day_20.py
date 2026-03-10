print("Find the Majority Element that occurs more than N/2 times")

nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
# Output: 7


def solution_1(nums: list[int]) -> int:
    hash_map = {}

    for i in nums:
        hash_map[i] = hash_map.get(i, 0) + 1

    for key, value in hash_map.items():
        if value > len(nums) // 2:
            return key
        return -1


print(solution_1(nums))

print()


def moore_voting_algo(nums: list[int]) -> int:
    count = 0
    element = None

    for elm in nums:
        if count == 0:
            element = elm
            count += 1
        elif element == elm:
            count += 1
        else:
            count -= 1

    count = 0
    for elm in nums:
        if element == elm:
            count += 1

    if count > len(nums) // 2:
        return element
    return -1


print(moore_voting_algo(nums))

print()
print("Kadane's Algorithm : Maximum Subarray Sum in an Array")

nums = [2, 3, 5, -2, 7, -4]
# Output: 15


def kadane_algo(nums: list[int]) -> int:
    sum_ = 0
    max_ = float("-inf")

    for index, num in enumerate(nums):
        sum_ += num
        max_ = max(max_, sum_)
        if sum_ < 0:
            sum_ = 0
    return max_


print(kadane_algo(nums))
