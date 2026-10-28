# Compress the Video
# Chef recorded a video explaining his favorite recipe. However, the size of the video is too large to upload on the internet. He wants to compress the video so that it has the minimum size possible.

# Chef's video has 
# N
# N frames initially. The value of the 
# i
# t
# h
# i 
# th
#   frame is 
# A
# i
# A 
# i
# ​
#  . Chef can do the following type of operation any number of times:

# Choose an index 
# i
# i 
# (
# 1
# ≤
# i
# ≤
# N
# )
# (1≤i≤N) such that the value of the 
# i
# t
# h
# i 
# th
#   frame is equal to the value of either of its neighbors and remove the 
# i
# t
# h
# i 
# th
#   frame.
# Find the minimum number of frames Chef can achieve.

# Input Format
# First line will contain 
# T
# T, the number of test cases. Then the test cases follow.
# The first line of each test case contains a single integer 
# N
# N - the number of frames initially.
# The second line contains 
# N
# N space-separated integers, 
# A
# 1
# ,
# A
# 2
# ,
# …
# ,
# A
# N
# A 
# 1
# ​
#  ,A 
# 2
# ​
#  ,…,A 
# N
# ​
#   - the values of the frames.


# cook your dish here

t = int(input())

for _ in range(t):
    n = int(input())
    a = input().split()

    count = 1

    for i in range(1, n):
        if a[i] != a[i - 1]:
            count += 1

    print(count)
