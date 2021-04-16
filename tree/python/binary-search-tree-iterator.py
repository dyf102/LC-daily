# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """LC 173. Binary Search Tree Iterator
    """

    def __init__(self, root: TreeNode):
        self.ptr = root
        self.stack = []

    def next(self) -> int:
        ptr = self.ptr
        while ptr:
            self.stack.append(ptr)
            ptr = ptr.left
        current = self.stack.pop()
        self.ptr = current.right
        return current.val

    def hasNext(self) -> bool:
        return self.ptr is not None or len(self.stack) > 0
class BSTIterator:
    """Constant space solution
    """

    def __init__(self, root: TreeNode):
        self.ptr = root

    def next(self) -> int:
        if self.ptr is None:
            return None
        if self.ptr.left is None:
            val = self.ptr.val
            self.ptr = self.ptr.right
            return val
        else:
            predecessor = self.ptr.left
            while predecessor.right and predecessor.right != self.ptr:
                predecessor = predecessor.right
            if predecessor.right is None:
                predecessor.right = self.ptr
                self.ptr = self.ptr.left
                return self.next()
            else:
                val = self.ptr.val
                predecessor.right = None
                self.ptr = self.ptr.right
                return val
    def hasNext(self) -> bool:
        return self.ptr is not None

