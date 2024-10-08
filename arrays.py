#Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target. This problem is a variation of 2Sum problem.

#Examples: 

#Input: arr[] = {0, -1, 2, -3, 1}, target = -2
#Output: True
#Explanation: If we calculate the sum of the output,1 + (-3) = -2


#Input: arr[] = {1, -2, 1, 0, 5}, target = 0
#Output: False


##naive approach
def two_sum(arr, target):
    n = len(arr)
    
    #itterate through each element in the array
    for i in range(n):
        # For each element arr[i], check every
        # other element arr[j] that comes after it
        for j in range(i + 1, n):
            # Check if the sum of the current pair
            # equals the target
            if arr[i] + arr[j] == target:
                return True
    # If no pair is found after checking
    # all possibilities
    return False

arr = [0, -1, 2, -3, 1]
target = -2

# Call the two_sum function and print the result
if two_sum(arr, target):
    print("true")
else:
    print("false") 

#better approach
def binary_search(arr, right, target):#function to perform binary search
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

#Function to check whether any pair exists whos sum is equal to the given value
def two_sum(arr, target):
    #sort array
    arr.sort()
    
    #iterate through each element in the array
    for i in range(len(arr)):
        complete = target - arr[i]
        
        #use binary search to find the complement
        if binary_search(arr, i + 1, len(arr) - 1 , complement):
            return True
    return False

arr = [0, -1, 2, -3, 1]
target = -2                              