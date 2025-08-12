class Solution:
    def maxMeetings(self, start, end):
        #your code goes here
        n = len(start)
        meetings = []
        for i in range(n):
            meetings.append((start[i],end[i]))
        meetings.sort(key = lambda x:x[1]) #sort according to end time of the meetings
        limit = meetings[0][1]
        cnt = 1
        for i in range(1,n):
            if limit<meetings[i][0]:
                cnt+=1 #update cnt
                limit= meetings[i][1] #reset the limit to the end time of the current meeting
        return cnt
        #TC : O(N+N log N)
        #SC : O(N)