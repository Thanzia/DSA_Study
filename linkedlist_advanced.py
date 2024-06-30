class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode


    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=newnode

    def delete_firstnode(self):
        temp=self.head
        self.head=temp.next
        del(temp)

    def delete_lastnode(self):
        temp=self.head
        while(temp.next):
            lss=temp
            temp=temp.next
            ls=lss.next
            if ls.next==None:
                lss.next=None
        del(temp)

    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end="->")
            temp=temp.next
        print("Null")

    def insert_at_middle(self,data,pos):
        newnode1=Node(data)
        temp=self.head
        pos_temp=1
        while(temp.next):
            middle=temp
            temp=temp.next
            if pos-pos_temp==1:
                middle.next=newnode1
                newnode1.next=temp
                return    
            else:
                pos_temp+=1

    def delete_at_middle(self,pos):
        temp=self.head
        pos_t=1
        while(temp.next):
            middle=temp
            temp=temp.next
            tbd=temp
            if pos_t+1==pos:
                middle.next=temp.next
                del(tbd)
                return
            else:pos_t+=1
        

    def is_present(self,value):
        temp=self.head
        while(temp):
            if temp.data==value:
                return 1
            temp=temp.next
        return 0

l1=Linkedlist()
l1.insert_at_beginning(5)
l1.insert_at_beginning(4)            
l1.insert_at_beginning(3)    
l1.insert_at_beginning(2)
l1.insert_at_beginning(1)
l1.insert_at_end(6)
l1.insert_at_end(7)
l1.insert_at_end(8)
l1.insert_at_end(9)
l1.insert_at_middle(10,4)
l1.display()
l1.delete_at_middle(4)
l1.display()
l1.delete_firstnode()
l1.delete_lastnode()
l1.display()

#reversal in linked list
# Node Class
#brute force  tc:O(2n)  s.c:O(n)
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    #Function to reverse a linked list
    def reverseList(self, head):
        temp=head
        stack=[]
        while(temp):
            stack.append(temp.data)
            temp=temp.next
        temp=head
        while(temp):
            temp.data=stack[-1]
            stack.pop()
            temp=temp.next
        return head

#better t.c: O(n) s.c: O(1)
def reverseList(self, head):
        temp=head
        previous=None
        while(temp):
            front=temp.next
            temp.next=previous
            previous=temp
            temp=front
        return previous

#delete nth node from end of ll

# Definition for singly-linked list.
#T.C: O(len) S.C:O(1)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head  #fast traverse through n steps
        slow=head  #slow starts traversing after fast takes n move
        
        for i in range(n):
            fast=fast.next
        if not fast:
            return head.next
        #once fast reaches end slow reaches n-1 slow.next points to delnode
        while(fast.next):
            slow=slow.next
            fast=fast.next
        delnode=slow.next
        slow.next=slow.next.next
        del delnode
        return head
        
#middle of a linkedlist

class Solution:
    
    def findMid(self, head):
        #tortoise hare algo T.C:O(n/2) S.C:O(1)
        slow=head
        fast=head
        #slow traverse by 1 and fast traverse by 2 so that fast reaches 1
        #slow reach middle for odd exact middle for even the second middle
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow.data

#detect looop in LL

class Solution:
    #tortiose hare algorithm slow moves by 1 & fast by 2 T.C:O(n),S.C:O(1)
    #slow & fast collides if there is a loop
    def detectLoop(self, head):
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

#intersection of 2 nodes

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==None and headB==None:
            return None
        t1=headA
        t2=headB
        while(t1!=t2):
            t1=t1.next
            t2=t2.next
            if t1==t2:
                return t1
            if t1==None:
                t1=headB
            if t2==None:
                t2=headA
        return t1

#union of 2 LL

class Solution:
    
    def union(self, head1,head2):
        st=set()
        t1=head1
        t2=head2
        while(t1):
            st.add(t1.data)
            t1=t1.next
        while(t2):
            st.add(t2.data)
            t2=t2.next
        sorted_list=sorted(st)
        
        union_list=linkedList()
        for i in sorted_list:
            union_list.insert(i)  #fn defined inthe driver code elsewrite 
        return union_list.head

#sortlist in LL Brute Force approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp=head
        arr=[]

        while(temp):
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        temp=head
        while(temp):
            for i in arr:
                temp.val=i
                temp=temp.next
            return head

#rotate linked list

class Solution:
    def findnthnode(self,temp,k):
        cnt=1
        while(temp):
            if cnt==k:
                return temp
            cnt+=1
            temp=temp.next
        return temp
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=1
        if not head or k==0:
            return head
        #calculate length of LL
        tail=head
        while(tail.next):
            length+=1
            tail=tail.next
        #round k to avoid over rotation
        if k%length==0:
            return head
        k=k%length
        #now tail points to last make it as newhead
        tail.next=head
        newlastnode=self.findnthnode(head,length-k)
        head=newlastnode.next
        newlastnode.next=None
        return head
