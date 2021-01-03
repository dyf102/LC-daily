class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        """LC 889 Construct Binary Tree from Preorder and Postorder Traversal
        Time complexity: O(N)
        Args:
            pre (List[int]): preorder travel
            post (List[int]): postorder travel

        Returns:
            TreeNode: binary tree
        """
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) > 1:
            idx = post.index(pre[1])
            root.left = self.constructFromPrePost(pre[1: idx + 2], post[:idx + 1])
            root.right = self.constructFromPrePost(pre[idx + 2:], post[idx + 1:-1])
        return root