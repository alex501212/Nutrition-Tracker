TIME = []
MTYPE = []
DESC = []
SERVING = []
KCAL = []
SFATg = []  # emtpy lists for food record values


def open_read():
    # open and close file
    num_records = 0
    with open('Diet_Dataset.txt', 'r') as file:
        data = file.readlines()
    file.close()

    # add all values to their corresponding lists with commas removed and # lines removed
    for line in data:
        if not line.startswith('#'):
            line = line.split(", ")
            TIME.append(line[0])
            MTYPE.append(line[1])
            DESC.append(line[2])
            SERVING.append(line[3])
            KCAL.append(line[4])
            SFATg.append(line[5])
            num_records += 1  # keeps track of how many records are added from the file

    # remove new line at end of each line
    i = 0
    while i != len(SFATg):
        SFATg[i] = SFATg[i].replace("\n", "")
        i += 1

    print("""  ____        __        __   _ _     _   ___  
 | __ )  ___  \ \      / /__| | |   / | / _ \ 
 |  _ \ / _ \  \ \ /\ / / _ \ | |   | || | | |
 | |_) |  __/   \ V  V /  __/ | |   | || |_| |
 |____/ \___|    \_/\_/ \___|_|_|   |_(_)___/ """)  # Welcome ascii art
    print("----------------------------------------------------------------")
    print(num_records, "Records successfully added.")


open_read()  # makes sure the file is read first


def menu():
    print("----------------------------------------------------------------")
    choice = input("[1] Show all Food Records\n"
                   "[2] Show Total Calorie Count of All Foods\n"
                   "[3] Show Average Serving Weights\n"
                   "[4] Add A New Food Item\n"
                   "[5] Show Number of Items for Each Meal Type\n"
                   "[6] Query by Saturated Fat Threshold\n"
                   "[7] Exit\n"
                   "----------------------------------------------------------------\n")  # read corresponding choice

    # if statement for all menu choices
    if choice == "1":  # show all food records and return to the menu
        show_all()
        menu()
    elif choice == "2":  # Show Total Calorie Count of All Foods and return to the menu
        cal_count()
        menu()
    elif choice == "3":  # Show Average Serving Weights and return to the menu
        serving_weights()
        menu()
    elif choice == "4":  # Add A New Food Item and return to the menu
        add_record()
        menu()
    elif choice == "5":  # Show Number of Items for Each Meal Type and return to the menu
        num_meal_type()
        menu()
    elif choice == "6":  # Query by Saturated Fat threshold and return to the menu
        query_sfat()
        menu()
    elif choice == "7":  # Exit
        end_prog = 0  # counter for while loop to check if user wants to end program
        while end_prog == 0:
            print("----------------------------------------------------------------")
            really_quit = input("Do you really want to quit? (Y/N): ")
            if really_quit == "y" or really_quit == "Y":
                print("----------------------------------------------------------------")
                print("""  ____                                                        _ 
 / ___|  ___  ___   _   _  ___  _   _   ___  ___   ___  _ __ | |
 \___ \ / _ \/ _ \ | | | |/ _ \| | | | / __|/ _ \ / _ \| '_ \| |
  ___) |  __/  __/ | |_| | (_) | |_| | \__ \ (_) | (_) | | | |_|
 |____/ \___|\___|  \__, |\___/ \__,_| |___/\___/ \___/|_| |_(_)
                    |___/                                       """)  # Exit ascii art
                quit()
            elif really_quit == "n" or really_quit == "N":
                menu()
            else:
                print("----------------------------------------------------------------")
                print("Insert a Correct Value.")
    else:  # for incorrect values
        print("----------------------------------------------------------------")
        print("Insert a Correct Value.")
        menu()


def show_all():
    print("================================================================")
    print("[TIME] | [MTYPE] | [DESC] | [SERVING] | [KCAL] | [SFATg]")
    print("================================================================")

    line = [None] * len(TIME)  # creates list with None * the number of records in TIME (could be any other attribute)

    # put all items into one list
    i = 0  # i used as a counter for the while loop
    while i != len(TIME):
        line[i] = TIME[i], MTYPE[i], DESC[i], SERVING[i], KCAL[i], SFATg[i]
        i += 1
    line.sort(key=lambda tup: tup[0])  # sort the list line by the tuple time attribute at [0]
    for items in line:
        print(items[0], items[1], items[2], items[3], items[4], items[5])  # print al records


def cal_count():
    #  calculates and prints the total calorie count
    for i in range(0, len(KCAL)):  # i used as counter
        KCAL[i] = float(KCAL[i])
    print("----------------------------------------------------------------")
    print(sum(KCAL), "Total Calories.")


def serving_weights():
    #  calculate and print the average serving weights for all foods
    weights = [] + SERVING
    for i in range(0, len(weights)):  # i used as counter
        weights[i] = float(weights[i])
    print("----------------------------------------------------------------")
    print(sum(weights) / len(weights), " is the average serving weight for all foods.")


def add_record():
    # user input is appended to the corresponding attribute list
    print("----------------------------------------------------------------")
    time_append = input("TIME: ")
    mtype_append = input("MTYPE: ")
    desc_append = input("DESC: ")
    serving_append = input("SERVING: ")
    kcal_append = input("KCAL: ")
    sfatg_append = input("SFATg: ")

    i = 0  # used as a counter for the while loop
    while i == 0:
        # checks whether you want to add the inputted the record or not and will react accordingly
        print("----------------------------------------------------------------")
        confirm = input("Are you sure you want to add this record? (Y/N): ")
        # appends the user input to the corresponding list and returns to the menu
        if confirm == "y" or confirm == "Y":
            TIME.append(time_append)
            MTYPE.append(mtype_append)
            DESC.append(desc_append)
            SERVING.append(serving_append)
            KCAL.append(kcal_append)
            SFATg.append(sfatg_append)
            menu()
        # returns to the menu
        elif confirm == "n" or confirm == "N":
            menu()
        # detects if y/Y/n/N is not inputted
        else:
            print("----------------------------------------------------------------")
            print("Insert a Correct Value.")


def num_meal_type():
    # total all meal types and print with their corresponding number
    breakfast = MTYPE.count("Breakfast")
    snack = MTYPE.count("Snack")
    lunch = MTYPE.count("Lunch")
    dinner = MTYPE.count("Dinner")
    print("----------------------------------------------------------------")
    print("Breakfast =", breakfast,
          "\nSnack =", snack,
          "\nLunch =", lunch,
          "\nDinner =", dinner)


def query_sfat():
    # user input sfat threshold in which records are returned
    print("----------------------------------------------------------------")
    threshold = input("Show all foods with saturated fat above: ")
    print("================================================================")
    print("[TIME] | [MTYPE] | [DESC] | [SERVING] | [KCAL] | [SFATg]")
    print("================================================================")

    # put all attributes in to a new list
    line = [None] * len(TIME)  # creates list with None * the number of records in TIME (could be any other attribute)
    i = 0  # i used as counter for the while loop
    while i != len(TIME):
        line[i] = TIME[i], MTYPE[i], DESC[i], SERVING[i], KCAL[i], SFATg[i]  # put all items into one list
        i += 1

    # display all records above the user inputted sfat threshold
    for items in line:
        if items[5] > threshold:
            print(items[0], items[1], items[2], items[3], items[4], items[5])


menu()  # calls menu() function when the program starts
