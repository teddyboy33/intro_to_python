#!/usr/bin/env python3

'''
hw5.py
Created by Philip Korte

dependancies
 - python3x

runtime
 - python3 hw5.py
'''

# open file
infile = "./ToDo.txt"
with open(infile, 'r') as file:
    lines = file.readlines() # import each line into a list

# create an empty dictionary to store our data
task_dict = {}

# loop through list, creating a key/value pair and put them in dictionary
for line in lines:
    task = line.split(',')[0].strip()
    priority = line.split(',')[1].strip()
    task_dict[task] = priority

while True:
    print(
    """
Menu of Options
    
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save data to file
    5) Exit program
    """
    )
    choice = input("Which option would you like to choose? ")
    print()

    # list the dictionary
    if choice == '1':
        print("Task - Priority")
        print("---------------")
        for key, value in task_dict.items():
            print(key, "-", value)

    # add a new item to dictionary
    elif choice == '2':
        item = input("What is the task you wish to add? ")
        item = item.title() # convert to title case to match dictionary key
        priority = input("What is the priority for " + item + "? ")
        # if item is not in the list, add it
        if item not in task_dict:
            task_dict[item] = priority
            print(item.title(), "was added to your ToDo dictionary.")
        # if item is in the list ask to update it
        else:
            already_exists = input(item + " is already in your ToDo file. Would you like to update it's priorty? ")
            if already_exists.lower()[0] == 'y':
                task_dict[item] = priority
            else:
                print(item, "was not updated.")

    # remove existing item from dictionary
    elif choice == '3':
        item = input("What task do you wish to remove? ")
        item = item.title() # convert to title case to match dictionary key
        if item in task_dict:
            del task_dict[item]
            print(item, "has been deleted from your ToDo dictionary.")
        else:
            print("{0} is not in your ToDo list.".format(item))

    # save your dictionary to text file
    elif choice == '4':
        with open(infile, 'w') as file:
            for key, value in task_dict.items():
                file.write("{0},{1}\n".format(key,value))
            print("Your ToDo.txt file has been updated.")

    # exit program
    elif choice == '5':
        print("This concludes your homework session. Good-bye.")
        break

    # just in case user can't read instructions
    else:
        print("Please pick a valid option from the menu. ")
      #  continue