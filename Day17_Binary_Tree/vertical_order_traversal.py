# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        mpp = {}
        if not root:
            return res
        q = deque([(root,0,0)]) # store (node, column, row) to handle sorting by column, then row, then value

        while q:
            node, level, row = q.popleft()
            if level not in mpp:
                mpp[level] = []
            mpp[level].append((row,node.val))# store (row, value) so we can later sort first by row (top-to-bottom), then by value (tie-breaker)
            if node.left:
                q.append((node.left,level-1,row+1))
            if node.right:
                q.append((node.right,level+1,row+1))
        for level in sorted(mpp.keys()):
            level_nodes = sorted(mpp[level]) # sort nodes in this column by row first, then by value (Python's tuple sort handles this lexicographically)
            res.append([val for row,val in level_nodes]) # extract only the values after sorting
        return res
        # TC : O(N log N) due to sorting all nodes within columns
# SC : O(N) for storing nodes in the map and queue

        
        