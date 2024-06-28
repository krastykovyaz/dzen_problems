# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dd = defaultdict(int)
        t_dd = defaultdict(int)
        for c in s:
            s_dd[c] += 1
        for c in t:
            t_dd[c] += 1
        if s_dd == t_dd:
            return True
        return False