# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS Solution
        res = []
        if root is None:
            return res
        q = deque([root])
        while q:
            level = len(q)
            for i in range(level):
                curr = q.popleft()
                
                #If its the the first node of current level
                if i==0:
                    res.append(curr.val)
                if curr.right is not None:#append right side into queue
                    q.append(curr.right)
                if curr.left is not None:#append left side into queue
                    q.append(curr.left)
        return res
        #TC : O(N)
        #SC : O(N)