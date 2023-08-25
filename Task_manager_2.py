import datetime
def list_to_string(s):
    string = ""
    for f in s:
        string += f
    return string

def reg_user():
    if enter_username == "admin":
        new_username = input("Enter the username of the new user: ")
        if new_username in usernames:
            print("This username is already ragisterd...\nPlease select a diffrent username and try again:")
            new_username = input("Enter your username here: ")
        new_password = input("Enter your password here: ")
        check_password = input("Enter your password again: ")
        while new_password != check_password:
            print("Your passwords do not match")
            new_password = input("Please enter ur password again: ")
        if new_password == check_password:
            user_file = open('user.txt' , 'a')
            user_file.write(f"\n{new_username}, {new_password}")
            user_file.close

def add_task():
    user = input("Enter the user that will be assigned to this task: ")
    task_title = input("Enter the task that must be completed: ")
    task_desc = input("Enter a description of waht must be done to complete this task: ")
    due_date = input("Enter the due date of this task  (dd-mm-yyyy): ")
    current_date = datetime.date.today()
    print(current_date)
    tasks_file = open("tasks.txt" , "a")
    tasks_file.write(f"\n{user}, {task_title}, {task_desc}, {current_date}, {due_date}, No")
    tasks_file.close()

def view_all():
    tasks_list = []
    tasks_file = open("tasks.txt" , "r+")
    for line in tasks_file:
            temp = line.strip(" ,\n")
            temp = line.split(",")
            print(f"Username: {temp[0]}")
            print(f"Task: {temp[1]}")
            print(f"Task description: {temp[2]}")
            print(f"Date assigned: {temp[3]}")
            print(f"Due date: {temp[4]}")
            print("\n")
    tasks_file.close

def view_mine():
    num = 1
    num_1 = 1
    exit = 0
    task_dict = {}
    tasks_file = open("tasks.txt" , "r+")
    print("Here is a list of all your assigned tasks:\n")
    for line in tasks_file:
        temp = line.strip(" ,\n")
        temp = line.split(",")
        task_dict[num] = temp
        num = num + 1
        if enter_username in temp:
            print(f"Task:               {num_1}")
            print(f"Username:           {temp[0]}")
            print(f"Task:              {temp[1]}")
            print(f"Task description:  {temp[2]}")
            print(f"Date assigned:     {temp[3]}")
            print(f"Due date:          {temp[4]}")
            print(f"Complete:          {temp[5]}")
            print("\n")
            num_1 = num_1 + 1
    #print(task_dict)
    while exit == 0:
        task = int(input("What task would you like to view?(Enter number assigned to task): \nIf you want to return to the main menu type -1:\n"))
        if task == -1:
            exit = 1
            break
        else:
            task_num = task_dict.get(task)
        print(f"Username:         {task_num[0]}")
        print(f"Task:             {task_num[1]}")
        print(f"Task description: {task_num[2]}")
        print(f"Date assigned:    {task_num[3]}")
        print(f"Due date:         {task_num[4]}")
        print(f"Complete:         {task_num[5]}")
        
        complete = input("Would you like to mark this Task as complete or edit the task?(Enter complete, edit or no): ")
        complete = complete.lower()
        if complete == 'complete':
            act_task = task - 1
            task_num = task_dict.get(task)
            task_num[5] = 'yes\n'
            tasks_file = open("tasks.txt" , "r")
            lines_task_file = tasks_file.readlines()
            lines_task_file[act_task] = list_to_string(task_num)
            tasks_file = open("tasks.txt" , "w")
            tasks_file.writelines(lines_task_file)
        elif complete == 'edit':
            edit = input("Would you like to edit the due date or user assigned?(Enter due date , user): ")
            edit = edit.lower()
            if edit == 'due date':
                new_due_date = input("Enter the new due date(dd-mm-yyyy):  ")
                task_num = task_dict.get(task)
                task_num[4] = new_due_date
                tasks_file = open("tasks.txt" , "r")
                lines_task_file = tasks_file.readlines()
                lines_task_file[act_task] = list_to_string(task_num)
                tasks_file = open("tasks.txt" , "w")
                tasks_file.writelines(lines_task_file)

            elif edit == 'user':
                new_user = input("Enter the user name to br reassigned to the task: ")
                task_num = task_dict.get(task)
                task_num[0] = new_user
                tasks_file = open("tasks.txt" , "r")
                lines_task_file = tasks_file.readlines()
                lines_task_file[act_task] = list_to_string(task_num)
                tasks_file = open("tasks.txt" , "w")
                tasks_file.writelines(lines_task_file)

def gen_rep():
    import datetime

    tasks_file = open("tasks.txt", "r")
    lines_list = []
    amount_tasks = 0
    completed_task = 0
    incomplete_task = 0
    overdue_task = 0

    for line in tasks_file:
        amount_tasks += 1
        lines_list = line.strip("\n")
        lines_list = line.split(",")

        if lines_list[5] == 'yes':
            completed_task += 1
        else:
            incomplete_task += 1

       
    percen_inc_task = (incomplete_task / amount_tasks) * 100
    percen_overdue_task = (overdue_task / amount_tasks) * 100

    task_overview = open('task.overview.txt', 'w')
    task_overview.write(f'''
    The total number of tasks is: {amount_tasks}
    The amount of tasks that are completed are: {completed_task}
    The amount of incomplete Tasks are: {incomplete_task}
    The amount of overdue tasks are {overdue_task}
    The percentage of overdue tasks are {percen_overdue_task}%
    The percentage of incomplete tasks are {percen_inc_task}%''')

    tasks_file.close()

    user_file = open('user.txt', "r")
    tasks_file = open('tasks.txt', 'r')
    user_file_overview = open('user.file.overview.txt', 'w')
    amount_user = 0

    for f in user_file:
        amount_user += 1

    usernames = []

    for line in tasks_file:
        lines_list = line.strip("\n")
        lines_list = line.split(",")
        if lines_list[0] not in usernames:
            usernames.append(lines_list[0])

    for names in usernames:
        user_task_amount = 0
        percen_task_user = 0
        completed_task_user = 0
        incomplete_task_user = 0

        user_file_overview.write(f"{names}\n")

        tasks_file.seek(0)

        for lines in tasks_file:
            lines_list_2 = lines.strip("\n")
            lines_list_2 = lines.split(",")
            if names == lines_list_2[0]:
                user_task_amount += 1
                if lines_list_2[5] == "Yes":
                    completed_task_user += 1
                else:
                    incomplete_task_user += 1

        percen_task_user = (user_task_amount / amount_tasks) * 100
        percen_com_task_user = (completed_task_user / user_task_amount) * 100
        percen_inc_task_user = (incomplete_task_user / user_task_amount) * 100

        user_file_overview.write(f'''
        Number of tasks: {user_task_amount}
        percent of tasks assigned to user: {percen_task_user:.2f}%
        Percentage of tasks completed: {percen_com_task_user:.2f}%
        Percentage of tasks incomplete: {percen_inc_task_user:.2f}%
        ''')

    tasks_file.close()
    user_file.close()
    user_file_overview.close()

        

#=====importing libraries===========
'''This is the section where you will import libraries'''
tasks_file = open('tasks.txt', 'r+')
user_file  = open('user.txt' , 'r+')

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
usernames = []
passwords = []
for lines in user_file:
    temp = lines.strip()
    temp = lines.strip()
    temp = lines.split(", ")
    usernames.append(temp[0])
    passwords.append(temp[1].strip())
tasks_file.close()
user_file.close()

login = False
enter_username =input("Enter your username here: ")
enter_password = input("Enter your password: ")

while enter_username not in usernames :
    print("This user name does not exsist!")
    enter_username =input("Enter your username here: ")

while enter_password not in passwords:
    print("Your password is incorrect...")
    enter_password = input("Enter your password: ")
if enter_username in usernames and enter_password in passwords:
    login = True

while login == True:
    if enter_username == "admin":
            menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - statistics
gr - generate
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.


    if menu == 'r':
        reg_user()
        
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    elif menu == 'a':
        add_task()
        
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va':
        view_all()
     
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        view_mine()
        
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    elif menu == 's':
        tasks_file_overview = open('task.overview.txt' , 'r')
        user_file_overview = open('user.file.overview' , 'r')
        for lines in tasks_file_overview:
            print(lines)
        for lines in user_file_overview:
            print(lines)
        tasks_file_overview.close()
        user_file_overview.close()
    
    elif menu == 'gr':
        gen_rep()
        

    else:
        print("You have made a wrong choice, Please Try again")