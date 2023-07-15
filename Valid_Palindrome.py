# 125. Valid Palindrome

# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        
        s = s.lower()
        s = [c for c in s if 'a' <= c <= 'z' or '0' <= c <= '9']
        i = 0
        j = len(s) - 1
        while i < len(s) and j > -1 and i <= j:
            while s[i] not in alphabet and i < len(s) and j > -1 and i <= j:
                i += 1
            while s[j] not in alphabet and i < len(s) and j > -1 and i <= j:
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
if __name__=='__main__':
    sol = Solution()
    t1 = '......a.....'
    t2 = "A man, a plan, a canal: Panama"
    t3 = "race a car"
    print(sol.isPalindrome(t3))