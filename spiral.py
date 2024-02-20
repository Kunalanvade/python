def spiral_pattern(n):
    # Creating an empty n x n matrix filled with zeros
    matrix = [[0] * n for _ in range(n)]

    # Define the initial values
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    # Loop to fill the matrix in a spiral pattern
    while top <= bottom and left <= right:
        # Fill the top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Fill the rightmost column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Fill the bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Fill the leftmost column
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    # Print the spiral pattern
    for row in matrix:
        print(" ".join(map(str, row)))

# Example usage
spiral_pattern(5)
