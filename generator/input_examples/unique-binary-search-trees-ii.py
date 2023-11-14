class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_trees(n):
    if n == 0:
        return []
    return generate_trees_helper(1, n)

def generate_trees_helper(start, end):
    trees = []
    if start > end:
        trees.append(None)
        return trees
    
    for i in range(start, end+1): 
        left_trees = generate_trees_helper(start, i-1)
        right_trees = generate_trees_helper(i+1, end)
        
        for l in left_trees:
            for r in right_trees:
                current_tree = TreeNode(i)
                current_tree.left = l 
                current_tree.right = r
                trees.append(current_tree)
    return trees
