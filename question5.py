"""Goal : Your job is to create a program that will output a person's degree, which is listed after their name in the input.

Warning: not all names have a degree. For these names you must output N/A.
Input :
First line: An integer N for how many names will be provided.
Next N lines: A name, optionally containing a comma followed by a degree.

Note : names can contain non-alpha characters such as hyphens -, but a comma , is always followed by a degree.

Note : degrees can contain capital, lowercase letters, spaces and periods.

Output : One line per name containing that person's degree if it exists, N/A otherwise.
Constraints : 0<N<20

Example :

Input : 
2
James Morrison, BAS
Amy Jones

Output : 
BAS
N/A"""

n = int(input())
d = []
for i in range(n):
    name = input()
    if name.count(",")!=0:
        d.append(name.split(",")[1].strip())
    else:
        d.append("N/A")
for i in range(n):
    print(d[i])
