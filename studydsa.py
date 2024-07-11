#1.isprime

class Solution:
    def isPrime (self, N):
        if(N==1):
            return(0)
        for i in range(2,N):
            if(N%i==0):
                return 0
        return 1
N=int(input('enter the number'))
solution=Solution()
result=solution.isPrime(N)
print(result)

#2.palindrome

s=input('enter the string')
def ispalindrome(s: str)->bool:
    n=len(s)
    for i in range(0,n//2):
        if s[i]!=s[n-1-i]:
            return False
    return True
print(ispalindrome(s))

#3.lcm and gcd

import math
class Solution:
    def lcmAndGcd(self, A , B):
        return abs(A*B)//math.gcd(A,B),math.gcd(A,B)

#4.count of perfect squares less than N

    import math
class Solution:
    def countSquares(self, N):
        count=0
        for i in range(1,N):
            root=int(math.sqrt(i))
            if root*root==i:
                count+=1
        return count

#or to remove tle error(optimal)

import math
class Solution:
    def countSquares(self, N):
        root=int(N**0.5)
        return root-1 if root*root==N else root
    (#here for large numbers we have to consider the perfect square or not condn)


#5.no. of digits evenly divides N

    class Solution:
    def evenlyDivides (self, N):
        count=0
        number=str(N)
        n=len(number)
        for i in range(1,n):
            for i in number:
                if int(i)!=0 and N%int(i)==0:
                    count+=1
            return count

#6.palindrome

n=int(input('enter no'))
num=str(n)
N=len(num)
sum=0
for i in range(N):
    a=int(num[i])
    sum+=pow(a,3)
print(sum)
if sum==n:
    print("Yes")
else:
    print("No")

#or
    k=n%100
        k1=k%10
        n1=n//100
        n2=k//10
        j=k1**3+n1**3+n2**3
        if(j==n):
            return "Yes"
        else:
            return "No"

        
#7.multiplication table of a number printed in single row
class Solution:
    def getTable(self,N):
        return [N*i for i in range(1,11)]
    

#8.print second largest element  and print -1 if second largest dosnt exist

    class Solution:
	def print2largest(self,arr, n):
	    if n<2:
            return -1
        else:
            largest=secondlargest=float('-inf')
            for num in arr:
                if num>largest:
                    secondlargest=largest
                    largest=num
                elif num>secondlargest and num!=largest:
                    secondlargest=num
            if secondlargest==float('-inf') or secondlargest==largest:
                return -1
            else:
                return secondlargest


# 9.to reverse the equation
            class Solution:
    def reverseEqn(self, s):
        stk = []
        current = ""
        for c in s:
            if c.isalnum():
                current += c
            else:
                if current:
                    stk.append(current)
                    current = ""
                    stk.append(c)
        if current:
            stk.append(current)
        return ''.join(stk[::-1])


#SET
list1=[1,2,3,2,2,1,1,3,4]
set1=set(list1)
print(set1)
print(type(set1))
set2=set()
for i in range(0,9):
    set2.add(list1[i])
print(set2)

#10.remove duplicates in sorted array
def removeDuplicates(arr: list[int]) -> int:
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    k = len(st)
    print(k)
    j = 0
    for x in st:
        arr[j] = x
        j += 1
    return k


arr = [1, 1, 2, 2, 2, 3, 3]
k = removeDuplicates(arr)
print("The array after removing duplicate elements is ")
for i in range(k):
    print(arr[i], end=" ")


#11.move zeroes to end


nums=[0,1,0,3,12]

def moveZeroes(nums):
    j=-1
    n=len(nums)
    for i in range(0,n):
        if(nums[i]==0):
            j=i
            break
    if j==-1:
        return nums
                
    for i in range(j+1,n):
        if(nums[i]!=0):
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
            
    return nums
ans=moveZeroes(nums)
for it in ans:
    print(it,end=' ')
print()


#12.STRINGS

def removeOuterParentheses(s: str) -> str:
    stack = []
    result = []
    primitive = []

    for char in s:
        if char == '(':
            if stack:
                primitive.append(char)
            stack.append(char)
        else:
            stack.pop()
            if stack:
                primitive.append(char)
            else:
                result.append(''.join(primitive))
                primitive = []

    return ''.join(result)

def removeOuterParentheses(s: str) -> str:
    stack = []
    result = []
    primitive = []

    for char in s:
        if char == '(':
            if stack:
                primitive.append(char)
            stack.append(char)
        else:
            stack.pop()
            if stack:
                primitive.append(char)
            else:
                result.append(''.join(primitive))
                primitive = []

    return ''.join(result)

def removeOuterParentheses(s: str) -> str:
    stack = []
    result = []
    primitive = []

    for char in s:
        if char == '(':
            if stack:
                primitive.append(char)
            stack.append(char)
        else:
            stack.pop()
            if stack:
                primitive.append(char)
            else:
                result.append(''.join(primitive))
                primitive = []

    return ''.join(result)










    
