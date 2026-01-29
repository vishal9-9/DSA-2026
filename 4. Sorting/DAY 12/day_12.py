unsorted_array = [13, 46, 24, 52, 20, 9]  # Worst Case & Best Case O(n^2)

print("Selection Sort")

# Selecting the minimum and placing at position where element belongs. for 1st pass [9, 46, 24,..., 13]

for i in range(0, len(unsorted_array)):
    min_index = i
    for j in range(i + 1, len(unsorted_array)):
        if unsorted_array[min_index] > unsorted_array[j]:
            min_index = j
    unsorted_array[i], unsorted_array[min_index] = (
        unsorted_array[min_index],
        unsorted_array[i],
    )

print(unsorted_array)

unsorted_array = [13, 46, 24, 52, 20, 9]  # Worst Case O(n^2)
# unsorted_array = [1,2,3,4,5] Best Case O(n)
print()
print("Bubble Sort")

# Places the Biggest Element at last by check adjacent elements and swapping if left element is bigger than right element.
# 1st Pass => [13, 46, 24, 52, 20, 9] after comparing 13 and 46 as 13 is smaller than 46 no Swap.
# 2nd Pass => [13, 24, 46, 52, 20, 9] after comparing 46 and 24 as 24 is smaller than 46 we Swap.
# and so on at last we will have for first inner loop completion we will have [13, 24, 46, 20, 9, 52].
# this is working of bubble sort.
# did_swap if at any given moment in nested loop no swap happens then array has been sorted and we need to break out of it as it is no use of running.


for i in range(0, len(unsorted_array)):
    did_swap = False
    for j in range(1, len(unsorted_array) - i):
        if unsorted_array[j - 1] > unsorted_array[j]:
            unsorted_array[j - 1], unsorted_array[j] = (
                unsorted_array[j],
                unsorted_array[j - 1],
            )
            did_swap = True
    if not did_swap:
        break

print(unsorted_array)


unsorted_array = [13, 46, 24, 52, 20, 9]
print()
print("Insertion Sort")

# Insertion Sort works by placing the element in in it's correct position. we check right element with left and check if they need swap .i.e. right element is smaller than left.
# Pass 1 => we compare 13 with 46 no swap [13, 46, 24, 52, 20, 9]. First nested loop done.
# Pass 2 => we compare 24 with 46 swap, then we compare 24 with 13 so no swap [13, 24, 46, 52, 20, 9]. 2nd Nested loop done.
# Pass 3 => we compare 52 with 46 no swap [13, 24, 46, 52, 20, 9]. 3rd....
# Pass 4 => we comapare 20 with 52 swap, comapre 20 with 46 swap, compare 20 with 24 swap, compare 20 with 13 no swap stop. 4th...
# Pass 5 => we compare everything to 9 and it comes and index 0 and everything is shiifted by 1 and array becomes sorted. 5th...

for i in range(0, len(unsorted_array)):
    j = i
    while j > 0 and unsorted_array[j - 1] > unsorted_array[j]:
        unsorted_array[j - 1], unsorted_array[j] = (
            unsorted_array[j],
            unsorted_array[j - 1],
        )
        j -= 1

print(unsorted_array)
