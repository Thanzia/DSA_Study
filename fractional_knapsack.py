class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    def fractionalknapsack(self, w,arr,n):
        #sort arr based on value/weight in decreasing order
        arr.sort(key=lambda x:x.value/x.weight,reverse=True)
        totalVal=0
        for i in range(n):
            if arr[i].weight<=w:
                totalVal+=arr[i].value
                w-=arr[i].weight
            else:
                totalVal+=(arr[i].value/arr[i].weight)*w
                break
        return totalVal
        
