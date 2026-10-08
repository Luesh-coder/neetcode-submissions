# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1, ptr2 = head, head

        while ptr1 and ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next if ptr2.next else None
            
            if ptr1 and ptr2:
                if ptr1.val == ptr2.val:
                    return True
        return False