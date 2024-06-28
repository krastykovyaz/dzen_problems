class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution:        
    def lowestCommonAncestor(self, root, x, y):
        if not root or root.left is None or root.left is None:
            return root
        l = self.lowestCommonAncestor(root.left, x, y)
        r = self.lowestCommonAncestor(root.right, x, y)
        if r and l:
            return root
        return r or l

if __name__=='__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    p = root.left
    q = root.right
    solution = Solution()
    result = solution.lowestCommonAncestor(root, p, q)
    print(result.val)  # Output: 3
