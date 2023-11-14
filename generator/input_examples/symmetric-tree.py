def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True

    queue = collections.deque([root.left, root.right])
    while queue:
        left = queue.popleft()
        right = queue.popleft()

        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        
        queue.append(left.left)
        queue.append(right.right)

        queue.append(left.right)
        queue.append(right.left)

    return True
