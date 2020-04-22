
'''
Objective
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

Task
Given an integer,n , print its first 10 multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.

Input Format

A single integer, .

Constraints

Output Format

Print  10 lines of output; each line  (where ) contains the  of  in the form:
n x i = result.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    i = 1
    for i in range(1,11):
        print(n,"x", i, "=", (n*i))

