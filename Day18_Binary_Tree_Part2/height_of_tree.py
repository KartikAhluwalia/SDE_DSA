# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        left = 1+self.maxDepth(root.left) #traverse left of node
        right = 1+self.maxDepth(root.right) #traverse right of node
        return max(left,right)
        #TC : O(N)
        #SC : O(H)