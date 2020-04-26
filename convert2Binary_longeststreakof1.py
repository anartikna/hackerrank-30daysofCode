#!/bin/python3

import math
import os
import random
import re
import sys

    #return bin(n).replace("0b", "") another way
def DecimalToBinary(num): 
    binrep = None
    elements = []
    alllen = []
    streak = 0
    #print(bin)
    binrep = bin(n)[2:] #format is 0bxxxx e.g. 0b1010
    elements = binrep.strip('0').split('0')
    #print(elements)
    for item in elements:
      alllen.append(len(item))
    streak = max(alllen)
    print(streak)

if __name__ == '__main__':
    n = int(input())
    DecimalToBinary(n)
