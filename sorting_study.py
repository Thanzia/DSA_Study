                #sorting

            #merge sort

arr=list(input('enter the list'))
l=0
r=len(arr)-1



def merge(arr,l,m,r):
    temp=[]
    left=l
    right=m+1
    while(left<=m and right<=r):
        if(arr[left]<=arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=m):
        temp.append(arr[left])
        left+=1
    while(right<=r):
        temp.append(arr[right])
        right+=1
    
    for i in range(l,r+1):
        arr[i]=temp[i-l]
           
def mergeSort(arr,l,r):
    if(l>=r):
        return
    m=(l+r)//2
    mergeSort(arr,l,m)
    mergeSort(arr,m+1,r)
    merge(arr,l,m,r)
    return arr
print(mergeSort(arr,l,r))


      #selection sort


arr=[9,46,24,52,20,13]
n=len(arr)

def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]
def selectionsort(arr,n):
    for i in range(0,n-1):
        min=i
        for j in range(i,n):
            if(arr[j]<arr[min]):
                min=j
            swap(arr,min,i)
    return arr
print(selectionsort(arr,n))

