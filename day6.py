'''Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.

Input Format

The first line contains an integer,  (the number of test cases).
Each line  of the  subsequent lines contain a String, .

Constraints

Output Format

For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.'''


import math
import os
import random
import re
import sys
#from str import join

if __name__ == '__main__':
    allstr = []
    #oddlist = []
    #evenlist = []
    #strcount = 0
    templen = 0
    n = int(input())
    for i in range(n):
        allstr.append(str(input()))
    
    #strcount = len(allstr)
    for j in range(n):
      templen = len(allstr[j])
      oddlist = []
      evenlist = []
      for k in range(templen):
        if k==0 or k%2==0:
          evenlist.append(allstr[j][k].strip()) 
        else:
          oddlist.append(allstr[j][k].strip())
      s1=("".join(evenlist))
      s2=("".join(oddlist))
      print(s1, s2)

