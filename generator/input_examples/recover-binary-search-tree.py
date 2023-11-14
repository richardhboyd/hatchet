# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Traverse the tree in-order and store the node values in a list
        nodes = []
        self.inorder(root, nodes)
        
        # Find the two swapped nodes
        x = y = None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i+1].val:
                y = nodes[i+1] 
                if x is None:
                    x = nodes[i]
                else:
                    break
        
        # Swap the values of the two nodes        
        x.val, y.val = y.val, x.val
        
    def inorder(self, root, nodes):
        if root:
            self.inorder(root.left, nodes)
            nodes.append(root)
            self.inorder(root.right, nodes)
