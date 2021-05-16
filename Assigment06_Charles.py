# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# CTUNG, 5.15.2021,Modified code to complete assignment 6.  Add functions
# To Read and Write CSV Text File (ToDoList.txt) with Task and Priority,
# Add Task to List, and Remove Task from Dictionary of Lists, Add Callouts
# To Main Body of Script Calling out Functions
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoList.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_dictionary_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_dictionary_rows = []
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Task": data[0].strip(), "Priority": data[1].strip()}
            list_of_dictionary_rows.append(row)
        file.close()
        return list_of_dictionary_rows, 'Success'

    @staticmethod
    def add_data_to_list(list_of_dictionary_rows, task, priority):
        """Adds data to a list of dictionary row
        :param list_of_dictionary_rows" (list) of dictionary adding data to it
        :param task: (string) with name of task
        :param priority: (string) with name of priority
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        list_of_dictionary_rows.append(row)

    @staticmethod
    def remove_data_from_list(list_of_dictionary_rows, strKeyToRemove):
        """Removes data from a list of dictionary rows
        :param list_of_dictionary_rows: (list) of dictionary rows removing from it
        :param strKeyToRemove: Task to Remove
        :return: Revised list of dictionary rows
        """

        sucess_status = False
        row_number = 0
        for row in list_of_dictionary_rows:
            task, priority = row.values()
            #why does this not work
            if task == strKeyToRemove:
                del lstTable[row_number]
                sucess_status = True
            row_number += 1
        return list_of_dictionary_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Add Code Here!
        f = open(file_name, "w")
        for row in list_of_rows:
            f.write(str(row["Task"]) + ',' + str(row["Priority"] + '\n'))
        f.close()
        print("now in file!")
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(lstTable):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        print(lstTable)
        for row in lstTable:
              print(row)
              print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """Gets data for a dictionary rows
        :return: (tuple) of string with tasks and priority
        """

        task = str(input("What is the task? -")).strip()
        priority = str(input("What is the priority? [high|low] - ")).strip()
        print()  # Add an extra lin for looks
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """Gets a task from the user to remove
        :return: (string) task to remove
        """
        task = str(input("What task would you like to remove? - ")).strip()
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
lstTable, status = Processor.read_data_from_file(strFileName)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Adds a New Tasks
        tplData = IO.input_new_task_and_priority()   # Outputs Tuple with New Task & Priority
        Processor.add_data_to_list(lstTable, tplData[0], tplData[1])   # Adds Data to List
        IO.print_current_Tasks_in_list(lstTable)
        print("Added New Task Successfully")
        continue  # to show the menu

    elif strChoice == '2':  # Removes an Existing Task
        strKeyToRemove = input("Which Task would you like removed?-")
        blnItemRemoved = Processor.remove_data_from_list(lstTable, strKeyToRemove)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)   # Writes Data to File
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable.clear()
            lstTable, status = Processor.read_data_from_file(strFileName) #Outputs List and Sucess
            IO.print_current_Tasks_in_list(lstTable)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
