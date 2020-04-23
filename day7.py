'''
Objective
Today, we're learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.

Input Format

The first line contains an integer,  (the size of our array).
The second line contains  space-separated integers describing array 's elements.

Constraints

, where  is the  integer in the array.
Output Format

Print the elements of array  in reverse order as a single line of space-separated numbers.
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    temparr = []
    arr = list(map(int, input().rstrip().split()))
    totalelements = len(arr)
    for item in range(0,totalelements):
        temparr.append(arr[totalelements-1])
        totalelements -=1
    for member in range(0,len(temparr)):
      print(temparr[member], end=' ')

      #or

     ''' if __name__ == '__main__':
    n = int(input())
    temparr = []
    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])

    where * is needed to unpack it from the lit form and present the elements
'''
#or
'''
print(' '.join(map(str, *reversed(arr))))
'''

      #print(" ".join(map(str, arr[::-1])))
      '''
      map() function returns a map object(which is an iterator) of the results after           applying the given function to each item of a given iterable (list, tuple etc.)
    ex1:
     # Python program to demonstrate working 
     # of map. 
  
        # Return double of n 
        def addition(n): 
        return n + n 
  
        # We double all numbers using map() 
        numbers = (1, 2, 3, 4) 
        result = map(addition, numbers) 
        print(list(result)) 

    ex2:
            # Double all numbers using map and lambda 
  
            numbers = (1, 2, 3, 4) 
            result = map(lambda x: x + x, numbers) 
            print(list(result))
    ex3
    # List of strings 
        l = ['sat', 'bat', 'cat', 'mat'] 

        # map() can listify the list of strings individually 
        test = list(map(list, l)) 
        print(test) 



      '''
