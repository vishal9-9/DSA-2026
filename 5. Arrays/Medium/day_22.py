print("Rearrange Array Elements by Sign")

arr = [1, 2, -3, -1, -2, -3]


def solution_1(arr: list[int]):
    positive = []
    negative = []

    for i in arr:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(i)

    if len(positive) > len(negative):
        for i in range(0, len(negative)):
            arr[2 * i] = positive[i]
            arr[2 * i + 1] = negative[i]
        to_contiue_index = len(negative) * 2
        for i in range(len(negative), len(positive)):
            arr[to_contiue_index] = positive[i]
            to_contiue_index += 1
    else:
        for i in range(0, len(positive)):
            arr[2 * i] = positive[i]
            arr[2 * i + 1] = negative[i]
        to_contiue_index = len(positive) * 2
        for i in range(len(positive), len(negative)):
            arr[to_contiue_index] = negative[i]
            to_contiue_index += 1


solution_1(arr=arr)
print(arr)


print()
print("next_permutation : find next lexicographically greater permutation")

arr = [2, 1, 5, 4, 3, 0, 0]
# arr = [1, 4, 3, 2]


# Step 1 find element where graph Brakes (if at any movement element[i] > element[i - 1] that is our breakpoint)
def solution_2(arr: list[int]):
    breakpoint = -1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i - 1] < arr[i]:
            breakpoint = i - 1
            break
    return breakpoint


print(solution_2(arr))
