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

#pbm 2: Convert Min Heap to Max Heap

class Solution:
    def heapify_down(self,arr, N, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < N and arr[left] < arr[smallest]:
            smallest = left

        if right < N and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify_down(arr, N, smallest)
        
        
    def convertMinToMaxHeap(self, N, arr):
        # Step 1: Negate all elements in the heap
        for i in range(N):
            arr[i] = -arr[i]

        # Step 2: Re-heapify using the min-heap functions
        # Start from the last non-leaf node and move to the root
        for i in range((N // 2) - 1, -1, -1):
            self.heapify_down(arr, N, i)

        # Step 3: Negate all elements back to their original values
        for i in range(N):
            arr[i] = -arr[i]


#pbm 3: huffman coding

import heapq
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class Solution:

    def printCodes(self,node, code, codes):
        if node is None:
            return
    
        if node.char != '#':  #leaf node
            codes.append((code))
    
        self.printCodes(node.left, code + '0', codes)
        self.printCodes(node.right, code + '1', codes)

    def huffmanCodes(self,S,f,N):
        
        heap = []
    
        for i in range(N):
            heapq.heappush(heap, Node(S[i], f[i]))
    
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
        
            merged = Node('#', left.freq + right.freq)
            merged.left = left
            merged.right = right
        
            heapq.heappush(heap, merged)
    
        root = heapq.heappop(heap)
    
        codes = []
        self.printCodes(root, "", codes)
    
        return codes
