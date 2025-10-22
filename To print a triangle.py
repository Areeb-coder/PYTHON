n = int(input("Enter the size of the triangle: "))

# outer loop for rows
for i in range(1, n + 1):
    # inner loop for columns (printing stars)
    for j in range(i):
        print("*", end=" ")
    # move to the next line after each row
    print()