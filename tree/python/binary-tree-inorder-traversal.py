# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        LC 94. Binary Tree Inorder Traversal
        Non-recursive implementation
        Time complexity: O(N)
        Space: O(N)
        """
        result = []
        stack = []
        ptr = root

        while ptr or len(stack) > 0:
            while ptr:
                stack.append(ptr)
                ptr = ptr.left
            current = stack.pop()
            result.append(current.val)
            ptr = current.right
        return result

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        Morris Algorithm
        Constant space solution
        """
        result = []
        ptr = root
        while ptr:
            if ptr.left is None:
                result.append(ptr.val)
                ptr = ptr.right
            else:
                # find right most node on left tree
                predecessor = ptr.left
                while predecessor.right and predecessor.right != ptr:
                    pre = pre.right
                # build return link
                if pre.right is None:
                    predecessor.right = ptr 
                    ptr = ptr.left
                else: # left subtree has been visited 
                    result.append(ptr.val)
                    predecessor.right = None
                    ptr = ptr.right
        return result

