def main():
  # Define menu
  print("--Birthday Holder--")

  # Get previously saved birthdays
  birthdays = get_birthdays()
  
  # Iterate as long as user wants to run program
  while True:
    print("What would you like to do?",
         "\n1. Add new birthday",
         "\n2. Look up friend's birthday",
         "\n3. Delete a birthday,",
         "\n4. Quit")
    choice = input()
    # Navigate choices
    if choice == "1":
      birthdays = add_birthday(birthdays)
    elif choice == "2":
      look_up_birthday(birthdays)
    elif choice == "3":
      birthdays = delete_birthday(birthdays)
    elif choice == "4":
      save_birthdays(birthdays)
      break
    else: 
      print("That is not a valid option. Please try again.")


def get_birthdays():
  '''
  Function opens a csv file and returns a dictionary 
  of birthdays where the keys are first names
  and the values are dates as strings.
  return: dictionary of name: date as strings
  '''
  # Define dictionary for birthdays
  birthdays = {}

  # Open file to read in birthdays if it exists
  try:
    with open("birthdays.csv", "r") as infile:
      # Get data as a list by lines without \n
      data = infile.read().split("\n")

      # Iterate through data to create two-dimensional list
      persons = []
      i = 0
      while data[i] != "":
        persons.append(data[i].split(","))
        i += 1

      # Iterate through list to create dictionary
      for person in persons:
        birthdays[person[0]] = person[1]
  except FileNotFoundError:
    print("There are no saved birthdays.")

  # Return brithdays dictionary
  return birthdays


def add_birthday(birthdays):
  '''
  Function takes a current dictionary of birthdays and then
  prompts the user for a new friend's birthday, updates
  the dictionary if the name is not already a key, and 
  then returns the updated dictionary.
  param birthdays: dictionary as name: birthday as strings
  return: dictionary as name: birthday as strings
  '''
  # Prompt user for information
  name = input("Name: ")
  birthday = input("Birthday: ")
  # Check if key exists
  if name in birthdays.keys():
    # Warn user key exists
    print(f"Whoa there buddy, you already have a friend named {name}.")
    question = input("Do you want to change the name? (y or n)")
    # Get a new name
    if question.lower() == 'y':
      name = input("Name: ")

  # Add data to the dictionary
  birthdays[name] = birthday

  # Return dictionary
  return birthdays



def look_up_birthday(birthdays):
  '''  
  Void function takes a current dictionary of birthdays and then
  promps the user for a name to use as a key to look up the value.
  Function then displays the birthday if the key exists.
  param birthdays: dictionary as name: birthday as strings
  '''
  # Ask the user which key
  name = input("Name: ")

  # Check for name in the dictionary
  if name in birthdays.keys():
    print(birthdays[name])
  else:
    print("That name does not have a stored birthday.")



def delete_birthday(birthdays):
  '''
  Function takes a dictionary of birthdays, prompts the user for
  a key to delete the whole element, then returns an updated
  dictionary if the key exists.
  param birthdays: dictionary as name: birthday as strings
  return: dictionary as name: birthday as strings
  '''
  # Ask the user which key
  name = input("Name: ")

  # Check for name in the dictionary
  if name in birthdays.keys():
    del birthdays[name]
  else: 
    print("There is not birthday assigned to that name.")

  # Return dictionary
  return birthdays
  


def save_birthdays(birthdays):
  '''
  Void function takes a dictionary of birthdays and saves them
  to a csv file.
  param birthdays: dictionary as name: birthday as strings
  '''
  # Open file
  with open("birthdays.csv", "w") as outfile:
    for name, birthday in birthdays.items():
      outfile.write(name + "," + birthday + "\n")



if __name__ == "__main__":
  main()