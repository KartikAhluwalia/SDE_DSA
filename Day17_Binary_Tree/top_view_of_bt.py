# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def topView(self, root):
        res = []
        if root is None:
            return res
        mpp  = {}
        q = deque([(root,0)])
        while q:
            node,line = q.popleft()
            if line not in mpp: #only update if there is no node for that line
                mpp[line] = node.data
            if node.left:
                q.append((node.left,line-1))
            if node.right:
                q.append((node.right,line+1))
        for key in sorted(mpp.keys()):
            res.append(mpp[key])
        return res
        #TC : O(N log N)
        #SC : O(N)