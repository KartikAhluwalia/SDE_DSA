# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        dummy = ListNode(0,head) #next node of dummy is head, incase head gets deleted
        first,second = head,dummy
        for _ in range(n):
            first = first.next
        while first != None: #we don't use first.next != None as it fails when there is only one node in the list
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
        #TC : O(N)
        #SC : O(1)



        