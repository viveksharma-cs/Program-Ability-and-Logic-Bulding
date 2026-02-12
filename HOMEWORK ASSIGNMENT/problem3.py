#  Given an array arr[]. The task is to find the largest element and return it. 
# Examples: 
# Input: arr[] = [1, 8, 7, 56, 90] 
# Output: 90 
# Explanation: The largest element of the given array is 90.
def largest_element(arr):
    max_element = arr[0]
    for x in arr:
        if x > max_element:
            max_element = x
    return max_element
arr = [1, 8, 7, 56, 90]
print(largest_element(arr)) 


