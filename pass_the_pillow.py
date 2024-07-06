
def passThePillow(n: int, time: int) -> int:
    index = 1  # Start with the first person holding the pillow
    direction = 1  # Initial direction: 1 (moving to the right)
    for _ in range(time):
        index += direction  # Move to the next person
        # Check if we reach either end of the line
        if index == 0:
            index = 2  # Move from person 1 to person 2
            direction = 1  # Change direction to right
        elif index == n + 1:
            index = n - 1  # Move from person n to person n-1
            direction = -1  # Change direction to left
    return index
print(passThePillow(4,5))   
