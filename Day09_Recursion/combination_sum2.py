class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(list(cur))
                return
            if total > target or i == len(candidates):
                return
            #include element at index i
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            cur.pop()
            #skip at index i
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,cur,total)

        
        dfs(0,[],0)
        return res
        #TC : O(2^N)
        #SC : O(N)

        