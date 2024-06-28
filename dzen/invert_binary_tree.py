from typing import Optional

class NodeTree:
    def __init__(self, x):
        self.val = x
        self.rigth = None
        self.left = None

class Solution:
    def invert_leaves(self, root: Optional[NodeTree])->Optional[NodeTree]:
        if not root:
            return None
        l = root.left
        r = root.right
        root.right = self.invert_leaves(l)
        root.left = self.invert_leaves(r)
        return root