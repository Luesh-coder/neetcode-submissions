# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        curr = root
        carry, newVal = 0, 0
        while l1 or l2:
            twoSum = 0 + carry

            if l1:
                twoSum += l1.val
            if l2:
                twoSum += l2.val
            
            if twoSum >= 10:
                newVal = twoSum % 10
                carry = 1
            else:
                newVal = twoSum
                carry = 0

            curr.next = ListNode(newVal)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2: 
                l2 = l2.next
        
        if carry == 1:
            curr.next = ListNode(1)

        return root.next


