class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def _rob(root):
            if root is None:
                return (0, 0)
            left_rob, left_non_rob = _rob(root.left)
            right_rob, right_non_rob = _rob(root.right)
            
            rob = left_non_rob + right_non_rob + root.val
            non_rob = max(left_rob, left_non_rob) + max(right_rob, right_non_rob) 
            
            return (rob, non_rob)
        
        return max(_rob(root))