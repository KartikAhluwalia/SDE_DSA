class Solution:
    def dfsOfGraph(self, V, adj):
      #There can be plenty of dfs depending on the starting node
      vis = [0] * V #Visited array to store the nodes that have been visited
      start = 0
      dfs_ls = [] #to store resulting dfs traversal
      #Recursive dfs function
      def dfs(node,adj,vis,dfs_ls):
        vis[node] = 1
        dfs_ls.append(node)
        for it in adj[node]:
          if not vis[it]:
            dfs(it,adj,vis,dfs_ls)
      dfs(start,adj,vis,dfs_ls)
      return dfs_ls
    #TC : O(V+E)
    #SC : O(V)