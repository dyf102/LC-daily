
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """LC 23. Merge k Sorted Lists
        Divide and conquer approach
        """
        def mergeTwo(first, second):
            dummy = ListNode()
            ptr = dummy
            while first and second:
                if first.val < second.val:
                    ptr.next = first
                    first = first.next
                else:
                    ptr.next = second
                    second = second.next
                ptr = ptr.next
            ptr.next = first if first else second
            return dummy.next
        
        def split(start, end):
            if end < start:
                return None
            if start == end:
                return lists[start]
            elif start + 1 == end:
                return mergeTwo(lists[start], lists[end])
            else:
                return mergeTwo(split(start, (start + end) // 2), split((start + end) // 2 + 1, end))
        
        return split(0, len(lists) - 1)