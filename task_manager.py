"""
Task Manager Program Function Summary

This program manages tasks for multiple users. It uses 'user.txt' for user credentials
and 'tasks.txt' for task data. The program offers different functionalities based on 
user roles:

Admin Users:
- Register new users
- Add tasks
- View all tasks
- View and edit their own tasks
- Generate reports
- Display statistics
- Exit program

Regular Users:
- Add tasks
- View all tasks
- View and edit their own tasks
- Exit program

The program utilizes the datetime module for date handling and implements various 
functions for improved modularity and maintainability.

Files:
- user.txt: Stores user credentials
- tasks.txt: Stores task information
- task_overview.txt: Generated report on task statistics
- user_overview.txt: Generated report on user statistics
"""

                            # USER LOGIN SECTION

""" This section deals with the login section of the program. It verifies the entered credentials against the stored data in the 'user.txt' file.
The program will continue to prompt the user to add the right login details until valid credentials are inserted."""


# Import the necessary library:
import datetime

# Create a login page to check if the user already registered. If the wrong credentials are entered display an error:
print("Please log in using your credentials:".upper())

# define a boolean variable to ensure that the program only proceeds further once the user enters the correct data.
logged_in = False

# Define an empty list for the entered username and passwords to be added to using append:
user_list = []

# Start a 'while loop' and ask the user to enter their username and password:
while not logged_in:
    username = input("Enter your username:\n")
    password = input("Enter your password:\n")


# Add a login verification:
    with open("user.txt", "r") as user_file:
        for line in user_file:
            stored_username, stored_password = line.strip().split(", ")
            if username == stored_username and password == stored_password:
                logged_in = True
                break

    if not logged_in:
            print("\nInvalid username or password. Please try again.\n".upper())


                        # CREATE A FUNCTION TO REGISTER NEW USERS:


"""This functions allows the admin to register new users. It checks for existing users and avoids duplicate entries and adds the new user to the 'user.txt file.'"""

# Ask the username and password of the new user to register them only if the person registering is 'admin':
def reg_user():
    if username != "admin":
        print("\nOnly admins can register new users.\n".upper())
        return
    while True:
        new_username = input("\nPlease enter a username:\n")

# Check if user details exist in the 'user.txt' file:
        if user_exists(new_username):
            print("\nUsername already exists. Please try another:\n".upper())
            continue

# Check if the new password and the re-entry of the password match. If the passwords do not match ask the user to re-enter the passwords:
        new_password = input("\nPlease enter a password:\n")
        confirm_password = input("\nRe-enter the password to confirm:\n")
        if new_password == confirm_password:
            with open("user.txt", "a") as user_file:
                user_file.write(f"\n{new_username}, {new_password}")
            print("\nNew user registered successfully!\n".upper())
            break
        else:
            print("\nPasswords do not match. Please try again:\n".upper())


                            # CREATE A FUNCTION TO CHECK IF A USER EXISTS IN THE 'USER.TXT' FILE:


"""This function checks if a user exists. It returns True if the user is found and false if the user is not found."""

def user_exists(username):
    with open ("user.txt", "r") as user_file:
        for line in user_file:
            if line.split(", ")[0] == username:
                return True
    return False


                            # CREATE A FUNCTION TO ADD TASKS:


"""This function allows users to add tasks. It collects the required details and appends them to the 'task.txt' file"""

# Ask the user to input all the required fields to add a new task:
# Check if the user exists in the 'user.txt' file. If the user does not exist do not add the user and display and error message:
def add_task():
    task_username = input("\nPlease enter the username of the user the task is assigned to:\n")
    if not user_exists(task_username):
        print(f"\nError: User '{task_username}' does not exist. The task will not be added.\n".upper())
        return

    task_title = input("\nPlease enter the title of the task:\n")
    task_description = input("\nPlease enter the description of the task:\n")
    current_date = datetime.date.today().strftime("%d %b %Y")

    while True:
        try:
            due_date_input = input("\nPlease enter the due date of the task (DD MMM YYYY):\n")
            task_due_date = datetime.datetime.strptime(due_date_input, "%d %b %Y")
            task_due_date = task_due_date.strftime("%d %b %Y")
            break
        except ValueError:
            print("\nInput Error: Please use DD-MMM-YYYY\n".upper())
    
    task_complete = "No"

# Open the 'task.txt' file and add the new data to it:
    with open("tasks.txt", "a") as task_file:
        task_file.write(f"\n{task_username}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_complete}")

    print("\nThe task has been added successfully!\n".upper())


                            # CREATE A FUNCTION TO VIEW ALL TASKS:


"""This function displays all the details in the 'tasks.txt' file."""

def view_all():
    print("\nHere are all the tasks:\n".upper())

# Read the 'tasks.txt' file and loop through it. Use the 'strip' and 'split' functions to break the data up into the correct sections:
    with open("tasks.txt", "r") as task_file:
        for i in task_file:
            task_sections = i.strip().split(", ")
            if len(task_sections) == 6:                   
                print(f"""
____________________________________________________________________________________________________                                           
Task:                   {task_sections[1]}
Assigned to:            {task_sections[0]}
Date assigned:          {task_sections[3]}
Due date:               {task_sections[4]}
Task completed?         {task_sections[5]}
Task description:       {task_sections[2]}
____________________________________________________________________________________________________
                """)
            else:
                print(f"Skipping incorrect formatted task: {i}".upper())



                            # CREATE A FUNCTION THAT ALLOWS USERS TO VIEW THEIR OWN TASKS:


"""This function allows users to view the tasks assigned to them and that allows tasks selection and editing."""

def view_mine():
    print(f"\nHere are all the tasks assigned to you ({username}):\n".upper())
    
    user_tasks = {}
    with open("tasks.txt", "r") as task_file:
        for i, line in enumerate(task_file, 1):
            task_data = line.strip().split(", ")
            if task_data[0] == username:
                user_tasks[i] = task_data

                print(f"""
Task {i}:
____________________________________________________________________________________________________                                       
Task:                   {task_data[1]}
Assigned to:            {task_data[0]}
Date assigned:          {task_data[3]}
Due date:               {task_data[4]}
Task completed?         {task_data[5]}
Task description:       {task_data[2]}
____________________________________________________________________________________________________
                """)

    if not user_tasks:
        print("\nYou do not have any tasks assigned to you.\n".upper())
        return

    while True:
        choice = input("\nEnter the number of a task to edit it, or -1 to return to the main menu:\n")
        if choice == "-1":
            break
        
        try:
            task_number = int(choice)
            if task_number in user_tasks:
                edit_task((task_number, user_tasks[task_number]))
            else:
                print("\nInvalid task number. Please try again.\n".upper())
        except ValueError:
            print("\nInvalid input. Please enter a number or -1 to exit.\n".upper())


                            # CREATE A FUNCTION TO EDIT TASKS:


"""This function allows users to edit selected tasks. The editing includes changing assigned users, due dates and marking the task as complete."""

# NB my friend Mark gave some advice and guidance in this section:
def edit_task(task):
    task_number, task_data = task
    if task_data[5].lower() == "yes":
        print("\nThis task is already completed and cannot be edited.\n".upper())
        return

    print(f"""
1. Mark as complete
2. Edit assigned user
3. Edit due date
            """)

    choice = input("Enter your choice (1-3):\n")

    if choice == "1":
        task_data[5] = "Yes"
        print("\nTask marked as complete.\n".upper())

    elif choice == "2":
        new_user = input("\nEnter the new username for this task:\n")
        if user_exists(new_user):
            task_data[0] = new_user
            print("\nTask assigned user updated.\n".upper())
        else:
            print("\nUser does not exist. Task not updated.\n".upper())

    elif choice == "3":
        while True:
            try:
                new_due_date = input("\nEnter the new due date (DD MMM YYYY):\n")
                parsed_date = datetime.datetime.strptime(new_due_date, "%d %b %Y")
                task_data[4] = parsed_date.strftime("%d %b %Y")
                print("\nDue date update complete.\n".upper())
                break
            except ValueError:
                print("\nInvalid date format. Please use DD MMM YYYY.\n".upper())
    else:
        print("\nInvalid choice. No changes made.\nEnter the number of a task to edit it, or -1 to return to the main menu:\n".upper())

    update_task_file(task_number, task_data)


                            # CREATE A FUNCTION TO UPDATE THE 'TASK.TXT' FILE:


"""This function updates the 'tasks.txt' file with the edited task information."""


def update_task_file(task_number, updated_task):
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()

    tasks[task_number - 1] = ", ".join(updated_task) + "\n"

    with open("tasks.txt", "w") as task_file:
        task_file.writelines(tasks)


                            # CREATE FUNCTIONS TO CREATE REPORT GENERATIONS:


"""This function generates task and user overview reports."""

def generate_report():
    gen_task_overview()
    gen_user_overview()
    print("\nThe reports have successfully generated\n".upper())


"""This function generates 'task_overview.txt' which contains statistics about all the tasks."""

def gen_task_overview():
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    today = datetime.datetime.now().date()
    
    with open("tasks.txt", "r") as task_file:
        for line in task_file:
            total_tasks += 1
            task_data = line.strip().split(", ")
            if task_data[5].lower() == "yes":
                completed_tasks += 1
            else:
                uncompleted_tasks += 1
                due_date = datetime.datetime.strptime(task_data[4], "%d %b %Y").date()
                if due_date < today:
                    overdue_tasks += 1

    with open("task_overview.txt", "w") as overview_file:
            overview_file.write(f"""
Total tasks: {total_tasks}
Completed tasks: {completed_tasks}
Uncompleted tasks: {uncompleted_tasks}
Overdue tasks: {overdue_tasks}
Percentage of incomplete tasks: {(uncompleted_tasks / total_tasks) * 100:.2f}%
Percentage of overdue tasks: {(overdue_tasks / total_tasks) * 100:.2f}%
                                """)


"""This function generates the 'user_overview.txt' file containing statistics about tasks of each user."""

def gen_user_overview():
    total_users = 0
    total_tasks = 0
    user_tasks = {}

# Populate 'user_tasks' and count 'total_users' and 'total_tasks'
# NB my friend Mark gave some advice and guidance in this section:
    with open("user.txt", "r") as user_file:
        for line in user_file:
            total_users += 1
            username = line.strip().split(", ")[0]
            user_tasks[username] = {"total": 0, "completed": 0, "uncompleted": 0, "overdue": 0}

    with open("tasks.txt", "r") as task_file:
        for line in task_file:
            total_tasks += 1
            task_data = line.strip().split(", ")
            username = task_data[0]
            if username in user_tasks:
                user_tasks[username]["total"] += 1
                if task_data[5].lower() == "yes":
                    user_tasks[username]["completed"] += 1
                else:
                    user_tasks[username]["uncompleted"] += 1
                    due_date = datetime.datetime.strptime(task_data[4], "%d %b %Y").date()
                    if due_date < datetime.date.today():
                        user_tasks[username]["overdue"] += 1

    with open("user_overview.txt", "w") as overview_file:
        overview_file.write(f"Total users: {total_users}\n")
        overview_file.write(f"Total tasks: {total_tasks}\n\n")
        
        for user, stats in user_tasks.items():
            if stats["total"] > 0:
                    overview_file.write(f"""
User: {user}
Total tasks assigned: {stats['total']}
Percentage of total tasks: {(stats['total'] / total_tasks) * 100:.2f}%
Percentage of completed tasks: {(stats['completed'] / stats['total']) * 100:.2f}%
Percentage of tasks to be completed: {(stats['uncompleted'] / stats['total']) * 100:.2f}%
Percentage of overdue tasks: {(stats['overdue'] / stats['total']) * 100:.2f}%
                                    """)


"""This function displays statistics from both the 'task_overview' and 'user_overview.txt' files and generates the files if they do not exist."""

def display_stats():
    try:
        with open("task_overview.txt", "r") as task_overview, open("user_overview.txt", "r") as user_overview:
            print(f"""
TASK OVERVIEW:
{task_overview.read()}

USER OVERVIEW:
{user_overview.read()}
                    """)
    except FileNotFoundError:
        print("\nReports are not found. New reports are being generated...\n".upper())
        generate_report()
        display_stats()


                            # THE MAIN LOOP STARTS HERE:


"""This is the main loop program which displays the user menu options and calls the appropriate functions based on the user's input. The menu presented will be different for admin and normal users."""

# The menu below indicates the admin's menu:
while logged_in:
    if username == "admin":
            menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
: ''').lower()
    else:

# The menu below indicates the normal user's menu:
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

# Create an elif statments combined with the newly created functions:
    if menu == "r":
        reg_user()
    elif menu == "a":
        add_task()
    elif menu == "va":
        view_all()
    elif menu == "vm":
        view_mine()
    elif menu == "gr" and username == "admin":
        generate_report()
    elif menu == "ds" and username == "admin":
        display_stats()
    elif menu == "e":
        print("\nGoodbye!!!\n".upper())
        break
    else:
        print("\nYou have entered an invalid input. Please try again:\n".upper())
