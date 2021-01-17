# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """LC 19. Remove Nth Node From End of List
        Time complexity: O(N)
        Sapce: O(N)
        It can be optimized by tail optimization
        """
        if head is None:
            return None
        
        def helper(node):
            if  node is None:
                return 0
            to_end = helper(node.next) + 1
            if to_end == n + 1:
                if node.next != None:
                    node.next = node.next.next
            return to_end
        
        dummy = ListNode()
        dummy.next = head
        helper(dummy)
        return dummy.next
        