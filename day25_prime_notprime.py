'''
Objective
Today we're learning about running time! Check out the Tutorial tab for learning materials and an instructional video!

Task
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it's  or .

Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

Input Format

The first line contains an integer, , the number of test cases.
Each of the  subsequent lines contains an integer, , to be tested for primality.

Constraints

Output Format

For each test case, print whether  is  or  on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import count, islice

n = int(input())
for i in range(n):
    x, prime = int(input()), True
    sq = int(x**0.5)-1
    if x<2: prime = False
    else:
        for num in islice(count(2), sq):
            if not x%num:
                prime = False
    print("Prime") if prime else print("Not prime")