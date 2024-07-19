#i wrote all dese lines to generate lucky numbers in matrix but found the result in
#single line  result printed for both separated by a dotted line

def luckyNumbers(matrix):
    if not matrix:
        return []
    
    min_in_rows = [float("inf")]*len(matrix)
    max_in_cols = [float("-inf")]*len(matrix[0])

    # Find the minimum in each row
    for i in range(len(matrix)):
        min_in_rows[i] = min(matrix[i])

    # Find the maximum in each column
    for j in range(len(matrix[0])):
        max_in_cols[j] = max(matrix[i][j] for i in range(len(matrix)))

    lucky_numbers = []

    # Check for lucky numbers
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == min_in_rows[i] and matrix[i][j] == max_in_cols[j]:
                lucky_numbers.append(matrix[i][j])

    return lucky_numbers
matrix = [
    [3, 7, 8],
    [9, 11, 13],
    [15, 16, 17]
]



print(luckyNumbers(matrix))
print('...............')
print(list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)}))
#find min in row first and make transpose of col so that it turns out to be row
#and find max and do intersection of both list
