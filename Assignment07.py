# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Script that demonstrates exception handling and
#              pickling with short examples.
#              in "ToDoToDoList.txt" into a Python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RAyeni,11.14.2020,Created started script to complete Assignment 07
# ---------------------------------------------------------------------------- #

# Import modules

# os module is used to delete existing file.  Delete file will generate exception
# which is captured and handled.
import os
import pickle

# Data
# Declare variables and constants
demo_file_1 = "data1.dat"  # file to be referenced in exception demo
demo_pickle_file = "PickleDemo.dat"  # file to be created in pickle demo
demo_movie_file = "MovieRatings.dat"  # file to be created in pickle demo
menu_choice = "1"  # variable to capture user's selection from main menu
demo_item1 = ""  # element to be added to list_demo list object
demo_item2 = ""  # element to be added to list_demo list object
demo_item3 = ""  # element to be added to list_demo list object
pickle_object = None  # data in pickle format
movie = ""  # element in movie rating dictionary
movie_rating = ""  # element in movie rating dictionary
list_demo = []  # list of cars in pickle demo
dict_row = {}  # movie row (Title and Rating)
lst_table = []  # list of movies and their ratings


# Processing
class Processor:
    """ Contains Processing Functions """

    @staticmethod
    def demo_exception_handler(file_name):
        """ Demonstrates how exception handling works"""

        # deletes file to demonstrate exception handling
        if os.path.exists(file_name):
            os.remove(file_name)

        # exception handler
        try:
            open(file_name, "rb")
        except FileNotFoundError:  # Exception generates following message:
            print("\n[Custom Exception Message]: File is not present, skipping the reading process...\n")
            print("**************************************************************************************")
            print("* The above message is a custom exception that either allows the program to continue *")
            print("* execution or to exit gracefully, instead of exiting abruptly.                      *")
            print("**************************************************************************************")

    @staticmethod
    def add_data_to_list(element1, element2, element3, demo_list):
        """ Adds data to demo_list and returns it """

        demo_list = [element1, element2, element3]
        return demo_list

    @staticmethod
    def pickle_object_to_file(demo_list, demo_file):
        """ Pickles list and adds to file """

        input("\nPress [Enter] to pickle the list. ")
        print()  # whitespace
        f = open(demo_file, "wb")  # open binary file
        pickle.dump(demo_list, f)  # pickle list and write to file
        f.close()  # close file
        # create a pickle object (only to print to screen in demo)
        pk_object = pickle.dumps(demo_list)
        # print confirmation message
        print(f'The pickle list was written to {demo_file}. File will appear when demo quits. ')
        return pk_object

    @staticmethod
    def add_movie_rating(film, rating, list_of_rows):
        """ Adds movie and rating to dictionary as a row.
            Then adds dictionary to list (table).
        """

        # add movie and rating to dictionary
        row = {"Movie": film.strip().capitalize(), "Rating": rating.strip().capitalize()}
        # add row to table
        list_of_rows.append(row)
        return list_of_rows


# Presentation (Input/Output)

class IO:
    """ Contains Input and Output Tasks"""

    @staticmethod
    def print_menu_options():
        print("""
        Exception Handling and Pickling Demo

        Main Menu:
        1. Exception Handling Demo
        2. Pickling Demo
        3. Exception and Pickling Demo
        4. Quit
        """)
        print()

    @staticmethod
    def print_exception_pickling_intro():
        """ Print purpose of demo """

        print("************************************************************")
        print("* This demo will cover the use of exception handling,      *")
        print("* pickling, and saving data to a binary file.              *")
        print("************************************************************")

        #  Ask user to press Enter to continue
        input("\nPress [Enter] to continue: ")

    @staticmethod
    def input_demo_list_items():
        """Gets demo list items from user """

        print("*******************************************************")
        print("* Pickling is the process of converting an object to  *")
        print("* a stream of bytes (serialization) that can be saved *")
        print("* to disk.                                            *")
        print("*******************************************************")

        # Ask user to press Enter to continue with demo.
        input("\nPress [Enter] to continue: ")

        print("\n********************************************************")
        print("* In this demo we will create a three element list,    *")
        print("* pickle it, and save it to a binary file.             *")
        print("********************************************************")

        # Ask user to press Enter to continue with demo.
        input("\nPress [Enter] to continue: ")

        print("\n*******************************************************")
        print("* Let's create a list of three cars.                  *")
        print("*******************************************************")

        # Ask user to press Enter to continue with demo.
        input("\nPress [Enter] to continue: ")

        car1 = input("\nEnter the first car (ex. Volt, Prius, etc): ")
        car2 = input("Enter the second car (ex. Volt, Prius, etc): ")
        car3 = input("Enter the third car (ex. Volt, Prius, etc): ")

        return car1, car2, car3

    @staticmethod
    def input_movie(order):
        """ Gets movie and rating from user """

        film = input(f"\nEnter {order} movie: ")
        rating = input(f"Enter {order} movie's rating (ex. Excellent, Good, Fair, Bad): ")
        return film, rating


    @staticmethod
    def input_menu_choice():
        """ Gets menu choice from user """

        choice = str(input("Please make your selection [1, 2, 3, or 4]: ")).strip()
        print()  # white space
        return choice

    @staticmethod
    def input_press_enter_to_continue(message):
        input(message)

    @staticmethod
    def print_message(message):
        print("\n******************************************************")
        print(f'* {message}')
        print("******************************************************")

        # Ask user to press Enter to continue with demo.
        input("\nPress [Enter] to continue: ")

    @staticmethod
    def print_table(list_of_rows):
        """ Shows current rows in list object """

        print()
        print("*************************************************************")
        print("* Great. We now have two entries in our list object (table) *")
        print("*************************************************************")

        input("\nPress [Enter] to see the list object in list and table forms: ")
        print("\nList Form:")
        print()  # whitespace
        print(list_of_rows)
        print("\nTable Form:")
        print("\n**************** Movie Ratings *****************")
        for row in list_of_rows:
            print("* " + row["Movie"] + " (" + row["Rating"] + ")")
        print("************************************************")
        print()

        print("*************************************************************")
        print("* Next. Let's pickle the list object and save it to a file. *")
        print("*************************************************************")


    @staticmethod
    def show_pickle_object(pickle_list, non_pickle_list):
        """ Shows the user the pickle object created from list """

        print("\n******************************************************************")
        print("* Before we end the demo, let's see what both a pickled list and *")
        print("* non-pickled list look like                                     *")
        print("******************************************************************")

        # Ask user to press Enter to continue with demo.
        input("\nPress [Enter] to continue: ")

        #  print non-pickle list
        print("\nNon-pickle list:")
        print(non_pickle_list)

        print()

        # print pickle list
        print("Pickle list:")
        print(pickle_list)


# Main
while(True):
    IO.print_menu_options()
    menu_choice = IO.input_menu_choice()

    if menu_choice.strip() == "1": # Exception Handling Demo
        Processor.demo_exception_handler(demo_file_1)
        IO.input_press_enter_to_continue("\nPress the [Enter] key to return to Main Menu: ")
        continue

    if menu_choice.strip() == "2":  # Pickling Demo
        demo_item1, demo_item2, demo_item3 = IO.input_demo_list_items()
        list_demo = Processor.add_data_to_list(demo_item1, demo_item2, demo_item3, list_demo)
        Processor.pickle_object_to_file(list_demo, demo_pickle_file)
        IO.input_press_enter_to_continue("\nPress the [Enter] key to return to Main Menu: ")
        continue

    if menu_choice.strip() == "3":  # Exception and Pickling Demo
        # Print demo purpose
        IO.print_exception_pickling_intro()
        # Trigger exception and its handling
        Processor.demo_exception_handler(demo_movie_file)
        # Instruct user to press Enter to continue
        IO.input_press_enter_to_continue("\nPress the [Enter] key to continue: ")
        # Print instruction
        IO.print_message("Let's enter a two movie ratings.")
        # Have user enter movie and rating
        movie, movie_rating = IO.input_movie("the first")
        # Add movie and rating to table
        Processor.add_movie_rating(movie, movie_rating, lst_table)
        # Have user enter movie and rating
        movie, movie_rating = IO.input_movie("the second")
        # Add movie and rating to table
        Processor.add_movie_rating(movie, movie_rating, lst_table)
        # Show table
        IO.print_table(lst_table)
        # pickle list object and save to binary file
        pickle_object = Processor.pickle_object_to_file(lst_table, demo_movie_file)
        # show pickle list object
        IO.show_pickle_object(pickle_object, lst_table)

    if menu_choice.strip() == "4":
        break

