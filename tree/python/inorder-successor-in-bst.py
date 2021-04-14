# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """LC 285. Inorder Successor in BST
        Time complexity O(N)
        Space: O(N)
        """
        if root is None or p is None:
            return None
        if p.right:
            ptr = p.right
            while ptr.left:
                ptr = ptr.left
            return ptr
        else:
            stack = []
            predeccessor = None
            ptr = root
            while (len(stack) > 0 or ptr):
                while ptr:
                    stack.append(ptr)
                    ptr = ptr.left
                current = stack.pop()
                if predeccessor:
                    return current
                if current.val == p.val:
                    predeccessor = p
                ptr = current.right
        return None

    def inorderSuccessor2(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """
        Constant space
        """
        if root is None or p is None:
            return None
        if p.right:
            ptr = p.right
            while ptr.left:
                ptr = ptr.left
            return ptr
        else:
            prev = None
            ptr = root
            while ptr:
                if prev:
                    return ptr
                if ptr.left is None:
                    if ptr == p:
                        prev = ptr
                    ptr = ptr.right
                else:
                    predecessor = ptr.left
                    while predecessor.right and predecessor.right != ptr:
                        predecessor = predecessor.right
                    if predecessor.right is None:
                        predecessor.right = ptr
                        ptr = ptr.left
                    else:
                        if ptr == p:
                            prev = ptr
                        predecessor.right = None
                        ptr = ptr.right
        return None