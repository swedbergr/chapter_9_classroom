# List of integers to become the keys of the dictionary
ints = [1, 2, 3, 4, 5]

# Use a dictionary comprehension to creat a dictionary with each int and its square
#squares = {}
#for num in ints:
  #squares[num] = num * num

squares = {num: num * num for num in ints if num % 2 == 0}

# Display squares
print(squares)