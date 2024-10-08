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
        