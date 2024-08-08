# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input
# Expected output
# ABC
# DEF
# 02 Test 2
# Input
# Expected output
# CHICK
# HMNHP
# 03 Test 3
# Input
# Expected output
# HELLO
# MJQQT
# 04 Test 4
# Input
# Expected output
# I LOVE FRANCE
# V-Y\cR-S_N[PR

m1 = input()
y = ""
for x in m1:
    n = ord(x) + len(m1)
    y+=chr(n)
print(y)
