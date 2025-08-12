class Solution:
    def findPlatform(self, Arrival, Departure):
        #your code goes here
        n = len(Arrival)
        Arrival.sort()
        Departure.sort()
        ans = 1
        cnt = 1
        i,j = 1,0 #we consider the arrival of nect train and departure of current one
        while i<n and j<n:
            if Arrival[i]<=Departure[j]: #that means next train arrive before the curent one leaves
                cnt+=1
                i+=1
            else: #if not the platform is free
                cnt-=1
                j+=1
            ans = max(ans,cnt)
        return ans
        #TC : O(N log N)
        #SC : O(1)
