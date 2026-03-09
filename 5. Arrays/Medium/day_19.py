print("Two Sum")

nums = [2, 7, 11, 15]
target = 9


def two_sum(nums: list[int], target: int):
    hash_map = {}
    for i in range(0, len(nums)):
        new_target = target - nums[i]
        new_target_index = hash_map.get(new_target, None)
        if new_target_index is not None:
            return [new_target_index, i]
        hash_map[nums[i]] = i
    return []


print(two_sum(nums=nums, target=target))

print()
print("Sort Colors")

nums = [2, 0, 2, 1, 1, 0]
# Output: [0, 0, 1, 1, 2, 2]


def sortColors(nums: list[int]) -> list[int]:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(1, len(nums)):
        while i > 0 and nums[i - 1] >= nums[i]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1
    return nums


print(sortColors(nums=nums))
