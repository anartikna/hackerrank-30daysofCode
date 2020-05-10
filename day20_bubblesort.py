'''
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}

Task
Given an array, , of size  distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following  lines:

Array is sorted in numSwaps swaps.
where  is the number of swaps that took place.
First Element: firstElement
where  is the first element in the sorted array.
Last Element: lastElement
where  is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Input Format

The first line contains an integer, , denoting the number of elements in array .
The second line contains  space-separated integers describing the respective values of .

'''


#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
temp = 0


for i in range (0,len(a)-1):
    for index in range(0,len(a)-1):
        if(a[index] >a[index+1]):
            temp = a[index]
            a[index] = a[index+1] 
            a[index+1]=temp
            numSwaps+=1


firstElement = a[0]
lastElement = a[len(a)-1]
print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', firstElement)
print('Last Element:', lastElement)

#arr[i], arr[i+1] = arr[i+1], arr[i]
#this is another way to swap without a temp variable