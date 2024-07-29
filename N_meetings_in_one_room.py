class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meet=[(start[i],end[i],i+1) for i in range(n)]
        meet_sorted=sorted(meet,key=lambda x:x[1])
        #answer=[]
        limit=meet_sorted[0][1]
        #answer.append(meet_sorted[0].pos)
        cnt=1
        for i in range(1,n):
            if meet_sorted[i][0]>limit:
                limit=meet_sorted[i][1]
                #answer.append(meet_sorted[i].pos)
                cnt+=1
        return cnt
