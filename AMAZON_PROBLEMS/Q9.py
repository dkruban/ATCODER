def check_leaves_same_level(root):
    if not root: return True
    
    leaf_level = None
    
    def dfs(node, level):
        nonlocal leaf_level
        if not node:
            return True
        
        if not node.left and not node.right:
            if leaf_level is None:
                leaf_level = level
            elif leaf_level != level:
                return False
            return True
        
        return dfs(node.left, level + 1) and dfs(node.right, level + 1)
    
    return dfs(root, 0)
