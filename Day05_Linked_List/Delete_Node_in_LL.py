# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val #Copy the value of the next node into the current one
        node.next = node.next.next #Skip the current node
        #TC : O(1)
        #SC : O(1)
        