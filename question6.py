"""Goal : The among us imposter is trying to go to the mall for some among us plushies but needs to know if he will make it or not.

Input
Line 1: An integer f the starting fuel in liters
Line 2: An integer d the distance to travel in meters
Line 3: An integer r the rate at which fuel is burned liters per meters

Output
Line 1: An integer a for either the remaining fuel or not enough fuel

Example :
Input :
50
25
1

Output :
25
"""

f = int(input())
d = int(input())
r = int(input())
# formula is total_fuel - (distance * rate)
remaining_fuel = f - (d*r)
if remaining_fuel < 0:
    print("not enough fuel")
else:
    print(remaining_fuel)
