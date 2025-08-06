"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Clone the original nodes moapped to new nodes in a hashmap
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy_node = Node(node.val) #this will throw error if node is null hence in the last return we consider that case as well
            oldToNew[node] = copy_node
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
            return copy_node
        return(dfs(node)) if node else None #if node is null just return None
        #TC : O(N) N is Number of Edges + Number of Vertices => O(V+E)
        #SC : O(N) => O(V+E)

        