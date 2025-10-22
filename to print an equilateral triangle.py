# Program to print an equilateral triangle using nested loops

# take input for size of the triangle
n = int(input("Enter the size of the triangle: "))

# outer loop for rows
for i in range(1, n + 1):
    # print spaces before stars
    for j in range(n - i):
        print(" ", end="")
    # print stars with a space after each
    for k in range(2 * i - 1):
        print("*", end="")
    # move to the next line after each row
    print()
