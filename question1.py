"""In this puzzle, you will have to build a trivial magic square. In mathematics, a magic square is an array of numbers arranged so that their sums on each row, column, and each diagonal are equal. The value of this sum is called the magic_constant.

Here's is a simple pattern you'll have to follow :

Line 1 : A,1,12,7
Line 2 : 11,8,B,2
Line 3 : 5,10,3,C
Line 4 : 4,D,6,9

All the numbers will remains the same, only the letters will change according to the input :

A = magic_constant-20
B has to be calculated
C has to be calculated
D has to be calculated

Example :

Input
22

Output
2 1 12 7
11 8 1 2
5 10 3 4
4 3 6 9  """

magic_constant = int(input())
print(f"{(magic_constant-(1+12+7))} 1 12 7\n11 8 {magic_constant-(11+8+2)} 2\n5 10 3 {magic_constant-(5+10+3)}\n4 {magic_constant-(4+6+9)} 6 9")
