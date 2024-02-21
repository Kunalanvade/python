def multiplication_table(size):
    # Print the column headers
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()
    
    # Print the separator
    print("   ", end="")
    print("-" * (4 * size))
    
    # Print the rows of the table
    for i in range(1, size + 1):
        print(f"{i:2} |", end="")
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()

# Ask the user for input
size = int(input("Enter the size of the multiplication table: "))

# Print the multiplication table
multiplication_table(size)
