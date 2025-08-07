# Topological sorting only works for Directed Acyclic Graphs
# It is a linear ordering such that if there is and edge b/w u and v
# u appears before v in that ordering
class Solution:
    def dfs(self,node,vis,stack,adj):
        vis[node] = 1
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it,vis,stack,adj)
        stack.append(node)


    def topoSort(self, V, adj):
        #Use a stack for topological sort using dfs
        vis = [0]*V
        stack = deque()
        for i in range(V):
            if not vis[i]:
                self.dfs(i,vis,stack,adj)
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans
    #TC : O(V+E)
    #SC : O(V)

       
