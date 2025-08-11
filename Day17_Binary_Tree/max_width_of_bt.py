# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root):
        #your code goes here
        if not root:
            return 0
        ans = 0
        q = deque([(root,0)])
        while q:
            size = len(q)
            #Get the position of the front node in the current level
            front_pos = q[0][1]

            first = last = 0 #to store position of first and last positions of nodes in the current level
            for i in range(size):
                #Calculate current position relative to the min position in the level
                cur_idx = q[0][1] - front_pos #current index
                node = q[0][0] #get current node
                q.popleft() #pop the node from the queue
                if i == 0:
                    first = cur_idx
                #if this is last node in the level
                if i == size-1:
                    last = cur_idx
                if node.left:
                    q.append((node.left,cur_idx*2+1))
                if node.right:
                    q.append((node.right,cur_idx*2+2))
            ans = max(ans,last-first+1)
        return ans
        #TC : O(N)
        #SC : O(N)

