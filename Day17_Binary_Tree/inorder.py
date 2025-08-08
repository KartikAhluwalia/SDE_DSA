# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    def helper(self,root,res):
        if root is not None:
            self.helper(root.left,res) #Traverse Left Part
            res.append(root.val) #Traverse the node
            self.helper(root.right,res) #Traverse Right Part
    #TC : O(N)
    #SC : O(N)