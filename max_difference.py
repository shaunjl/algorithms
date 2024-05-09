"""
Problem:
Find Maximum difference between two elements such that larger element appears after the smaller number
Assume that there are at least two elements in array. 
Return a negative value if the array is sorted in decreasing order.
Return 0 if elements are equal

Solution:
Set the min element as the first in the list
for each (starting from second):
 - calculate the diff between the lowest and current element, set max diff to lowest(current diff, previous highest diff)
 - reset lowest if current is lower than the previous lowest
"""
def forward_max_diff(arr: list[int]) -> int: 
    max_diff = arr[1] - arr[0]  # initialize to the diff between the first two elements
    min_element = arr[0] # first element is by default the lowest (and highest)
    
    for i in range(1, len(arr)): 
        if (arr[i] - min_element > max_diff): 
            max_diff = arr[i] - min_element 
    
        if (arr[i] < min_element): 
            min_element = arr[i] 
    return max_diff 
    
# Driver program to test above function 
arr = [10, -2, 6, 80, 100]
print("Maximum difference is", forward_max_diff(arr)) 
