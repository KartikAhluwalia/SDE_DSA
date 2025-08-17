class Solution:
    def reverse(self,s,l,r):
        while l<r:
            s[l],s[r] = s[r],s[l] #swap
            l+=1
            r-=1
    def reverseWords(self, s: str) -> str:
        s = list(s) #"hello world"
        s.reverse() #Reverse the whole string -> "dlrow olleh"
        i,k,n =0,0,len(s) #i is scanning input, k is building result in place
        while i<n:
            #to find the starting position of the next word 
            while i<n and s[i] == " ":
                i+=1
            if i!=n and k>0:
                s[k] = " "
                k+=1
            start_index = k
            #Find the ending pos of the word
            while i<n and s[i]!=" ":
                s[k] = s[i]
                i+=1
                k+=1
            self.reverse(s,start_index,k-1)
        s = s[:k]
        return "".join(s)
        #TC : O(N)
        #SC : O(1)

