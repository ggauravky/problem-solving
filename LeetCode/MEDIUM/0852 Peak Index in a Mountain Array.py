# 852. Peak Index in a Mountain Array
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

# Return the index of the peak element.

# Your task is to solve it in O(log(n)) time complexity.

 

# Example 1:

# Input: arr = [0,1,0]

# Output: 1

# Example 2:

# Input: arr = [0,2,1,0]

# Output: 1

# Example 3:

# Input: arr = [0,10,5,2]

# Output: 1



class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
