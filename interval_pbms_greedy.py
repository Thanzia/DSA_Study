#merge intervals

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    n=len(intervals)
    intervals.sort()
    ans=[]
    for i in range(n):
        # if the current interval does not
        # lie in the last interval:
        if not ans or intervals[i][0]>ans[-1][1]:
            ans.append(intervals[i])
        # if the current interval
        # lies in the last interval:
        else:
            ans[-1][1]=max(ans[-1][1],intervals[i][1])
    return ans

#insert intervals

def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res=[]
    i=0
    n=len(intervals)
    while(i<n and intervals[i][1]<newInterval[0]):
        res.append(intervals[i])
        i+=1
    while(i<n and intervals[i][0]<=newInterval[1]):
        newInterval[0]=min(newInterval[0],intervals[i][0])
        newInterval[1]=max(newInterval[1],intervals[i][1])
        i+=1
    res.append(newInterval)
    while(i<n):
        res.append(intervals[i])
        i+=1
    return res

#non overlapping intervals

def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    n=len(intervals)
    sorted_intervals=sorted(intervals,key=lambda x:x[1])
    limit=sorted_intervals[0][1]
    cnt=1
    for i in range(1,n):
        if sorted_intervals[i][0]>=limit:
            limit=sorted_intervals[i][1]
            cnt+=1
    return n-cnt
