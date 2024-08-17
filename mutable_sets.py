# Create sets to manipulate
set1 = set([1, 2, 3])
set2 = set([4, 5, 6])

# Use the update method
set1.update(set2)
print(set1)
print(set2)

# Use the add method
set1.add(7)
print(set1)

# Use the discard and remove methods
set1.remove(7)
set1.discard(6)
print(set1)

# Demonstrate bad arguments
set1.discard(10)
print(set1)

# Demonstrate clear method
set1.clear()
print(set1)