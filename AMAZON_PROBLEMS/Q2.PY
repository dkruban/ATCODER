class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    # Current node must be strictly greater than min and strictly less than max
    if root.val <= min_val or root.val >= max_val:
        return False
    
    # Left subtree must be less than current node's value
    # Right subtree must be greater than current node's value
    return (is_bst(root.left, min_val, root.val) and 
            is_bst(root.right, root.val, max_val))

# Wrapper
def check_bst(root):
    return 1 if is_bst(root) else 0
