# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp1 = slow.next
        slow.next = None
        nextN = None

        while temp1:
            temp2 = temp1.next
            temp1.next = nextN
            nextN = temp1
            temp1 = temp2
        
        head1 = head
        head2 = nextN

        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1

            head1 = temp1
            head2 = temp2
        
        if head2:
            head1.next = head2



