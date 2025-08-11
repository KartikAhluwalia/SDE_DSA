class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        self.func(0,s,path,res)
        return res
    def func(self,index,s,path,res):
        if index == len(s):
            res.append(path[:]) #lists in python are mutable so we need to append a copy of this list so that it doesnt get updated in res list as path list is updated
            return #we return after we reach the end of the string
        for i in range(index,len(s)):
            if self.isPalindrome(s,index,i):
                path.append(s[index:i+1])
                self.func(i+1,s,path,res)
                path.pop() #once the function returns i.e. we have reached the end of the string, we pop to explore different alterantive (we only pop the last inserted element kind of like a stack)
    def isPalindrome(self,s,start,end): #function to check whether the string is a palindrome or not
        while start<=end:
            if(s[start] != s[end]):
                return False
            start+=1
            end-=1
        return True
        #TC : O(N * 2^N)
        #SC : O(N)
        
        