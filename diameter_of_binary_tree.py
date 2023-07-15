from typing import Optional

class NodeTree:
    def __init__(self, x):
        self.right = None
        self.left = None
        self.val = x

    
class Solution:
    def get_diameter(self, root: Optional[NodeTree])->int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return -1
            l = dfs(root.left) + 1
            r = dfs(root.right) + 1
            res = max(res, l + r)
            return max(l , r)
        dfs(root)
        return res
        