class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next:
            return [-1,-1]
        critical_points=[]
        current=head
        index=1
        while current and current.next:
            if current.val < current.next.val > (current.next.next.val if current.next.next else float('-inf')):
                critical_points.append(index+1)
                print(critical_points)
            elif current.val> current.next.val<(current.next.next.val if current.next.next else float('inf')):
                critical_points.append(index+1)
                #print(critical_points)
            current = current.next
            #print(current)
            index += 1
            #print(index)
    
        if len(critical_points) < 2:
            return [-1, -1]
    
        min_distance = float('inf')
        max_distance = float('-inf')
        print(critical_points)
        for i in range(len(critical_points) - 1):
            distance = critical_points[i + 1] - critical_points[i]
            min_distance = min(min_distance, distance)
            max_distance = max(max_distance, distance)
        print([min_distance, max_distance])

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next = ListNode(6)
O=Solution()
O.nodesBetweenCriticalPoints(head)



        
