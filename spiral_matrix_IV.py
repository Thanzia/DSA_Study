class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generate_spiral_matrix(m, n, head):
    # Initialize the matrix with -1
    matrix = [[-1 for _ in range(n)] for _ in range(m)]
    
    # Directions represent right, down, left, up (in clockwise order)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Boundary initialization
    top, bottom, left, right = 0, m - 1, 0, n - 1
    direction = 0  # Start by moving right
    i, j = 0, 0  # Start at top-left corner
    
    # Traverse the linked list
    curr = head
    while curr:
        matrix[i][j] = curr.val
        curr = curr.next
        
        # Calculate the next position
        ni, nj = i + directions[direction][0], j + directions[direction][1]
        
        # Check if the next position is within the current boundary
        if ni < top or ni > bottom or nj < left or nj > right:
            # Change direction if the next step is out of bounds
            if direction == 0:  # Moving right
                top += 1
            elif direction == 1:  # Moving down
                right -= 1
            elif direction == 2:  # Moving left
                bottom -= 1
            elif direction == 3:  # Moving up
                left += 1
            direction = (direction + 1) % 4
        
        # Update the current position
        i += directions[direction][0]
        j += directions[direction][1]
    
    return matrix

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)

        Example 1:


        current = current.next
    return dummy.next

# Example usage:
# Create a linked list with values [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
head = create_linked_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
m, n = 3, 5
matrix = generate_spiral_matrix(m, n, head)

for row in matrix:
    print(row)
v
