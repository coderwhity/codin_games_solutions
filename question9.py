'''You must print a string triangle.
Start with the first character of the given string in the first line of output, and grow by one character in each subsequent line until the entire string is printed.
Input
Line 1: A string s
Output
The desired Pattern regarding to s
Constraints 
0 < length of s < 25
Example
Input
12345
Output
1
12
123
1234
12345
'''

s = input()
for x in range(1,len(s)+1):
    print(s[:x])
