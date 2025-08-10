# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def bottomView(self, root):
        #your code goes here
        ans = []
        if not root:
          return ans
        mpp = {} #dictionary to store the bottom view nodes
        #element is a pair containing node
        #and its vertical position
        q = deque([(root,0)])
        while q:
          node,line = q.popleft() #pop the nodes in the queue
          mpp[line] = node.data #we update the last node seen at the vertical level
          if node.left:
            q.append((node.left,line-1))
          if node.right:
            q.append((node.right,line+1))
        for key in sorted(mpp.keys()):
          ans.append(mpp[key])
        return ans
        #TC : O(N log N)
        #SC : O(N)