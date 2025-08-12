class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0 #number of content children
        num_children = len(g)
        num_cookies = len(s)
        i,j = 0,0
        while i<num_children and j<num_cookies:
            if g[i]<=s[j]: #if greed is satisfied by size of cookie
                i+=1
                j+=1
                ans+=1
            else: #move to the next cookie to satisfy the curent child
                j+=1
        return ans
        #TC : O(N log N) + O(M log M)
        #SC : O(1)




        