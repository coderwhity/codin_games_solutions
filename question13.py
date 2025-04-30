# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input
# Expected output
# 4
# 1234
# +123
# ++12
# +++1
# 02 Test 2
# Input
# Expected output
# 2
# 12
# +1
# 03 Test 3
# Input
# Expected output
# 1
# 1
# 04 Test 4
# Input
# Expected output
# 3
# 123
# +12
# ++1

n = int(input())
i = n
while i >=1:
    print((n-i)*"+",end='')
    print(''.join([str(j) for j in range(1,i+1)]))
    i-=1
