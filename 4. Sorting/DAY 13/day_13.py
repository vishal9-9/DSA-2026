unsorted_array = [13, 46, 24, 52, 20, 9]

print("Merge Sort")

# Divide & Merge


def merge_sort(array: list, start_index: int, end_index: int):

    def merge(array: list, start_index: int, middle_index: int, end_index: int):
        temp = []
        
        left_pointer = start_index
        right_pointer = middle_index + 1
        
        while left_pointer <= middle_index and right_pointer <= end_index:
            if array[left_pointer] <= array[right_pointer]:
                temp.append(array[left_pointer])
                left_pointer += 1
            else:
                temp.append(array[right_pointer])
                right_pointer += 1

        while left_pointer <= middle_index:
            temp.append(array[left_pointer])
            left_pointer += 1
        
        while right_pointer <= end_index:
            temp.append(array[right_pointer])
            right_pointer += 1

        for i in range(start_index, end_index + 1):
            array[i] = temp[i - start_index]


    if start_index >= end_index:
        return

    middle_index = (start_index + end_index) // 2

    merge_sort(array=array, start_index=start_index, end_index=middle_index)
    merge_sort(
        array=array, start_index=(middle_index + 1), end_index=end_index
    )

    merge(
        array=array,
        start_index=start_index,
        middle_index=middle_index,
        end_index=end_index,
    )


merge_sort(array=unsorted_array, start_index=0, end_index=len(unsorted_array) - 1)

print(unsorted_array)
