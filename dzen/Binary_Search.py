# 704. Binary Search

# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(seq, l, r, tg):
            mid = ((r-l) / 2) + l
            if seq[mid] == tg:
                return mid
            if (len(seq[l:r]) == 1 and seq[l:r][0] != tg) or len(seq[l:r]) == 0:
                return -1
            if seq[mid] > tg:
                return bs(seq, l, mid, tg)
            else:
                return bs(seq, mid, r, tg)
        return bs(nums, 0, len(nums) - 1, target)
    
if __name__=='__main__':
    sol = Solution()
    t1 = [2,5]
    target = 5
    print(sol.search(t1, target))