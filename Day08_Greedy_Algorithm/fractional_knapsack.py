class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        # Your code goes here
        n = len(val)
        #create a list to store value and weight
        items = [[val[i],wt[i]] for i in range(n)]
        #Sort items based on value to weight ratio in descending order
        items.sort(key = lambda x:x[0]/x[1],reverse= True)

        res = 0.0
        currentCapacity = cap
        for i in range(n):
            if items[i][1]<=currentCapacity:#to take entire item
                res+=items[i][0]
                currentCapacity -= items[i][1]
            else:#take fraction of item
                res+=(1.0*items[i][0]/items[i][1]) * currentCapacity
                break
        return res
        # TC : O(N log N)
        # SC : O(N)