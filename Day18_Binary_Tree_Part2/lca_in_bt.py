# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #We would be using recursive traversal technique
        if root == None or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left == None: #if left is null then just take the right one
            return right
        elif right == None: #if right is null then just take the left one
            return left
        else:
            return root #if both are not null then we can return the root
        #TC : O(N)
        #SC : O(N)       
        