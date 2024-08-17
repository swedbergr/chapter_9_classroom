# Import module
import pickle

def pickle_data():
  '''
  Void function pickles a dictionary data type to a file.
  '''
  # Create list of ints
  nums = [5, 6, 7, 8, 9]

  # Open file for writing bytes
  with open("nums.dat", "wb") as outfile:
    pickle.dump(nums, outfile)


def retrieve_data():
  '''
  Function retrieves pickled data from a file and returns
  it as its original file type.
  return: file type retrieved from pickled file
  '''
  # Open file
  with open("nums.dat", "rb") as infile:
    data = pickle.load(infile)

  return data


def main():
  while True:
    print("What would you like to do?",
        "\n1. Pickle data",
        "\n2. Retrieve pickled data",
        "\n3. Quit")
    choice = input()
    if choice == "1":
      pickle_data()
    elif choice == "2":
      data = retrieve_data()
      print(data)
      avg = sum(data) / len(data)
      print(avg)
    elif choice == "3":
      break
    else:
      print("That is not a valid response. Please try again.")


if __name__ == "__main__":
  main()