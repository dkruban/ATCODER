class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.head = None
        self.prev = None
    
    def bToDLL(self, root):
        self.head = None
        self.prev = None
        self._inorder(root)
        return self.head
    
    def _inorder(self, root):
        if not root:
            return
        
        self._inorder(root.left)
        
        if self.prev:
            root.left = self.prev
            self.prev.right = root
        else:
            self.head = root
            
        self.prev = root
        
        self._inorder(root.right)
