class Solution:
    def bfsOfGraph(self, V, adj):
      start = 0
      #Use a queue data structure
      q = deque()
      vis = [0] * V #Visted array
      vis[0] = 1 #first nnode is marked as visited
      q.append(start) #First node is appended to the queue
      bfs_ls = []
      while q:
        node = q.popleft()
        bfs_ls.append(node)
        for it in adj[node]:
          if not vis[it]:
            vis[it] = 1 
            q.append(it)
      return bfs_ls
    #TC : O(V+E)
    #SC : O(V)

      