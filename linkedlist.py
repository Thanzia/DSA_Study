#node creation
'''a class node of data and next which stores address of next node
here next is empty.many nodes can be ceated by using the same class'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
newnode1=Node(5)
newnode2=Node(6)
newnode3=Node(7)
newnode4=Node(8)
newnode5=Node(3)
print(newnode1.data)
print(newnode2.data)
print(newnode3.data)
print(newnode4.data)
print(newnode5.data)

#link 2 nodes
'''2 nodes ccan be linked by giving the next of first node
as the name of the second'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(3)
n2=Node(6)
n3=Node(7)
print(n2)
n1.next = n2
n1.next.next = n3
print(n1.next)
print(n1.next.next)
print(n1.next.data)
print(n1.next.next.data)
'''print(n1.data ,end = "->")
print(n1.next.data,end = "->")
print(n1.next.next.data)'''

 #create a basic linkedlist
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
O = Linkedlist()
print(O)

#to convert an array to linkedlist and traverse
#thru array,find length,search element

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=newnode
            
  """to traverse thru the array T.C: O(n)"""         
    def display(self):
        cnt=0
        temp=self.head
        while(temp):
            print(temp.data,end="->")
            cnt+=1
            temp=temp.next
        print("Null")  """to end the list"""
        print(cnt)

"""to check whether an element is present or not  T.C:O(n)"""
        
    def is_present(self,value):
        temp=self.head
        while(temp):
            if temp.data==value:
                return 1
            temp=temp.next
        return 0

def arr_to_linkedlist(arr):
    l1=Linkedlist()   """an object to class Linkedlist"""
    for item in arr:
        l1.insert_at_end(item)
    return l1

arr=[1,2,3,4,5]
l1=arr_to_linkedlist(arr)
l1.display()
print(l1.is_present(5))

#pbm: merge k sorted lists

''' Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next  (refer notes)'''

class Solution:
    def merge2lists(self,head1,head2):
        t1=head1
        t2=head2
        dummy=ListNode(-1)
        temp=dummy

        while(t1 is not None and t2 is not None):
            if t1.val < t2.val:
                temp.next=t1
                temp=t1
                t1=t1.next
            else:
                temp.next=t2
                temp=t2
                t2=t2.next
        if t1:
            temp.next=t1
        else:
            temp.next=t2
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        head=lists[0]
        for i in range(1,len(lists)):
            head=self.merge2lists(head,lists[i])
        return head
        

