print("4 Sum | Find Quads that add up to a target value")

nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9


def solution_1(nums: list[int]):
    nums = sorted(nums)
    to_return = []

    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = len(nums) - 1

            while k < l:

                sum_ = nums[i] + nums[j] + nums[k] + nums[l]

                if sum_ < target:
                    k += 1
                elif sum_ > target:
                    l -= 1
                else:
                    to_return.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l - 1]:
                        l -= 1

    return to_return


print(solution_1(nums=nums))
