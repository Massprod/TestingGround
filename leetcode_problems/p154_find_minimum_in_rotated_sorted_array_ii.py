# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,4,4,5,6,7] might become:
#       [4,5,6,7,0,1,4] if it was rotated 4 times.
#       [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
#   1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
# You must decrease the overall operation steps as much as possible.
# ----------------------
# n == nums.length  ,  1 <= n <= 5000  ,  -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
# ----------------------
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates.
# Would this affect the runtime complexity? How and why?


def find_min(nums: list[int]) -> int:
    pass


test1 = [1, 3, 5]
test1_out = 1

test2 = [2, 2, 2, 0, 1]
test2_out = 0
