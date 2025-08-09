# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #DFS Solution
    def rightView(self,root,level,res):
        if root is None:
            return
        if level == len(res): #if the level is reached append the node value to result
            res.append(root.val)
        self.rightView(root.right,level+1,res) #Check the right nodes first
        self.rightView(root.left,level+1,res) #then check the left nodes

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.rightView(root,0,res)
        return res
        #TC : O(N)
        #SC : O(H)
        
        