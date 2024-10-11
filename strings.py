#Given a string s, find the length of the longest substring without repeating characters. 

#Examples:

#Input: “ABCBC”
#Output: 3
#Explanation: The longest substring without repeating characters is “ABC”

#Input: “AAA”
#Output: 1
#Explanation: The longest substring without repeating characters is “A”

#Input: “GEEKSFORGEEKS”
#Output: 7 
#Explanation: The longest substrings without repeating characters are “EKSFORG” and “KSFORGE”, with lengths of 7.

#naive approach
def longestUniqueSubstr(s):
    n = len(s)
    res = 0
    
    for i in range(n):
        #if current chaaracter is visited break the loop
        if visited[ord(s[j])] == True:
            break
        #else update the result if this window is larger, and mark current character as visited
        else:
            res = max(res, j - i + 1)
            visited[ord(s[j])] = True
            
    return res

if __name__ == "__main__":
    s = "ABCBC"
    print(longestUniqueSubstr(s))  
    
#better approach
def longestUniqueSubstr(s):
#if string length is 0 return 0
    if len(s) == 0:
        return 0
    #if string length is 1 return 1
    if len(s) == 1:
        return 1
    #if string length is more than 1
    max_length = 0
    visited = [False] * 256
    
    #right and left pointers of sliding window
    left = 0
    right = 0
    while right < len(s):
        #if the character is repeated, move the left pointer to the right and mark visited as false until the repeating character is no longer part of the current window
        while visited[ord(s[right])]:
            visited[ord(s[left])] = False
            left += 1
        #if the character is not repeated, mark visited as true and move the right pointer to the right
        visited[ord(s[right])] = True
        
        #update the max length of the substring
        max_length = max(max_length, right - left + 1)
        right += 1
    return maxLength
if __name__ == "__main__":
    s = "ABCBC"
    print(longestUniqueSubstr(s))
        