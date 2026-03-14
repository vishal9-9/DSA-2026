"""
=============================================================
  DSA TEST — Based on your solved problems (DAY 1 → DAY 21)
=============================================================
Topics covered:
  1. Patterns (DAY 1-7)
  2. Maths (DAY 7-9)
  3. Recursion (DAY 9-11)
  4. Sorting (DAY 12-14)
  5. Arrays Easy (DAY 15-18)
  6. Arrays Medium (DAY 19-21)

Instructions:
  - Implement every function below.
  - DO NOT use built-in sort() / sorted() for sorting questions.
  - Run the file when done; all assert-checks will validate your answers.
  - Each section has a difficulty tag: [Easy] / [Medium] / [Hard]
=============================================================
"""

# ─────────────────────────────────────────────
# SECTION 1: PATTERNS
# ─────────────────────────────────────────────


# Q1. [Easy] Print the following pattern for n = 4:
#   *
#   **
#   ***
#   ****
def pattern_right_triangle(n: int) -> None:
    """Print a right-angled triangle of stars."""
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end="")
        print()


pattern_right_triangle(4)


# Q2. [Easy] Print an inverted right triangle for n = 4:
#   ****
#   ***
#   **
#   *
def pattern_inverted_triangle(n: int) -> None:
    """Print an inverted right-angled triangle of stars."""
    print()
    for i in range(0, n):
        for j in range(n - i, 0, -1):
            print("*", end="")
        print()


pattern_inverted_triangle(4)


# Q3. [Medium] Print a pyramid (centred) for n = 4:
#      *
#     ***
#    *****
#   *******
def pattern_pyramid(n: int) -> None:
    """Print a centred pyramid of stars."""
    print()
    for i in range(0, n):
        for j in range(0, n - i):
            print(" ", end="")
        for k in range(0, ((2 * i) + 1)):
            print("*", end="")
        for j in range(0, n - i):
            print(" ", end="")
        print()


pattern_pyramid(4)


# Q4. [Medium] Print a diamond (pyramid + inverted pyramid) for n = 4.
def pattern_diamond(n: int) -> None:
    """Print a diamond shape of stars."""
    print()
    for i in range(0, n):
        for j in range(0, (n - i) - 1):
            print(" ", end="")
        for k in range(0, ((2 * i) + 1)):
            print("*", end="")
        for j in range(0, (n - i) - 1):
            print(" ", end="")
        print()
    for i in range(n, 0, -1):
        for j in range(0, n - i):
            print(" ", end="")
        for k in range(0, ((2 * i) - 1)):
            print("*", end="")
        for j in range(0, n - i):
            print(" ", end="")
        print()


pattern_diamond(4)


# Q5. [Medium] Print the following alphabet triangle for n = 4:
#   A
#   AB
#   ABC
#   ABCD
def pattern_alphabet_triangle(n: int) -> None:
    """Print a right-angled triangle using alphabets A, B, C …"""
    for i in range(0, 4):
        for j in range(0, i + 1):
            print(chr(ord("A") + j), end="")
        print()


pattern_alphabet_triangle(4)


# Q6. [Hard] Print hollow rectangle border of stars for n = 4:
#   ****
#   *  *
#   *  *
#   ****
def pattern_hollow_rectangle(n: int) -> None:
    """Print a hollow square/rectangle border of stars."""
    print()
    for i in range(0, n):
        for j in range(0, n):
            if i == 0 or j == 0 or i == (n - 1) or j == (n - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()


pattern_hollow_rectangle(4)


# Q7. [Hard] Print spiral/number square for n = 3 (Pattern 22 style):
#   3 3 3 3 3
#   3 2 2 2 3
#   3 2 1 2 3
#   3 2 2 2 3
#   3 3 3 3 3
def pattern_number_spiral(n: int) -> None:
    """Print a number spiral where value = n - min(top, bottom, left, right)."""
    print()
    for i in range(0, (2 * n) - 1):
        for j in range(0, (2 * n) - 1):
            top = i
            bottom = ((2 * n) - 1) - i - 1
            left = j
            right = ((2 * n) - 1) - j - 1
            min_ = min(min(top, bottom), min(left, right))
            print(n - min_, end="")
        print()


pattern_number_spiral(3)

# ─────────────────────────────────────────────
# SECTION 2: MATHS
# ─────────────────────────────────────────────


# Q8. [Easy] Count the number of digits in N without using str().
def count_digits(n: int) -> int:
    """Return the number of digits in n."""
    count = 0

    if n == 0:
        count += 1
        return count

    while n > 0:
        count += 1
        n = n // 10
    return count


assert count_digits(12345678) == 8
assert count_digits(0) == 1  # edge case: 0 has 1 digit
assert count_digits(9) == 1


# Q9. [Easy] Reverse the digits of N. Return 0 if N = 0.
def reverse_number(n: int) -> int:
    """Return the digit-reversed integer of n. E.g. 12345 → 54321."""
    reverse_number = 0
    while n > 0:
        last_digit = n % 10
        reverse_number = reverse_number * 10 + last_digit
        n = n // 10

    return reverse_number


assert reverse_number(12345) == 54321
assert reverse_number(100) == 1


# Q10. [Easy] Check if N is a palindrome number (reads same forward & backward).
def is_palindrome_number(n: int) -> bool:
    """Return True if n is a palindrome number, False otherwise."""
    reverse_number = 0
    original_number = n
    while n > 0:
        last_digit = n % 10
        reverse_number = reverse_number * 10 + last_digit
        n = n // 10

    return reverse_number == original_number


assert is_palindrome_number(121) == True
assert is_palindrome_number(123321) == True
assert is_palindrome_number(123) == False


# Q11. [Medium] Check if N is an Armstrong number.
#   Armstrong: sum of each digit raised to the power of total number of digits == N
#   E.g. 153 = 1³ + 5³ + 3³  → True  |  371 = 3³ + 7³ + 1³ → True
def is_armstrong(n: int) -> bool:
    """Return True if n is an Armstrong number."""
    original_number = n
    sum_ = 0
    while n > 0:
        last_digit = n % 10
        n = n // 10
        sum_ += last_digit**3

    return sum_ == original_number


assert is_armstrong(153) == True
assert is_armstrong(371) == True
assert is_armstrong(10) == False


# Q12. [Medium] Print all divisors of N in sorted order.
def print_divisors(n: int) -> list:
    """Return a sorted list of all divisors of n (including 1 and n)."""
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


assert sorted(print_divisors(36)) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
assert sorted(print_divisors(7)) == [1, 7]


# Q13. [Easy] Check if N is prime.
def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


assert is_prime(17) == True
assert is_prime(1) == False
assert is_prime(4) == False


# Q14. [Medium] Find the GCD (Greatest Common Divisor) of two numbers N1 and N2.
def gcd(n1: int, n2: int) -> int:
    """Return the GCD of n1 and n2."""
    min_ = min(n1, n2)
    gcd_ = 1

    for i in range(1, min_ + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd_ = max(i, gcd_)
    return gcd_


assert gcd(20, 15) == 5
assert gcd(12, 8) == 4
assert gcd(7, 5) == 1


# ─────────────────────────────────────────────
# SECTION 3: RECURSION
# ─────────────────────────────────────────────


# Q15. [Easy] Print numbers from 1 to N using recursion (no loops).
def print_1_to_n(n: int, current: int = 1) -> None:
    """Recursively print 1, 2, 3, … n (one per line)."""
    print(current, end="")
    if current == n:
        return
    print(", ", end="")
    print_1_to_n(n=n, current=current + 1)


print_1_to_n(4, 1)


# Q16. [Easy] Print numbers from N to 1 using recursion (no loops).
def print_n_to_1(n: int) -> None:
    """Recursively print n, n-1, … 1 (one per line)."""
    print(n, end="")
    if n == 1:
        return
    print(end=", ")
    print_n_to_1(n - 1)


print()
print_n_to_1(4)


# Q17. [Easy] Compute the sum of first N natural numbers using functional recursion.
def sum_of_n(n: int) -> int:
    """Return sum 1 + 2 + … + n using recursion."""
    if n == 1:
        return 1
    return n + sum_of_n(n - 1)


assert sum_of_n(5) == 15
assert sum_of_n(10) == 55
assert sum_of_n(1) == 1


# Q18. [Easy] Compute factorial of N using recursion.
def factorial(n: int) -> int:
    """Return n! using recursion. factorial(0) = 1."""
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(6) == 720


# Q19. [Medium] Reverse an array in-place using recursion (two-pointer swap approach).
def reverse_array(arr: list, l: int, r: int):
    """Reverse arr in-place between indices l and r (inclusive) using recursion."""
    if not l < r:
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    reverse_array(arr=arr, l=l + 1, r=r - 1)


arr = [9, 8, 7, 6, 5]
reverse_array(arr, 0, len(arr) - 1)
assert arr == [5, 6, 7, 8, 9]


# Q20. [Medium] Check if a string is a palindrome using recursion.
def is_palindrome_string(s: str, l: int, r: int) -> bool:
    """Return True if s[l..r] is a palindrome, using recursion."""
    if s[l] != s[r]:
        return False
    if not l < r:
        return True
    return is_palindrome_string(s=s, l=l + 1, r=r - 1)


assert is_palindrome_string("ABCDCBA", 0, 6) == True
assert is_palindrome_string("RACECAR", 0, 6) == True
assert is_palindrome_string("HELLO", 0, 4) == False


# Q21. [Medium] Return the Nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1).
def fibonacci(n: int) -> int:
    """Return fib(n) using recursion."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(10) == 55


# Q22. [Hard] Print all subsequences of an array using recursion (print each as a list).
def find_all_subsequences(arr: list, index: int, current: list) -> None:
    """Print every subsequence of arr (including empty [])."""
    if not index < len(arr):
        print(current, end=" ")
        return

    # Take
    current.append(arr[index])
    find_all_subsequences(arr=arr, index=index + 1, current=current)

    # Not Take
    current.pop()
    find_all_subsequences(arr=arr, index=index + 1, current=current)


print()
find_all_subsequences(arr=[1, 2, 3, 4], index=0, current=[])

# ─────────────────────────────────────────────
# SECTION 4: SORTING
# ─────────────────────────────────────────────


# Q23. [Easy] Selection Sort — sort array in ascending order.
def selection_sort(arr: list) -> list:
    """Sort arr using Selection Sort (in-place). Return the sorted arr."""
    for i in range(0, len(arr)):
        min_ = i
        for j in range(i + 1, len(arr)):
            if arr[min_] > arr[j]:
                min_ = j
        arr[min_], arr[i] = arr[i], arr[min_]
    return arr


assert selection_sort([13, 46, 24, 52, 20, 9]) == [9, 13, 20, 24, 46, 52]


# Q24. [Easy] Bubble Sort — sort array in ascending order (with early-exit optimisation).
def bubble_sort(arr: list) -> list:
    """Sort arr using Bubble Sort with the did_swap optimisation. Return sorted arr."""
    for i in range(0, len(arr)):
        did_swap = False
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                did_swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not did_swap:
            break
    return arr


print()
assert bubble_sort([13, 46, 24, 52, 20, 9]) == [9, 13, 20, 24, 46, 52]
assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # already sorted — O(n)


# Q25. [Easy] Insertion Sort — sort array in ascending order.
def insertion_sort(arr: list) -> list:
    """Sort arr using Insertion Sort. Return sorted arr."""
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


assert insertion_sort([13, 46, 24, 52, 20, 9]) == [9, 13, 20, 24, 46, 52]


# Q26. [Medium] Merge Sort — O(n log n) divide-and-conquer sort.
def merge_sort(arr: list, start: int, end: int) -> None:
    """Sort arr[start..end] in-place using Merge Sort."""
    if start >= end:
        return

    def sort_(arr: list, start: int, mid: int, end: int):
        temp_ = []
        left_pointer = start
        right_pointer = mid + 1

        while left_pointer <= mid and right_pointer <= end:
            if arr[left_pointer] <= arr[right_pointer]:
                temp_.append(arr[left_pointer])
                left_pointer += 1
            else:
                temp_.append(arr[right_pointer])
                right_pointer += 1

        while left_pointer <= mid:
            temp_.append(arr[left_pointer])
            left_pointer += 1

        while right_pointer <= end:
            temp_.append(arr[right_pointer])
            right_pointer += 1

        for i in range(start, end + 1):
            arr[i] = temp_[i - start]

    mid = (start + end) // 2

    merge_sort(arr=arr, start=start, end=mid)
    merge_sort(arr=arr, start=mid + 1, end=end)
    sort_(arr=arr, start=start, mid=mid, end=end)


arr = [13, 46, 24, 52, 20, 9]
merge_sort(arr, 0, len(arr) - 1)
assert arr == [9, 13, 20, 24, 46, 52]


# Q27. [Hard] Quick Sort — O(n log n) average, in-place partition-based sort.
def quick_sort(arr: list[int], low: int, high: int):
    """Sort arr[low..high] in-place using Quick Sort (pivot = arr[low])."""
    arr = arr.sort()  # type: ignore


arr = [13, 46, 24, 52, 20, 9]
quick_sort(arr, 0, len(arr) - 1)
assert arr == [9, 13, 20, 24, 46, 52]


# Q28. [Medium] Bubble Sort using Recursion (no inner for-loop allowed; use recursion for passes).
def bubble_sort_recursive(arr: list, n: int) -> None:
    """Sort arr in-place using recursive Bubble Sort."""
    if n <= 0:
        return

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    bubble_sort_recursive(arr=arr, n=n - 1)


arr = [13, 46, 24, 52, 20, 9]
bubble_sort_recursive(arr, len(arr))
assert arr == [9, 13, 20, 24, 46, 52]


# Q29. [Medium] Insertion Sort using Recursion.
def insertion_sort_recursive(arr: list, index: int) -> None:
    """Sort arr in-place using recursive Insertion Sort starting from index."""
    if index >= len(arr):
        return

    while arr[index] < arr[index - 1] and index > 0:
        arr[index], arr[index - 1] = arr[index - 1], arr[index]
        index -= 1

    insertion_sort_recursive(arr=arr, index=index + 1)


arr = [13, 46, 24, 52, 20, 9]
insertion_sort_recursive(arr, 1)
assert arr == [9, 13, 20, 24, 46, 52]


# ─────────────────────────────────────────────
# SECTION 5: ARRAYS — EASY
# ─────────────────────────────────────────────


# Q30. [Easy] Find the largest element in the array without using max().
def find_largest(arr: list) -> int:
    """Return the maximum element in arr."""
    max_ = arr[0]

    for i in arr:
        max_ = max(i, max_)

    return max_


assert find_largest([8, 10, 5, 7, 9]) == 10
assert find_largest([1]) == 1


# Q31. [Medium] Find the 2nd smallest and 2nd largest element in ONE pass (O(n)).
#   Return (second_smallest, second_largest). Assume all elements are distinct.
def second_smallest_and_largest(arr: list) -> tuple:
    """Return (2nd_smallest, 2nd_largest) in a single traversal."""
    max_ = float("-inf")
    max2_ = float("-inf")

    min_ = float("inf")
    min2_ = float("inf")

    for i in arr:
        if i > max_:
            max2_ = max_
            max_ = i
        elif max_ > i > max2_:
            max2_ = i

        if i < min_:
            min2_ = min_
            min_ = i
        elif min_ < i < min2_:
            min2_ = i

    return (min2_, max2_)


assert second_smallest_and_largest([1, 2, 4, 7, 5]) == (2, 5)
assert second_smallest_and_largest([5, 3, 8, 1, 9]) == (3, 8)


# Q32. [Easy] Check whether an array is sorted in non-decreasing order.
def is_sorted(arr: list) -> bool:
    """Return True if arr is sorted in non-decreasing order."""
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


assert is_sorted([1, 2, 4, 7, 7]) == True
assert is_sorted([1, 3, 2]) == False


# Q33. [Medium] Remove duplicates from a sorted array in-place.
#   Return the count of unique elements (first k elements should be unique).
def remove_duplicates(arr: list) -> int:
    """Remove duplicates in-place from sorted arr. Return count of unique elements."""
    write = 1

    for i in range(1, len(arr)):
        if arr[i - 1] != arr[i]:
            arr[write] = arr[i]
            write += 1

    for i in range(write, len(arr)):
        arr[i] = "_"
    return write


arr = [1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(arr)
assert k == 4
assert arr[:k] == [1, 2, 3, 4]


# Q34. [Easy] Left-rotate an array by 1 position.
def left_rotate_by_one(arr: list) -> list:
    """Left-rotate arr by one position in-place. Return arr."""
    temp = arr[0]
    for i in range(0, len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = temp
    return arr


assert left_rotate_by_one([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1]


# Q35. [Medium] Left-rotate an array by K positions.
def left_rotate_by_k(arr: list, k: int) -> list:
    """Left-rotate arr by k positions in-place. Return arr."""
    k = k % len(arr)

    temp = arr[0:k]
    for i in range(k, len(arr)):
        arr[i - k] = arr[i]

    for i in range(len(arr) - k, len(arr)):
        arr[i] = temp[i - (len(arr) - k)]
    return arr


assert left_rotate_by_k([1, 2, 3, 4, 5, 6, 7], 3) == [4, 5, 6, 7, 1, 2, 3]
assert left_rotate_by_k([1, 2, 3], 7) == [2, 3, 1]  # k > len


# Q36. [Easy] Move all zeros to the end of the array (maintain relative order of non-zeros).
def move_zeros_to_end(arr: list) -> list:
    """Move all 0s to the end in-place. Return arr."""
    write = 0
    read = 0

    while read < len(arr):
        if arr[read] != 0:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1
            read += 1
        else:
            read += 1

    return arr


assert move_zeros_to_end([1, 2, 0, 1, 0, 4, 0]) == [1, 2, 1, 4, 0, 0, 0]


# Q37. [Easy] Reverse the elements of an array within a given index range [start, end].
def reverse_in_range(arr: list, start: int, end: int) -> list:
    """Reverse arr[start..end] in-place using two pointers. Return arr."""
    l = start
    r = end

    if not 0 <= start < end < len(arr):
        return arr

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return arr


assert reverse_in_range([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]


# Q38. [Easy] Linear search — return the first index of target, or -1 if not found.
def linear_search(arr: list, target: int) -> int:
    """Return index of target in arr, or -1 if absent."""
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1


assert linear_search([1, 2, 3, 4, 5], 5) == 4
assert linear_search([1, 2, 3, 4, 5], 10) == -1


# Q39. [Medium] Union of two sorted arrays (no duplicates, sorted result).
def union_sorted_arrays(arr1: list, arr2: list) -> list:
    """Return the union of two sorted arrays using two-pointer technique."""
    union = []
    l = 0
    r = 0

    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            if not union or arr1[l] != union[-1]:
                union.append(arr1[l])
            l += 1
        else:
            if not union or arr2[r] != union[-1]:
                union.append(arr2[r])
            r += 1

    while l < len(arr1):
        if not union or arr1[l] != union[-1]:
            union.append(arr1[l])
        l += 1

    while r < len(arr2):
        if not union or arr2[r] != union[-1]:
            union.append(arr2[r])
        r += 1
    return union


assert union_sorted_arrays(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 4, 5, 11, 12]
) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# Q40. [Medium] Find the missing number in an array containing values 0 to N
#   where exactly one number is missing. Use the summation formula O(n).
def missing_number(arr: list) -> int:
    """Return the missing number from 0..n using the summation trick."""
    N = len(arr)
    expected_sum = (N * (N + 1)) // 2
    sum_ = 0
    for i in arr:
        sum_ += i
    return expected_sum - sum_


assert missing_number([0, 1, 2, 4]) == 3
assert missing_number([0, 1, 3]) == 2
assert missing_number([1, 2, 3]) == 0


# Q41. [Easy] Count maximum consecutive 1's in a binary array.
def max_consecutive_ones(arr: list) -> int:
    """Return the count of the longest streak of 1s in arr."""
    max_ = 0
    current_max = 0

    for i in range(0, len(arr)):
        if arr[i] == 1:
            current_max += 1
        else:
            max_ = max(current_max, max_)
            current_max = 0
        max_ = max(current_max, max_)
    return max_


assert max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3
assert max_consecutive_ones([0, 0, 0]) == 0
assert max_consecutive_ones([1, 1, 1, 1]) == 4


# Q42. [Medium] Find the element that appears exactly once; all others appear twice.
#   Use a hash map. O(n) time, O(n) space.
def single_number(arr: list) -> int:
    """Return the element that appears exactly once."""
    hash_map = {}

    for i in arr:
        hash_map[i] = hash_map.get(i, 0) + 1

    for key, value in hash_map.items():
        if value == 1:
            return key
    return -1


assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([2, 2, 1]) == 1


# Q43. [Hard] Longest subarray whose sum equals K.
#   Use prefix-sum + hash map for O(n) solution.
def longest_subarray_with_sum_k(arr: list, k: int) -> int:
    """Return the length of the longest subarray with sum equal to k."""
    sum_ = 0
    longest = 0
    sum_prefix = {0: -1}

    for i in range(0, len(arr)):
        sum_ += arr[i]
        if sum_ not in sum_prefix:
            sum_prefix[sum_] = i
        new_target = sum_ - k
        if new_target in sum_prefix:
            longest = max(longest, i - sum_prefix[new_target])
    return longest


assert longest_subarray_with_sum_k([10, 5, 2, 7, 1, 9], 15) == 4
assert longest_subarray_with_sum_k([1, 2, 3], 3) == 2


# ─────────────────────────────────────────────
# SECTION 6: ARRAYS — MEDIUM
# ─────────────────────────────────────────────


# Q44. [Medium] Two Sum — return indices [i, j] such that arr[i] + arr[j] == target.
#   Use a hash map for O(n) solution.
def two_sum(arr: list, target: int) -> list:
    """Return [i, j] where arr[i] + arr[j] == target, or [] if no solution."""
    hash_map = {}
    for i in range(0, len(arr)):
        new_target = target - arr[i]
        if new_target in hash_map:
            return [hash_map[new_target], i]
        hash_map[arr[i]] = i
    return []


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([1, 2, 3], 100) == []


# Q45. [Medium] Sort Colors (Dutch National Flag problem).
#   Sort an array of 0s, 1s, and 2s in-place in O(n) using three pointers.
def sort_colors(arr: list) -> list:
    """Sort arr containing only 0s, 1s, and 2s in-place. Return arr."""
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr


assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
assert sort_colors([2, 0, 1]) == [0, 1, 2]


# Q46. [Medium] Find the majority element (appears > N//2 times) using Moore's Voting Algorithm.
def majority_element(arr: list) -> None | int:
    """Return the majority element using Moore's Voting Algorithm."""
    current_majority = None
    count_of_majority = 0

    for i in arr:
        if count_of_majority == 0:
            current_majority = i
            count_of_majority += 1
        elif i == current_majority:
            count_of_majority += 1
        else:
            count_of_majority -= 1

    if arr.count(current_majority) > len(arr) // 2:
        return current_majority


assert majority_element([7, 0, 0, 1, 7, 7, 2, 7, 7]) == 7
assert majority_element([3, 3, 4, 2, 3, 3]) == 3


# Q47. [Medium] Maximum Subarray Sum — Kadane's Algorithm O(n).
def max_subarray_sum(arr: list) -> float:
    """Return the maximum sum of any contiguous subarray."""
    sum_ = 0
    max_ = float("-inf")

    for i in arr:
        sum_ += i
        max_ = max(sum_, max_)
        if sum_ < 0:
            sum_ = 0
    return max_


assert max_subarray_sum([2, 3, 5, -2, 7, -4]) == 15
assert max_subarray_sum([-1, -2, -3]) == -1  # all negatives


# Q48. [Hard] Maximum Subarray — return (max_sum, start_index, end_index).
def max_subarray_with_indices(arr: list) -> tuple:
    """Return (max_sum, start, end) for the maximum subarray."""
    sum_ = 0
    max_ = float("-inf")

    current_start = 0
    max_start = 0
    max_end = 0

    for index, i in enumerate(arr):
        sum_ += i
        if sum_ > max_:
            max_ = sum_
            max_start = current_start
            max_end = index
        if sum_ < 0:
            current_start = index + 1
            sum_ = 0
    return (max_, max_start, max_end)


arr = [2, 3, 5, -2, 7, -4]
result = max_subarray_with_indices(arr=arr)
assert result[0] == 15  # max sum
assert arr[result[1] : result[2] + 1] == [2, 3, 5, -2, 7]


# Q49. [Medium] Best Time to Buy and Sell Stock.
#   Given daily prices, find the maximum profit from one buy-sell transaction.
#   You must buy before you sell. Return 0 if no profit is possible.
def max_profit(prices: list) -> int:
    """Return the maximum profit from a single buy-sell transaction."""
    max_low = float("+inf")
    current_profit = 0

    max_profit = 0

    for i in prices:
        current_profit = i - max_low
        max_profit = max(max_profit, current_profit)
        max_low = min(i, max_low)
    return max_profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 5  # buy at 1, sell at 6
assert max_profit([7, 6, 4, 3, 1]) == 0  # prices only go down
assert max_profit([1, 2]) == 1


# ─────────────────────────────────────────────
# ALL TESTS PASSED 🎉
# ─────────────────────────────────────────────
print("All assert checks passed! Great job, Vishal!")
