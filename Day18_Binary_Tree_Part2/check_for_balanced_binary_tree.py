# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_height(root):
            if not root:
                return 0
            leftHeight = dfs_height(root.left) #to check height of left tree
            if leftHeight == -1:
                return -1
            rightHeight = dfs_height(root.right) #to check height of right tree
            if rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight)>1:
                return -1
            return 1+max(leftHeight,rightHeight)
        return dfs_height(root)!=-1
        #TC : O(N)
        #SC : O(N)
        
        
        

        
        