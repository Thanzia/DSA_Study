n,cows=map(int,input().split())
arr=[int(input().strip()) for _ in range(n)]
def Canweplace(arr,dist,cows):
    cntcows=1
    last=arr[0]
    for i in range(0,len(arr)):
        if arr[i]-last>=dist:
            cntcows+=1
            last=arr[i]
            if cntcows>=cows:
                return True
    return False
def aggrcows(arr,cows):
    arr.sort()
    
    low=0
    high=arr[n-1]-arr[0]
    while low<=high:
        mid=(low+high)//2
        if Canweplace(arr,mid,cows):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return high
result=aggrcows(arr,cows)
print(result)
        
