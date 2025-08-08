from collections import deque
class Solution:
    def bfs(self,i,adj,visited):
        #Queue to store (node,parent)
        q = deque()
        #Push initial node in queue with no on was parent
        q.append((i,-1))
        visited[i] = True
        while q:
            #Traverse all the neigbours
            node,parent = q.popleft()

            #Traverse all the nighbours
            for it in adj[node]:
                #If not visited
                if not visited[it]:
                    #Mark the node as visited
                    visited[it] = True
                    q.append((it,node))
                elif it!=parent:
                    return True
        return False



    def isCycle(self, V, adj):
        #BFS we use a queue
        #Create a visited array
        visited = [False]*V
        ans = False

        #Start traversal from every univisited node
        for i in range(V):
            if not visited[i]:
                #Start BFS Traversal and update result
                ans = self.bfs(i,adj,visited)
                if ans:
                    break
        return ans
        #TC : O(V+E)
        #SC : O(V)