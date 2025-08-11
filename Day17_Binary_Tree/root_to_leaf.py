# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def allRootToLeaf(self, root):
        all_paths = []
        def dfs(node,path):
            if not node:
                return
            path.append(node.data)
            if not node.left and not node.right:#it's a leaf node
                all_paths.append(list(path))
            else:
                dfs(node.left,path)
                dfs(node.right,path)
            path.pop()#backtrack by removing current node from the path
        dfs(root,[])
        return all_paths
        # TC: O(N × H) → worst case O(N²), balanced O(N log N)
        # SC: O(N × H) for results + O(H) recursion stack → worst case O(N²), balanced O(N log N)


        