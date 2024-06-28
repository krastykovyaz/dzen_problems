from typing import Optional

class NodeTree:
    def __init__(self, x):
        self.right = None
        self.left = None
        self.val = x

    
class Solution:
    def get_depth(self, root: Optional[NodeTree])->int:
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res            