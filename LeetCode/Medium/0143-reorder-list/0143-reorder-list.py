# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head.next:

            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            l2 = slow.next
            slow.next = None
            l1 = head

            prev = None
            while l2:
                temp = l2.next
                l2.next = prev
                prev = l2
                l2 = temp
            l2 = prev
            
            while l1 and l2:
                temp1 = l1.next
                temp2 = l2.next
                l1.next = l2
                l2.next = temp1
                l1 = temp1
                l2 = temp2
            
            if l2:
                l1.next = l2