#Topological sort usign BFS in called Kahn's Algorithm
class Solution:
    def topoSort(self, V, adj):
        #Use a queue for bfs
        #This is a slightly modified bfs algorithm because there would be an indegree list
        #Indegree is number of incoming edges to a node

        #Insert all nodes with indergree 0 initially
        #Take them out of the queue i.e. if a node with different indegree is not pushed till 
        #its indegree comes donw to zero and then is appended to the ans
        indegree = [0]*V
        for i in range(V):
            for it in adj[i]:
                indegree[it]+=1
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        topo_bfs = [] #Result for topo sort
        while queue:
            node = queue.popleft()
            topo_bfs.append(node)
            #node in topo sort
            #so we reduce indegree of the adj node
            for it in adj[node]:
                indegree[it]-=1
                if indegree[it] == 0:
                    queue.append(it)
        return topo_bfs
        #TC : O(V+E)
        #SC : O(V)
