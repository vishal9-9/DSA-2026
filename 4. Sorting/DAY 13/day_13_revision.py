unsorted_array = [13, 46, 24, 52, 20, 9]

print("Merge Sort")

# Mege sort uses Divide & Conquer Technique.
# array = [3,2,1]
# So we start by divison (start_array_index + end_array_index) // 2
# 1st Iteration it will be [3,2] & other [1] as we will be using recursion and condition of left is placed first so it will process whole left side first.
# 2nd Iteration [3], [2] this is the base condition for recusrion (start_index <= end_index) once base condition hits then we start merge.
# For merging we will place 2 pointers on 1st array start(start index) and 2nd array start(middle index + 1), we use while loop and start comparing element at both index and add it to a temp array and increase the ponter of element which was small so here temp = [2] and as right pointer cannot move forward as only 1 element(right pointer <= end_index).
# We the add another while loop as left array still has element and right is over add all elements of left array to temp. Same we need to do for right pointer as some time left array can be get exhausted before right array. after that we get temp = [2,3].
# As Temp is now sorted we need to replace it in original array within range of start and end index as we have sorted those elements.
# so we use for loop in range of start, end_index + 1 as we need to include end index as well. start_index should be repalced with first element of array and so on till we reach the end.


def merge_sort(array: list, start_index: int, end_index: int):

    def merge(array: list, start_index: int, middle_index: int, end_index: int):
        temp = []
        left_pointer = start_index
        right_pointer = middle_index + 1

        # Loop until there are elements in both left and right array
        while left_pointer <= middle_index and right_pointer <= end_index:
            if array[left_pointer] <= array[right_pointer]:
                temp.append(array[left_pointer])
                left_pointer += 1
            else:
                temp.append(array[right_pointer])
                right_pointer += 1

        # Backup if left pointer (array) has elements & right is exhausted
        while left_pointer <= middle_index:
            temp.append(array[left_pointer])
            left_pointer += 1

        # Backup if right pointer (array) has elements & left is exhausted
        while right_pointer <= end_index:
            temp.append(array[right_pointer])
            right_pointer += 1

        for i in range(start_index, end_index + 1):
            array[i] = temp[i - start_index]

    if start_index >= end_index:
        return

    # Finding mid to divide array in left & right groups.
    middle_index = (start_index + end_index) // 2

    # Left Group
    merge_sort(array=array, start_index=start_index, end_index=middle_index)

    # Right Group
    merge_sort(array=array, start_index=middle_index + 1, end_index=end_index)

    # Merge the Left & Right Group
    merge(
        array=array,
        start_index=start_index,
        middle_index=middle_index,
        end_index=end_index,
    )


merge_sort(array=unsorted_array, start_index=0, end_index=len(unsorted_array) - 1)
print(unsorted_array)
