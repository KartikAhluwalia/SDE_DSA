class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            #Traverse and turn into water
            if i<0 or i >= m or j<0 or j>=n or grid[i][j] != '1': #edge case for out of bounds, we don't care about these position
                return
            else:
                grid[i][j] = '0' #set current to '0' and then traverse all neighbours
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j) 
        
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1#Logic is to increment by one if there is '1' and then perform dfs and turn all the '1' s on the island to '0'so that we don't consider them again
                    dfs(i,j)
        return num_islands
        #TC : O(M*N)
        #SC : O(M*N)



        
        