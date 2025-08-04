class Solution:
	def subsetSums(self, arr):
		# brute force approach would be to use power set
		# for optimal we use pick/not pick recursion
		N = len(arr)
		def rec(index,sum,arr,N,sumSubset):
		    if index == len(arr):#You have decided for all elements
		        sumSubset.append(sum)
		        return
		    #pick the element
		    rec(index+1,sum+arr[index],arr,N,sumSubset)
		    #don't pick the element
		    rec(index+1,sum,arr,N,sumSubset)
		sumSubset = []
		sum = 0
		rec(0,sum,arr,N,sumSubset)
		return sumSubset
	
        # TC: O(2^N) - because there are 2 choices (pick or not pick) for each element
        # SC: O(2^N) - to store all possible subset sums in sumSubset