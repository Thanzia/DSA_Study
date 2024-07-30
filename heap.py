# Python code to depict 
# the implementation of a max heap. 

class MaxHeap: 
	# A pointer pointing to the elements 
	# in the array in the heap. 
	arr = [] 

	# Maximum possible size of 
	# the Max Heap. 
	maxSize = 0

	# Number of elements in the 
	# Max heap currently. 
	heapSize = 0

	# Constructor function. 
	def __init__(self, maxSize): 
		self.maxSize = maxSize 
		self.arr = [None]*maxSize 
		self.heapSize = 0

	# Heapifies a sub-tree taking the 
	# given index as the root. 
	def MaxHeapify(self, i): 
		l = self.lChild(i) 
		r = self.rChild(i) 
		largest = i 
		if l < self.heapSize and self.arr[l] > self.arr[i]: 
			largest = l 
		if r < self.heapSize and self.arr[r] > self.arr[largest]: 
			largest = r 
		if largest != i: 
			temp = self.arr[i] 
			self.arr[i] = self.arr[largest] 
			self.arr[largest] = temp 
			self.MaxHeapify(largest) 

	# Returns the index of the parent 
	# of the element at ith index. 
	def parent(self, i): 
		return (i - 1) // 2

	# Returns the index of the left child. 
	def lChild(self, i): 
		return (2 * i + 1) 

	# Returns the index of the 
	# right child. 
	def rChild(self, i): 
		return (2 * i + 2) 

	# Removes the root which in this 
	# case contains the maximum element. 
	def removeMax(self): 
		# Checking whether the heap array 
		# is empty or not. 
		if self.heapSize <= 0: 
			return None
		if self.heapSize == 1: 
			self.heapSize -= 1
			return self.arr[0] 

		# Storing the maximum element 
		# to remove it. 
		root = self.arr[0] 
		self.arr[0] = self.arr[self.heapSize - 1] 
		self.heapSize -= 1

		# To restore the property 
		# of the Max heap. 
		self.MaxHeapify(0) 

		return root 

	# Increases value of key at index 'i' to new_val.
	# maximum value will always be at the root .hence bubbling-up is 
	# used to restore heapify 
	def increaseKey(self, i, newVal): 
		self.arr[i] = newVal 
		while i != 0 and self.arr[self.parent(i)] < self.arr[i]: 
			temp = self.arr[i] 
			self.arr[i] = self.arr[self.parent(i)] 
			self.arr[self.parent(i)] = temp 
			i = self.parent(i) 

	# Returns the maximum key 
	# (key at root) from max heap. 
	def getMax(self): 
		return self.arr[0] 

	def curSize(self): 
		return self.heapSize 

	# Deletes a key at given index i. 
	def deleteKey(self, i): 
		# It increases the value of the key 
		# to infinity and then removes 
		# the maximum value. 
		self.increaseKey(i, float("inf")) 
		self.removeMax() 

	# Inserts a new key 'x' in the Max Heap. 
	def insertKey(self, x): 
		# To check whether the key 
		# can be inserted or not. 
		if self.heapSize == self.maxSize: 
			print("\nOverflow: Could not insertKey\n") 
			return

		# The new key is initially 
		# inserted at the end. 
		self.heapSize += 1
		i = self.heapSize - 1
		self.arr[i] = x 

		# The max heap property is checked by bubble-up approach  
		# and if violation occurs, 
		# it is restored moving from last to up upto root 
		while i != 0 and self.arr[self.parent(i)] < self.arr[i]: 
			temp = self.arr[i] 
			self.arr[i] = self.arr[self.parent(i)] 
			self.arr[self.parent(i)] = temp 
			i = self.parent(i) 


# Driver program to test above functions. 
if __name__ == '__main__': 
	# Assuming the maximum size of the heap to be 15. 
	h = MaxHeap(15) 

	# Asking the user to input the keys: 
	k, i, n = 6, 0, 6
	print("Entered 6 keys:- 3, 10, 12, 8, 2, 14 \n") 
	h.insertKey(3) 
	h.insertKey(10) 
	h.insertKey(12) 
	h.insertKey(8) 
	h.insertKey(2) 
	h.insertKey(14)
	print(h.deleteKey(4))

	# Printing the current size 
	# of the heap. 
	#print("The current size of the heap is "+ str(h.curSize()) + "\n") 

	# Printing the root element which is 
	# actually the maximum element. 
	#print("The current maximum element is " + str(h.getMax()) + "\n")


	#print("The current size of the heap before deletion is is "+ str(h.curSize()) + "\n") 
	#print(h.arr)
        # Deleting key at index 2. 
	
	#print(h.arr)
	# Printing the size of the heap 
	# after deletion. 
	#print("The current size of the heap after deletion is "+ str(h.curSize()) + "\n") 

	# Inserting 2 new keys into the heap. 
	h.insertKey(15) 
	h.insertKey(5) 
	#print("The current size of the heap is "+ str(h.curSize()) + "\n") 
	#print("The current maximum element is " + str(h.getMax()) + "\n")
