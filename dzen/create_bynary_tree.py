from collections import deque
class NodeTree:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None

def get_child(deque, cur_deque, cur_node, direct):
    # leaf = deque_[:1][0]
    # deque = deque_[:1]
    leaf = deque.popleft()
    if leaf is not None:
        if direct == 'l':
            cur_node.left = NodeTree(leaf)
            cur_deque.append(cur_node.left)
        if direct == 'r':
            cur_node.right = NodeTree(leaf)
            cur_deque.append(cur_node.right)
        




def get_tree(deque_, deque_orig):
    if len(deque_) <= 0:
        return None, None
    value = deque_[:1][0]
    deque_ = deque_[:1]
    root = NodeTree(value)
    root_orig = NodeTree(deque_orig.popleft())
    cur_deque = [root]
    cur_deque_orig = deque()
    cur_deque_orig.append(root)
    while len(deque_orig) > 0 and len(cur_deque_orig) > 0:
        cur_node = cur_deque[:1][0]
        cur_deque = cur_deque[:1]
        cur_node_orig = cur_deque_orig.popleft() 
        left = get_child(deque_orig, cur_deque_orig, cur_node_orig, 'l')
        right = get_child(deque_orig, cur_deque_orig, cur_node_orig, 'r')
    return root
        

if __name__=='__main__':
    root = [5, 3, 7, 1, 4, 6, 9, 0, 2, None, None, None, None, 8, 10]
    bt = get_tree(root, deque(root))