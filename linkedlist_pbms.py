'''Linked list pbms'''

'''pbm1: split linked list into parts'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the length of the linked list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
    
        # Step 2: Determine the size of each part
        part_size = length // k
        remainder = length % k
    
        # Step 3: Split the list into k parts
        parts = []
        current = head
    
        for i in range(k):
            # Calculate size for this part
            size = part_size + (1 if i < remainder else 0)
            if size == 0:
                parts.append(None)
                continue
        
            # Initialize the head of the current part
            part_head = current
            prev = None
        
            # Move `size` nodes into the current part
            for _ in range(size):
                prev = current
                current = current.next
        
            # Disconnect the current part from the rest of the list
            if prev:
                prev.next = None
        
            # Append the current part to the result list
            parts.append(part_head)
    
        return parts
