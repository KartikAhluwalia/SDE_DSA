class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        numbers = []
        for i in range(1,n):
            fact*=i #dont include n since we consider the first position fixed so there would be (n-1)! choices with the remaining numbers
            numbers.append(i)
        numbers.append(n)
        ans = ""
        k-=1 #converting to zero-based indexing
        while True:
            ans+=str(numbers[k//fact]) #append the number to the ans
            numbers.pop(k//fact) #pop this number since it won't be used further
            if not numbers: #if numbers is empty just break and return ans
                break
            k %= fact #this for finding the sequence in the next block
            fact //=len(numbers) #for finding the block
        return ans
        #TC : O(N^2)
        #SC : O(N)