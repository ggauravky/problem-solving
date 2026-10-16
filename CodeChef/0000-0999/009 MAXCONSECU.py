# Chef and Consecutive Ones
# Chef has a binary array 
# n
# u
# m
# s
# nums containing only 
# 0
# 0s and 
# 1
# 1s.
# He wants to find the maximum number of consecutive 
# 1
# 1s in the array regardless of how many such streaks exist. Can you help Chef determine this?

# Function Declaration
# Function Name
# f
# i
# n
# d
# M
# a
# x
# C
# o
# n
# s
# e
# c
# u
# t
# i
# v
# e
# O
# n
# e
# s
# findMaxConsecutiveOnes - This function computes the maximum length of a contiguous segment of 1s in a binary array.

# Parameters
# n
# u
# m
# s
# nums: A binary array of integers where each element is either 0 or 1.
# Return Value
# Returns a single integer representing the maximum number of consecutive 1s in the array.
# Constraints
# 1
# ≤
# N
# ≤
# 10
# 5
# 1≤N≤10 
# 5
 
# n
# u
# m
# s
# [
# i
# ]
# ∈
# 0
# ,
# 1
# nums[i]∈0,1
# Input Format
# The first line contains a single integer 
# N
# N — the size of the array.
# The second line contains 
# N
# N space-separated integers representing the binary array 
# n
# u
# m
# s
# nums.
# Output Format
# Print a single integer — the maximum number of consecutive 1s in the array.

def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    return max_count


n = int(input())
nums = []

values = input().split()

for value in values:
    nums.append(int(value))

print(findMaxConsecutiveOnes(nums))
