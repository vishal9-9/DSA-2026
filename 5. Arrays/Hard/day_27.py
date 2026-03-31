print("3 Sum : Find triplets that add up to a zero")

nums = [-1, 0, 1, 2, -1, -4]


def solution_1(nums: list[int]):
    # important sort before running the solution
    nums = sorted(nums)
    to_return = []
    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum_ = nums[i] + nums[j] + nums[k]

            if sum_ < 0:
                j += 1
            elif sum_ > 0:
                k -= 1
            else:
                to_return.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return to_return


print(solution_1(nums=nums))
