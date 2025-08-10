# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def tree_traversal(self, root):
        st = deque([(root,1)]) #stack for storing (node,num)
        #num is the indicator for preorder(1),inorder(2) and postorder(3)
        pre, in_order,post = [],[],[]
        if root is None:
            return [pre,in_order,post]
        while st:
            node,state = st.pop()
            if state == 1:
                pre.append(node.data)
                st.append((node,2))
                if node.left:
                    st.append((node.left,1))
            elif state == 2:
                in_order.append(node.data)
                st.append((node,3))
                if node.right:
                    st.append((node.right,1))
            else:
                post.append(node.data)
        return [in_order,pre,post]
        #TC : O(3*N)
        #SC : O(4*N) one N extra for stack
        
        
        