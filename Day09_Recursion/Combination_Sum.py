class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(i,nums,res,path,target):
            if target<0:
                return
            if target == 0:
                res.append(path)
            for i in range(len(nums)):
                dfs(i,nums[i:],res,path+[nums[i]],target-nums[i])
        res = []
        dfs(0,candidates,res,[],target)
        return res
        # TC : O(2^T) T is target value
        # SC : O(T)