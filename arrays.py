#hashing

#if it consists of lowercase only

#hash array of size26
hash=[0]*26 
print(hash)
s="abaaaacdaaaefhhhffdeerrg"
char=str(input())

'''precompute'''

for i in range(0,len(s)):
    hash[ord(s[i])-ord('a')]+=1
print(hash[ord(char)-ord('a')])


#if it consists of all characters then no need of subtracting from ord('a') of autocasting of characters
hash=[0]*256 
s="abaaaacdaaaAASSVVefhhhffdeerrg"
char=str(input())
for i in range(0,len(s)):
    hash[ord(s[i])]+=1
print(hash[ord(char)])

              #hashmaping   Dictionary
'''T.C for ordered mapping in all case O(logN)
#and in unoredered map its T.C :O(1) in best and average and O(N)in worst case

#if size of array in the order of 10^8 more
#than 10^7 we cannot use list as DS bcz we have to declare the list in that order (if arr=[1,2,3,5,12] we have to declare size of has as 12) 
#instead use dictionary(here we can have the key values as 1,2,3,5,12 only sizeof dict will be 5 instead of 12 in the previos)'''

from collections import defaultdict  #dont forget
n=6
arr=[1,2,3,3,4,4]
num=int(input())
hashmap={}
hashmap=defaultdict(int)#instead can use if num in arr[i]:hashmap[arr[i]]+=1 else:hashmap[arr[i]]=1
for i in range(0,n):
    hashmap[arr[i]]+=1
print(hashmap[num])

#to hashmapping string

from collections import defaultdict
n=6
s="abcdefg"
num=str(input())
hashmap={}
hashmap=defaultdict(int)
"""we can assign value to corresponding char as key {'a':1}"""
for c in s:        
    hashmap[c]+=1
print(hashmap[num])


#no.of subarrays with sum equals k
'''in the brute force 3 for loops T.C O(n^3)'''
#optimal

from collections import defaultdict
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={}      """ initialize a dict and it stores how presum as key and number of times the presum occurs as another count is the value of the key"""
        hashmap=defaultdict(int)
        hashmap[0]=1       """initialize 0 key to 1"""
        preSum=0
        cnt=0
        for i in range(0,len(nums)):
            preSum+=nums[i]
            remove=preSum-k        """find s-k"""
            cnt+=hashmap[remove]    """by searching dict find how many times s-k occurs and it will be adddedd as each count"""
            hashmap[preSum]+=1       """"modify presum with the new presum value or updte the value if t already exists"""
        return cnt


#majority element in an array
    
"""element appears more than n//2times using hashmap""" 
from collections import defaultdict
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        hashmap=defaultdict(int)
        n=len(nums)
        for i in range(0,n):
            hashmap[nums[i]]+=1
        for i in hashmap:
            if hashmap[i]>n//2:
                return i

"""using moores voting algorithm"""
def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        for i in range(0,len(nums)):
            if cnt==0:     """take first elemnt as the answer and run for a count"""
                cnt+=1      
                element=nums[i]
            elif nums[i]==element:   """if t appears again incr cnt and if another elemnt occurs decr cnt go untill cnt becomes 0 .
                                      if 0 go to if statement and take nesxt one as new elemnt and repeat fo"""
                cnt+=1
            else:
                cnt-=1
        return element

#find maximum sum of subarray

lsum=0
nums=[-2,1,-3,4,-1,2,1,-5,4]
maxi=float('-inf')
for i in range(0,len(nums)):
    lsum+=nums[i]
    print(lsum)
    if lsum>maxi:
        maxi=lsum
    if lsum<0:
        lsum=0
print(maxi)


#count inversions

"""by using merge sort we can do the count of inversions"""
"""tc:O(nlogn) sc:O(n)"""

class Solution:
    cnt=0
    def merge(self,arr,l,m,r):    """merging the sorted array"""
        temp=[]
        left=l
        right=m+1
        while(left<=m and right<=r):
            if(arr[left]<=arr[right]):
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                self.cnt+=((m-left)+1)
                right+=1
        while(left<=m):
            temp.append(arr[left])
            left+=1
        while(right<=r):
            temp.append(arr[right])
            right+=1
            
        for i in range(len(temp)):
            arr[l + i] = temp[i]
        
    def mergeSort(self,arr,l,r):
        if l>=r:
            return 
        m=(l+r)//2
        self.mergeSort(arr,l,m)
        self.mergeSort(arr,m+1,r)
        self.merge(arr,l,m,r)
        return arr
        
    def inversionCount(self, arr, n):
        self.cnt=0    """since calling static variable.it can be made local by giving cnt+=in every fn call as it returns the count"""
        self.mergeSort(arr,0,n-1)
        return self.cnt

    #merging intervals


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort()
        ans=[]
        for i in range(0,n):
            start=intervals[i][0]
            end=intervals[i][1]
            if ans and end<=ans[-1][1]:  """First iteration (i=0):
                                             start = 1, end = 3
                                             ans is empty, so [1, 3] is added to ans.
                                               ans = [[1, 3]]
                                              Second iteration (i=1):
                                            start = 2, end = 4
                                          end (4) is greater than ans[-1][1] (3), so [2, 4] is added to ans.
                                          ans = [[1, 3], [2, 4]]"""

                continue
            for j in range(i+1,n):
                if intervals[j][0]<=end:
                    end=max(end,intervals[j][1])
                else:
                    break
            ans.append([start,end])
        return ans
        
#to find maximum sum in an array by selecting from left end
    #or right end or one left and B-1 remaining right

    class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n=len(A)
        #handling the edge case
        if B>=n:
            return sum(A)
        #calculate initial sum of first B elements
        currentSum=sum(A[:B])
        maxSum=currentSum
        #sliding window to approach maximum sum
        for i in range(1,B+1):
            currentSum=currentSum-A[B-i]+A[n-i]
            maxSum=max(maxSum,currentSum)
        return maxSum

#longest consecutive sequence
"""tc: O(n^2) sc: O(1)"""

      def linearsearch(self,nums,target):   
        for i in range(0,len(nums)):
            if nums[i]==target:
                return True
        return False

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        longest=1
        for i in range(n):
            x=nums[i]
            cnt=1
            while(self.linearsearch(nums,x+1)):
                x+=1
                cnt+=1
            longest=max(longest,cnt)
        return longest
    
    """samee problem better approach"""

     def longestConsecutive(self, nums: List[int]) -> int:
        currcnt=0
        longest=1
        lastsmaller=float('-inf')
        nums.sort()
        if not nums:
            return 0
        for i in range(0,len(nums)):
            if (nums[i]-1==lastsmaller):
                currcnt+=1
                lastsmaller=nums[i]
            elif(nums[i]!=lastsmaller):
                currcnt=1
                lastsmaller=nums[i]
            longest=max(longest,currcnt)
        return longest

    """optimal approach with tc:O(3n)and sc:O(n)"""



def longestSuccessiveElements(a):
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set()
    # put all the array elements into set
    for i in range(n):
        st.add(a[i])

    # Find the longest sequence
    for it in st:
        # if 'it' is a starting number
        if it - 1 not in st:
            # find consecutive numbers
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)


#product subarray less than k

 def countSubArrayProductLessThanK(self, a, n, k):
        if k<=-1:
            return 0
        product=1
        start=0
        cnt=0
        for end in range(0,n):
            product*=a[end]
            """to shrink window divide by a[0] check again divide by a[1]
            until prod less than k""""
            
            while(product>=k and start<=end):
                product//=a[start]
                start+=1
            cnt+=(end-start+1)
        return cnt

    """Tc:O(n) and sc:O(1)"""

    #maximum product subarray

     def maxProduct(self, nums: List[int]) -> int:
        pref=1
        suff=1
        ans=float('-inf')
        ans1="-inf"
        n=len(nums)
        for i in range(0,n):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref*=nums[i]
            suff*=nums[n-i-1]
            
            ans=max(ans,max(pref,suff))
        return ans

    """  T.C:O(n)  S.C:O(1) """

    #ksized subarrray maximum

    from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        deq=deque()
        result=[]
        for i in range(0,n):
            """remove elements not within the window"""
            if deq and deq[0]==i-k:
                deq.popleft()
            """remove elements smaller than the current element from the deque"""
            while deq and arr[deq[-1]]<=arr[i]:
                deq.pop()
            """add current element index to deq"""
            deq.append(i)
            """append the maximum of current window to resultlist"""
            if i>=k-1:
                result.append(arr[deq[0]])
        return result


  #4sum

from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums) # size of the array
    ans = []

    # sort the given array:
    nums.sort()

    # calculating the quadruplets:
    for i in range(n):
        # avoid the duplicates while moving i:
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            # avoid the duplicates while moving j:
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # 2 pointers:
            k = j + 1
            l = n - 1
            while k < l:
                _sum = nums[i] + nums[j] + nums[k] + nums[l]
                if _sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1

                    # skip the duplicates:
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif _sum < target:
                    k += 1
                else:
                    l -= 1

    return ans

""" T.C: O(n^3) S.C:  O(1)


         #MATRIX

find the row with maximum number of ones"""

	def rowWithMax1s(self,arr, n, m):
	    len1=0
	    maxi=0
	    ans=-1
	    for i in range(0,n):
	        for j in range(0,m):
	            if arr[i][j]==1:
	                len1=m-j       """"since matrix sorted columnsize-current column give no.of ones in that particular row"""
	                if len1>maxi:
	                    ans=i
	                    maxi=max(maxi,len1)
	    return ans
        


#rotate matrix in clockwise by 90

	def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(0,n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]  """find transpose"""
        for i in range(0,n):
            matrix[i].reverse()   """reverse each row"""


#spirally traversing a matrix

def spirallyTraverse(self,matrix, r, c):
        top=0
        left=0
        bottom=r-1
        right=c-1
        ans=[]
        while(top<=bottom and left<=right):
            """traverse from left to right on the top row"""
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            '''top to bottom on the right column'''
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            '''right to left on the bottom row'''
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            '''bottom to top on the left column''''
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans

'''T.C: O(mxn)
S.C: O(n)'''

#searching 2d array

 def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        row=0
        col=m-1
        while(row<n and col>=0):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False

    

#REVERSE PAIRS!!!!  optimal soln using merge sort

def merge(self,nums,l,m,r):
        temp=[]
        left=l
        right=m+1
        while(left<=m and right<=r):
            if(nums[left]<=nums[right]):
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while(left<=m):
            temp.append(nums[left])
            left+=1
        while(right<=r):
            temp.append(nums[right])
            right+=1
        for i in range(l,r+1):
            nums[i]=temp[i-l]       
    def mergeSort(self,nums,l,r):image.pngimage.png
        cnt=0
        if(l>=r):
            return cnt
        m=(l+r)//2
        cnt+=self.mergeSort(nums,l,m)
        cnt+=self.mergeSort(nums,m+1,r)
        cnt+=self.countPairs(nums,l,m,r)  ''' Modification'''
        self.merge(nums,l,m,r)
        return cnt
    def countPairs(self,nums, low, mid, high):
        right = mid + 1
        cnt = 0
        for i in range(low, mid + 1):
            while right<=high and nums[i]>2*nums[right]:
                right += 1
            cnt+=(right-(mid+1))  ''''to take the exact cnt '''
        return cnt
    def reversePairs(self, nums: List[int]) -> int:
        n=len(nums)
        return self.mergeSort(nums, 0, n - 1)

'''T.C: O(2nlogn)  S.C:O(n)'''

##Rotated Sorted Arrays'''

def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
                '''find sorted half'''
            if nums[low]<=nums[mid]:           '''left sorted'''
                if nums[low]<=target and target<=nums[mid]: '''search in left''' 
                    high=mid-1   '''found eliminate right'''
                else:
                    low=mid+1
            else:                 '''right sorted'''
                if nums[mid]<=target and target<=nums[high]: '''right sorted'''
                    low=mid+1                    '''if found eliminate left'''
                else:
                    high=mid-1
        return -1

T.C: O(logn) S.C:  O(1)

#if duplicates and arr[low]=arr[mid]=arr[high] shrink array and move to next element
'''before finding sorted array check this also'''
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low=low+1
                high=high-1
                continue
            
 #minimun in rotated sorted array

def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        ans=float('inf')
        while(low<=high):
            mid=(low+high)//2
            if nums[low]<=nums[mid]:  #left half sorted
                ans=min(ans,nums[low])
                low=mid+1           '''eliminate left half'''
            else:                         #right half sorted
                ans=min(ans,nums[mid])
                high=mid-1             '''eliminate right half'''
        return ans
                
#Peak Element in a 2D grid

def MaxElement(self,mat,n,m,mid):
        MaxValue=-1
        index=-1
        for i in range(0,n):
            if mat[i][mid]>MaxValue:
                MaxValue=mat[i][mid]  '''find max element in a column'''
                index=i
        return index
    
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        low=0
        high=m-1
        while(low<=high):    '''binary search to get the mid column'''
            mid=(low+high)//2
            row=self.MaxElement(mat,n,m,mid) '''find the row that has the max element in column mid'''
            left=mat[row][mid-1] if mid-1>=0 else -1 '''left elemnt of the max.element if there is still column else -1 as in the qn'''
            right=mat[row][mid+1] if mid+1<m else -1'''right elmt of max elmnt if there is col else-1'''
            
     '''compare max element with its neighbours'''   
            if mat[row][mid]>left and mat[row][mid]>right:
                return [row,mid]  '''compare the value if its greater return'''
            elif mat[row][mid]<left:
                high=mid-1     '''elif  go to left colmn'''
            else:
                low=mid+1      '''else go to right column'''
        return [-1,-1]            

'''T.C:  O(nlogm)  , S.C: O(1)  
        



