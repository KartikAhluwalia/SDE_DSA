# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        if not root:
            return []
        res = []
        direction = 1 #toggle for zizag level order traversal
        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)  
                    q.append(node.left)      
                    q.append(node.right)  
            if direction == -1:
                level.reverse()
            if level:
                res.append(level)
            direction *= -1
            
        return res
        #TC : O(N)
        #SC : O(N)




        