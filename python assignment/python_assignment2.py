# question1
rows = 5

# Outer loop will print the number of rows
for i in range(0, rows):
    # This inner loop will print the stars
    for j in range(0, i + 1):
        print("*", end=' ')
        # Change line after each iteration
    print(" ")
# For second pattern
for i in range(rows , 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

# question2
word=input("enter a word")
print(word[::-1])