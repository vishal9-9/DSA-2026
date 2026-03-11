print("Print subarray with maximum subarray sum")

nums = [2, 3, 5, -2, 7, -4]


def solution_1(nums: list[int]):
    sum_ = 0
    max_ = float("-inf")

    start = 0

    max_start = None
    max_end = None

    for index, num in enumerate(nums):
        sum_ += num
        if sum_ <= 0:
            sum_ = 0
            start = index
        if sum_ > max_:
            max_ = sum_
            max_start = start
            max_end = index

    return max_, max_start, max_end


print(solution_1(nums))

print()
print("Stock Buy And Sell")

prices = [7, 6, 4, 3, 1]


def solution_2(nums: list[int]):
    max_profit = 0

    for buy_index in range(0, len(nums)):
        for sell_index in range(buy_index + 1, len(nums)):
            profit = nums[sell_index] - nums[buy_index]
            max_profit = max(max_profit, profit)

    return max_profit


print(solution_2(prices))


def optimal_solution_2(nums: list[int]):
    min_ = nums[0]
    profit = 0

    for index in range(1, len(nums)):
        # selling price [nums[index]] - buying price [min_]
        current_profit = nums[index] - min_
        # Max Profit that we have seen till now
        profit = max(profit, current_profit)
        # is the current nums[index] the minimum so we can consider buying here for future
        min_ = min(min_, nums[index])

    return profit


print(optimal_solution_2(prices))
