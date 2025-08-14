# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightOfTree(self,root):
        if root is None:
            return 0
        lh = self.heightOfTree(root.left) #left height of tree
        rh = self.heightOfTree(root.right) #right height of tree
        self.diameter = max(self.diameter,lh+rh) #update diameter considering the node as the pivot
        return 1+max(lh,rh) 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Things to keep in mind :
        # 1. Diameter of tree is max path between any two nodes
        # 2. The path need not traverse through the root 

        #First find height of tree in O(N) and in that code itslef keep updating the diameter
        self.diameter = 0
        self.heightOfTree(root)

        return self.diameter
        #TC : O(N)
        #SC : O(H)
