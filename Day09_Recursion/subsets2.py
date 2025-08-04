class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        # Sort to group duplicates together, which is essential for skipping
        nums.sort()

        def dfs(idx, path):
            # Always add the current subset to the result
            res.append(path)

            # Try all possibilities starting from index 'idx'
            for i in range(idx, len(nums)):
                # Skip duplicate elements at the same recursive level
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                # Include nums[i] and move forward
                dfs(i + 1, path + [nums[i]])

        # Start recursion from index 0 with an empty path
        dfs(0, [])
        return res
        #TC : O(2^n)
        #SC : O(2^n * k) , k is average length of subsets
