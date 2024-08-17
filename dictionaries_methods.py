# Create a sample dictionary
students = {"Chris": "555-1111", "Katie": "555-2222", "Joanne": "555-3333"}

# Use a dictionary method
new = {}
for x, y in students.items():
  new[x] = y

for key in students:
  print(key + ": " + students[key])