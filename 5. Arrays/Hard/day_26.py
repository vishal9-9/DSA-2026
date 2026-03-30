print("Find the elements that appears more than N/3 times in the array")

nums = [1, 2, 1, 1, 3, 2]


def solution_1(nums: list[nums]):
    count_1 = 0
    count_2 = 0

    ele_1 = float("-inf")
    ele_2 = float("-inf")

    for i in nums:

        if count_1 == 0 and i != ele_2:
            count_1 += 1
            ele_1 = i

        elif count_2 == 0 and i != ele_1:
            count_2 += 1
            ele_2 = i

        elif i == ele_1:
            count_1 += 1

        elif i == ele_2:
            count_2 += 1

        else:
            count_1 -= 1
            count_2 -= 1

    # Only 2 Elements can be repeated N/3 times Here N = 7, N // 3 = 2, Element has be present a minimum of 3 times. 3 + 3 = 6 .i.e. Maximum of 2 elements will always be returned and Minimum 0.
    times_to_repeat = (len(nums) // 3) + 1
    answer = []

    if nums.count(ele_1) >= times_to_repeat:
        answer.append(ele_1)
    if nums.count(ele_2) >= times_to_repeat:
        answer.append(ele_2)

    return answer


print(solution_1(nums))

print()
print("Program to generate Pascal's Triangle")

N = 5
r = 5
c = 3

answer = 1

for i in range(1, c + 1):
    answer = answer * (r - (i - 1))
    answer = answer / i

print(answer)
