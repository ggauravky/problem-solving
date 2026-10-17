# CodeChef Streak
# CodeChef offers a feature called streak count. A streak is maintained if you solve at least one problem daily.

# Om and Addy actively maintain their streaks on CodeChef. Over a span of 
# N
# N consecutive days, you have observed the count of problems solved by each of them.

# Your task is to determine the maximum streak achieved by Om and Addy and find who had the longer maximum streak.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of multiple lines of input.
# The first line of each test case contains an integer 
# N
# N — the number of days.
# The second line of each test case contains 
# N
# N space-separated integers, the 
# i
# t
# h
# i 
# th
#   of which is 
# A
# i
# A 
# i
# ​
#  , representing the problems solved by Om on the 
# i
# t
# h
# i 
# th
#   day.
# The third line of each test case contains 
# N
# N space-separated integers, the 
# i
# t
# h
# i 
# th
#   of which is 
# B
# i
# B 
# i
# ​
#  , representing the problems solved by Addy on the 
# i
# t
# h
# i 
# th
#   day.
# Output Format
# For each test case, output:

# OM, if Om has longer maximum streak than Addy;
# ADDY, if Addy has longer maximum streak than Om;
# DRAW, if both have equal maximum streak.
# You may print each character in uppercase or lowercase. For example, OM, om, Om, and oM, are all considered the same.


t = int(input())

while t > 0:
    n = int(input())
    a = input().split()
    b = input().split()
    t -= 1

    om = 0
    addy = 0
    max_om = 0
    max_addy = 0

    for i in range(n):
        if a[i] != '0':
            om += 1
        else:
            om = 0

        if b[i] != '0':
            addy += 1
        else:
            addy = 0

        if om > max_om:
            max_om = om

        if addy > max_addy:
            max_addy = addy

    if max_om > max_addy:
        print("OM")
    elif max_addy > max_om:
        print("ADDY")
    else:
        print("DRAW")