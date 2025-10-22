size = int(input("Enter the size of the heart: "))

for row in range(size // 2, size, 2):
    for space in range(1, size - row, 2):
        print(" ", end="")
    for col in range(row):
        print("*", end="")
    for space in range(1, size - row + 1):
        print(" ", end="")
    for col in range(row):
        print("*", end="")
    print()

for row in range(size, 0, -1):
    for space in range(size - row):
        print(" ", end="")
    for col in range(row * 2 - 1):
        print("*", end="")
    print()
print("Ayaan and Faijal")