'''
Objective
Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

Context
Given a 6x6  2D Array, :
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Input Format

There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = [] # a 6x6 2d array holder
    maxsum = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
 #we iterate in (0,4) coz max number of hourglasses could be 4 in any 3 rows
#visualize, a 3 row and 3 column set taht cascades to the right by 1 plac in the inner loop
    #the same set cascades downwards with the outer loop
    for i in range(0, 4):
        for j in range(0, 4):
            hglass_total = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            maxsum.append(hglass_total) #list of all hourglass totals
    print(max(maxsum))
    



