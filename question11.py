# Given an integer n, print a pattern of stars (*) forming an inverted triangle where the number of stars is n in the first row, and decreases by one in each row until reaching a single star, followed by another pattern of stars forming an upright triangle where the number of stars starts from 1, and increases by one in each row until back to n stars.

# Input
# Line 1: An integer n for the maximum width of the pattern of stars.
# Output
# Lines 1 to n: A pattern of stars forming an inverted triangle.
# Next n lines: A pattern of stars forming an upright triangle.

# Input
# 3
# Output
# ***
# **
# *
# *
# **
# ***


n = int(input())
c = n
f = 1
while c <=n:
    if c == 1:
        print("*\n*")
        f = 0
        c = 2
    else:
        print("*"*c)
        if f==0:
            c+=1
        else:
            c-=1
