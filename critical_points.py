class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next:
            return [-1,-1]
        critical_points=[]
        #critical points exists only if there is prev and next value for a node
        prev=head
        current=head.next
        index=0
        while current.next:
            if (current.val > prev.val and current.val > current.next.val) or (current.val < prev.val and current.val < current.next.val):
                critical_points.append(index)
                #print(critical_points)
                
            prev=current
            current = current.next
            index += 1
            #print(index)
    
        if len(critical_points) < 2:
            return [-1, -1]
    
        min_distance = float('inf')
        
        #To find max and min distance between critical points
        for i in range(len(critical_points) - 1):
            distance = critical_points[i + 1] - critical_points[i]
            min_distance = min(min_distance, distance)
        max_distance=critical_points[-1] - critical_points[0]
        print([min_distance, max_distance])

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next.next = ListNode(7)
O=Solution()
O.nodesBetweenCriticalPoints(head)



        
