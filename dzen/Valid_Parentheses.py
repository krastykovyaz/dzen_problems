# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_par = {')': '(', '}':'{',']':'['}
        s = list(s)
        for p in s:
            if p not in close_par:
                stack.append(p)
            elif len(stack) > 0:
                par = stack.pop()
                if par != close_par[p]:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False

if __name__=='__main__':
    sol = Solution()
    seq = '['
    print(sol.isValid(seq))