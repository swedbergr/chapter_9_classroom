# Sample sets
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])

# Demonstrate the union of set1 and set2
set3 = set1.union(set2)
print(set3)

# Demonstrate the intersection of set1 and set2
set4 = set1.intersection(set2)
print(set4)

# Demonstrate the difference of sets
set5 = set1.difference(set2)
print(set5)

# Demonstrate the semetric difference
set6 = set2.symmetric_difference(set1)
print(set6)

# Demonstrate subsets
value = set1 >= set4
print(value)