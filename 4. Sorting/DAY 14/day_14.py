unsorted_array = [13, 46, 24, 52, 20, 9]

print("Bubble Sort Using Recursion")


def bubble_sort(array: list, index: int):
    if (
        index <= 0
    ):  # Base condition index is 0 so all elements till index 1 are sorted making element on 0 index already sorted.
        return

    did_swap = False  # Flag to track if any swap is done if no swaps are done in a pass it means array is sorted and we can stop.

    for i in range(1, index):
        if array[i] <= array[i - 1]:
            array[i - 1], array[i] = array[i], array[i - 1]
            did_swap = True

    if not did_swap:
        return

    bubble_sort(
        array=array, index=index - 1
    )  # We start 2nd Pass to find 2nd biggest element and put it to last.


bubble_sort(array=unsorted_array, index=len(unsorted_array))
print(unsorted_array)

unsorted_array = [13, 46, 24, 52, 20, 9]
print()
print("Insertion Sort Using Recursion")


def insertion_sort(array: list, index: int):
    if index >= len(array):
        return

    index_copy = index + 0
    
    while index > 0 and array[index] <= array[index - 1]:
        array[index], array[index - 1] = array[index - 1], array[index]
        index -= 1

    insertion_sort(array=array, index=index_copy + 1)


insertion_sort(array=unsorted_array, index=1)
print(unsorted_array)
