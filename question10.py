# Find smallest odd number from given numbers string

line = input().split()
line = [int(n) for n in line if int(n)%2 != 0]
line.sort()
print(line[0])
