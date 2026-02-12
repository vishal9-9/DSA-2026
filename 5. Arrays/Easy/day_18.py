array = [4, 1, 2, 1, 2]

print("Find the number that appears once, and the other numbers twice")


def solution(arr: list):
    hash_ = {}

    for i in arr:
        hash_[i] = hash_.get(i, 0) + 1

    for key, value in hash_.items():
        if value == 1:
            return key


print(solution(arr=array))


array = [10, 5, 2, 7, 1, 9]
sum_is = 15

print()
print("Longest Subarray with given Sum K(Positives)")

# Logic:
# We generate every possible subarray using three loops.
#
# 1st loop (i): selects the starting index.
# 2nd loop (j): selects the ending index.
# 3rd loop (k): calculates the sum of elements from index i to j.
#
# For each subarray (i to j), we compute its total sum.
# If the sum equals the target (sum_is),
# we calculate its length (j - i + 1)
# and update the maximum length found so far.
#
# This is brute force because we recompute the sum
# from scratch for every subarray.
#
# Time Complexity: O(n^3)
# Works correctly for positive numbers.


# O(n ^ 3)
def solution(arr: list):
    longest_index_count = 0

    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            sum_ = 0
            for k in range(i, j + 1):
                sum_ += arr[k]
            if sum_ == sum_is:
                longest_index_count = max(
                    longest_index_count, (j - i) + 1
                )  # as index start from 0 j should be incremented by 1

    return longest_index_count


# Logic:
# We try every possible starting index i.
# For each i, we keep adding elements one by one (j moving forward).
# Instead of recalculating the sum every time, we maintain a running sum.
# If at any point the running sum equals the target (sum_is),
# we calculate the length of that subarray (j - i + 1)
# and update the maximum length found so far.
# This works because all numbers are positive,
# so expanding the subarray by moving j forward increases the sum progressively.
# Time Complexity: O(n^2)


# O(n ^ 2)
def solution(arr: list):
    longest_index_count = 0

    for i in range(0, len(arr)):
        sum_ = 0
        for j in range(i, len(arr)):
            sum_ += arr[j]
            if sum_ == sum_is:
                longest_index_count = max(
                    longest_index_count, (j - i) + 1
                )  # as index start from 0 j should be incremented by 1

    return longest_index_count


# Logic (Prefix Sum + Hashing):
#
# We maintain a running prefix sum while iterating through the array.
# prefix_sum[i] represents the total sum from index 0 to i.
#
# We initialize the hash map with:
# {0: -1} [10, 5, 2, 7] But when the subarray starts at index 0, there is no previous prefix sum stored for “before index 0”.
# This means before the array starts (at imaginary index -1),
# the prefix sum is 0.
# This helps automatically handle subarrays that start from index 0,
# because:
# if current_sum == target,
# then (current_sum - target) = 0,
# and length = i - (-1) = i + 1.
#
# Key idea:
# If (current_sum - target) was seen before at index j,
# then subarray from (j + 1) to i has sum = target.
#
# Because:
# prefix_sum[i] - prefix_sum[j] = target
#
# For every index i:
# 1. Update running sum.
# 2. If (current_sum - target) exists in the dictionary,
#    compute subarray length = i - stored_index.
# 3. Store the prefix sum only if it is seen for the first time
#    (to ensure maximum possible length).
# 4. Keep track of the longest length found.
#
# Time Complexity: O(n)
# Works for both positive and negative numbers.


def solution(arr: list):
    longest_index_count = 0
    sum_hash_ = {0: -1}
    sum_ = 0

    for i in range(0, len(arr)):
        sum_ += arr[i]

        # arr = [1, 2, -2, 3]
        # Prefix sums = [1, 3, 1, 4]
        #
        # Here, prefix sum 1 appears twice (at index 0 and index 2).
        #
        # If we update the hashmap when we see 1 again,
        # its index would change from 0 to 2.
        #
        # That is wrong for finding the LONGEST subarray,
        # because we want the earliest occurrence.
        #
        # Smaller index → larger distance → longer subarray.
        #
        # So we store a prefix sum only the first time we see it,
        # and never overwrite it.

        if sum_ not in sum_hash_:
            sum_hash_[sum_] = i

        if sum_ - sum_is in sum_hash_:
            longest_index_count = max(longest_index_count, (i - sum_hash_.get(sum_ - sum_is)))

    return longest_index_count


print(solution(arr=array))
