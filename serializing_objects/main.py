# Import module
import pickle

def pickle_data():
  '''
  Void function pickles a dictionary data type to a file.
  '''
  # Create dictionary object
  phonebook = {"Chris": "555-1111", 
               "Katie": "555-2222", 
               "Joanne": "555-3333"}
  
  # Open file for writing bytes
  with open("phonebook.dat", "wb") as outfile:
    pickle.dump(phonebook, outfile)


def retrieve_data():
  '''
  Function retrieves pickled data from a file and returns
  it as its original file type.
  return: file type retrieved from pickled file
  '''
  # Open file
  with open("phonebook.dat", "rb") as infile:
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
    elif choice == "3":
      break
    else:
      print("That is not a valid response. Please try again.")


if __name__ == "__main__":
  main()