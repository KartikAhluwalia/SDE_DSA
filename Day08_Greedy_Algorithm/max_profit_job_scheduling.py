class Solution:
    def JobScheduling(self, Jobs):
        #your code goes here
        Jobs.sort(key = lambda x:x[2],reverse = True)
        n = len(Jobs)
        #max deadline
        maxDeadline = -1
        for it in Jobs:
          maxDeadline = max(maxDeadline,it[1])
        #Initialize a hash table to store selected jobs
        hash = [-1] * (maxDeadline+1)
        cnt = 0
        totalProfit = 0
        for i in range(n):
          for j in range(Jobs[i][1] -1,-1,-1):
            if hash[j] ==-1:
              cnt+=1
              hash[j] = Jobs[i][0]
              totalProfit+=Jobs[i][2]
              break
        return [cnt,totalProfit]
        #TC : O(N^2 + N log N)
        #SC : O(N)