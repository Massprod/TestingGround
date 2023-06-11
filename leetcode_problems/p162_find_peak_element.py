# A peak element is an element that is strictly greater than its neighbors.
#   Given a 0-indexed integer array nums, find a peak element, and return its index.
#   If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
#
# You must write an algorithm that runs in O(log n) time.
# ----------------------
# 1 <= nums.length <= 1000  ,  -2 ** 31 <= nums[i] <= 2 ** 31 - 1
# nums[i] != nums[i + 1] for all valid i.


def find_peak_element(nums: list[int]) -> int:
    pass


test1 = [1, 2, 3, 1]
test1_out = 2

test2 = [1, 2, 1, 3, 5, 6, 4]
test2_out = 5
