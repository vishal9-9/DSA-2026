print("Count Subarray sum Equals K")

nums = [1, 2, 3]
k = 3


def solution_1(nums: list[int]):
    prefix_sumhash = {0: 1}
    sum_ = 0
    sub_array_count = 0

    for i in range(0, len(nums)):
        sum_ += nums[i]
        target_to_find = sum_ - k

        if target_to_find in prefix_sumhash:
            sub_array_count += prefix_sumhash.get(target_to_find)

        prefix_sumhash[sum_] = prefix_sumhash.get(sum_, 0) + 1

    return sub_array_count


print(solution_1(nums))
