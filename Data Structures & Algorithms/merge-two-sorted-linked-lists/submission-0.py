# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        head = ListNode()
        res = head


        while head1 and head2:
            if head1.val <= head2.val:
                res.next = head1
                res = head1
                head1 = head1.next
            else:
                res.next = head2
                res = head2
                head2 = head2.next
        
        if head1 :
            res.next = head1

        if head2:
            res.next = head2


        return head.next

            
                
        