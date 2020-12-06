
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        """LC 1110 
        Runtime: 88ms

        Args:
            root (TreeNode): [description]
            to_delete (List[int]): [description]

        Returns:
            List[TreeNode]: [description]
        """
        result = []
        def helper(root, to_delete, is_root):
            if root:
                delete = root.val in to_delete
                if not delete and is_root:
                    result.append(root)
                root.left = helper(root.left, to_delete, delete)
                root.right = helper(root.right, to_delete, delete)
                return None if delete else root
            else:
                return None
        helper(root, to_delete, True)
        return result
