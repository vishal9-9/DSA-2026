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
    if breakpoint == -1:
        # Reverse array as arr is last of the permutation so if we reverse it we will reach to first of it.
        l, r = 0, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr
    else:
        for i in range(len(arr) - 1, breakpoint, -1):
            if arr[i] > arr[breakpoint]:
                arr[i], arr[breakpoint] = arr[breakpoint], arr[i]
                break

        # then reverse the array to as array was already in increasing order from back & job done
        l, r = breakpoint + 1, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr


print(solution_2(arr))
