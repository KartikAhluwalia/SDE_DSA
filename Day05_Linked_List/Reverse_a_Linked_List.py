# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive approach
        if head == None or head.next == None:
            return head
        newHead = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead
        
        #Iterative Approach
        '''
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next #Save the next node
            curr.next = prev #Reverse the link
            prev = curr #Move pointers forward
            curr = next_node
        return prev

        '''