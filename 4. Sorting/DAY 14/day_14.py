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


unsorted_array = [13, 46, 24, 52, 20, 9]
print()
print("Quick Sort")


def sort_(array: list, low: int, high: int) -> int:
    pivot_value = array[low]  # Store pivot value
    left_pointer = low + 1  # Start just after pivot
    right_pointer = high  # Start from end

    while left_pointer <= right_pointer:

        # Move left_pointer until an element > pivot is found
        while left_pointer <= high and array[left_pointer] <= pivot_value:
            left_pointer += 1

        # Move right_pointer until an element <= pivot is found
        while array[right_pointer] > pivot_value:
            right_pointer -= 1

        # If pointers haven't crossed, swap misplaced elements
        if left_pointer < right_pointer:
            array[left_pointer], array[right_pointer] = (
                array[right_pointer],
                array[left_pointer],
            )
        else:
            break  # Pointers crossed → partitioning complete

    # Place pivot in its correct sorted position
    array[low], array[right_pointer] = array[right_pointer], array[low]

    return right_pointer


def qucik_sort(array: list, low: int, high: int):

    if high <= low:
        return

    partition = sort_(array=array, low=low, high=high)
    qucik_sort(array=array, low=low, high=partition - 1)
    qucik_sort(array=array, low=partition + 1, high=high)


qucik_sort(array=unsorted_array, low=0, high=len(unsorted_array) - 1)
print(unsorted_array)
