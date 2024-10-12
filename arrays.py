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

#Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell.

# Note: Stock must be bought before being sold.

# Examples:

# Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
# Output: 8
# Explanation: Buy for price 1 and sell for price 9. 


# Input: prices[] = {7, 6, 4, 3, 1} 
# Output: 0
# Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

# Input: prices[] = {1, 3, 6, 9, 11} 
# Output: 10
# Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]

#naive approach
def max_profit(prices):
    n = len(prices)
    res = 0
    
    #explore for all possible ways to buy and sell stock
    for i in range(n - 1):
        for j in range(i + 1, n):
            res = max(res, prices[j] - prices[i])
    return res
if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(max_profit(prices))
                               