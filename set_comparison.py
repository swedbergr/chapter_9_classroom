# Sample set
set1 = set([1, 2, 3, 4, 5])

# Create set2 as a comprehesion of set1
set2 = {item * item for item in set1 if item > 2}

print(set2)