import heapq

#heapq implement min-heap
heapq.heapify(arr)
total_cost=0
while len(arr)>1:
    #always pop smallest element from the heap
    first=heapq.heappop(arr)
    #second smaalest
    second=heapq.heappop(arr)
    cost=first+second
    total_cost+=cost
    heapq.heappush(arr,cost)
print(total_cost)
