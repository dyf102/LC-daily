# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        ptr = head.next
        head.next = None
        while ptr:
            tmp = ptr.next
            ptr.next = dummy.next
            dummy.next = ptr
            ptr = tmp
        return dummy.next
    
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
            