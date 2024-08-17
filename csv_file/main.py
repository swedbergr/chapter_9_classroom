def read_file(file_name):
  '''
  Function takes a string filename, reads the data from a csv file, 
  and then returns a two-dimensional list.
  param file_name: string for csv file
  return: two-dimensional list of data from file
  '''
  # Define list 
  data = []

  # Open file and read data into list
  try:
    with open(file_name, "r") as infile:
      # Read whole file as one string and split by \n into list
      students = infile.read().split("\n")
  except FileNotFoundError:
    print("No file exists with that name. Please try again.")
  else:
    # Iterate through every line
    for student in students:
      # Split data in each line into list by , and append to data
      data.append(student.split(","))

  # Return data list
  return data


def calculate_average(data):
  '''
  Function takes a two-dimensional list, calculates the average of each
  element and returns a list of averages for each element.
  param data: two-dimensional list
  return: list of averages
  '''
  # Define average list
  average = []

  # Iterate through lists in data
  for nums in data:
    total = 0
    for num in nums:
      total += int(num)

    average.append(total / len(nums))

  # Return average
  return average


def main():
  # Display purpose
  print("This program will take a csv file and calculate the average of each row.")
  # Get file name from user
  file_name = input("Enter the file name: ")
  # Get data as a list from file
  data = read_file(file_name)
  # Validate file name
  while len(data) == 0:
    file_name = input("Enter the file name: ")
    data = read_file(file_name)

  # Calculate averages into list
  averages = calculate_average(data)

  # Display averages
  row = 1
  for average in averages:
    print(f"Row {row}: {average}")
    row += 1


if __name__ == "__main__":
  main()