# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def isLeaf(node):
            return node.left is None and node.right is None
        #First take the left boundary excluding the leaf nodes
        def left_without_leaf(root,res):
            cur = root.left
            while cur != None:
                if(isLeaf(cur) == False):
                    res.append(cur.val)
                if cur.left != None:
                    cur = cur.left
                else:
                    cur = cur.right

        #Take leaf nodes
        def addLeaves(root,res):
            if isLeaf(root):
                res.append(root.val)
                return
            if root.left!=None:
                addLeaves(root.left,res)
            if root.right!=None:
                addLeaves(root.right,res)


        #Lastly take right boundary in the reverse direction while excluding the leaf ndoes
        def right_without_leaf(root,res):
            cur = root.right
            tmp = []#basically works as a stack
            while cur != None:
                if isLeaf(cur) == False:
                    tmp.append(cur.val)
                if cur.right!=None:
                    cur = cur.right
                else:
                    cur = cur.left
            for i in range(len(tmp)-1,-1,-1):
                res.append(tmp[i])
        
        res = []
        if not isLeaf(root):
            res.append(root.val)
        left_without_leaf(root,res)
        addLeaves(root,res)
        right_without_leaf(root,res)
        return res
        #TC : O(N)
        #SC : O(N)
        
