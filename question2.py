'''You are given a string. You need to calculate how many times each letter appears in the string. You should ignore the case of the letters (i.e., treat "A" and "a" as the same letter). As a result, you should write the counts with a space.
Input : 
Line 1: A string s
Output :
Return a dictionary in the format of {letter number of occurrences}, showing how many times each letter appears.Output must be alphabetical and lowercase.
Constraints :
1 ≤ length of s ≤ 100
Example
Input : 
abcdefg
Output :  
a 1
b 1
c 1
d 1
e 1
f 1
g 1'''

s = input()
k_map ={c.lower():0 for c in s}
for c in s:
    k_map[c.lower()]+=1
for c,val in k_map.items():
    print(f"{c} {val}")
