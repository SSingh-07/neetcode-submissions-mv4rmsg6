# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        while len(lists) > 1:
            mergedlists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1 ] if (i + 1) < len(lists) else None
                mergedlists.append(self.merge_2_lists(list1, list2))

            lists = mergedlists
        
        return lists[0]


    def merge_2_lists(self, l1, l2):
        tmp = ListNode()
        track = tmp

        while l1 and l2:
            if l1.val <= l2.val:
                track.next = l1
                l1 = l1.next

            else:
                track.next = l2
                l2 = l2.next

            track = track.next


        if l1:
            track.next = l1

        if l2:
            track.next = l2

        return tmp.next
        

