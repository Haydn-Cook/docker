from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = int(quantity)
    
    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
         

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    while True:
        try:
            file_to_open = input("Please Enter the name of the file you would like to open: ")
            file = open(file_to_open , "r")
            break
        except Exception:
            print("This is a invalid file name please try agian: ")
    
    
    number = 0
    for lines in file:
        number += 1
        if number == 1:
            pass
        elif lines == None:
            pass
        else:
            temp = lines.strip()
            temp = lines.split(",")
            temp[4] = temp[4].strip("\n")
            shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))
    
    return f"Shoes captured from {file}"
    

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country_shoe = input("What country will the shoe be shipped from?: ")
    code_shoe = input("What is the code of the shoe?: ")
    name_shoe = input("What is he name of the shoe?: ")
    cost_shoe = input("What is the cost of the shoe?: ")
    quantity_shoe = input("What is the amount of shoes in stock?: ")
    
    shoe_list.append(Shoe(country_shoe, code_shoe, name_shoe, cost_shoe, quantity_shoe))

    file = open("inventory.txt" , "a")
    file.write(f"\n{country_shoe},{code_shoe},{name_shoe},{cost_shoe},{quantity_shoe}\n")

    return f"Shoe has been captured"

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    number = 0
    for e in shoe_list:
        number += 1
        print(number)
        print(e.__str__())
    return "All shoe has been displayed"

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    amount_shoe = []
    for a in shoe_list:
        temp = a.quantity
        amount_shoe.append(temp)
        amount_shoe.sort()
    
    for e in shoe_list:
        if e.quantity == amount_shoe[0]:
            print(e.__str__())
            stock = input(f"This is the shoe with the lowest stock. Would you like to restock this shoe? (Yes or No): ")
            stock = stock.lower()
            if stock == "yes":
                amount_to_add = int(input("How much would you like to restock the shoe by?: "))
                e.quantity += amount_to_add
                with open("inventory.txt", "w") as file:
                    for n in shoe_list:
                        file.write(f"{n.__str__()}\n")
            elif stock == "no":
                print("Here is a list of all shoes. Please select one you want to restock.")
                print("If you don't want to restock a shoe, type 'no'.")
                big_shoe_list = []
                for i, a in enumerate(shoe_list):
                    big_shoe_list.append([i+1, a.product, a.quantity])
                shoe_table = tabulate(big_shoe_list, headers=["Number", "Product", "Quantity"])
                print(shoe_table)
                table_number = int(input("Please provide the integer number of the shoe you want to restock: ")) - 1
                amount_to_add = int(input("How much would you like to restock this shoe by?"))
                if table_number < 0 or table_number >= len(shoe_list):
                    return "Invalid shoe number."
                big_shoe_list[table_number][2] += amount_to_add
                temp = big_shoe_list[table_number][2]
                with open("inventory.txt", "w") as file:
                    for i, n in enumerate(shoe_list):
                        if i == table_number:
                            n.quantity = temp
                        file.write(f"{n.__str__()}\n")
            return "The stock of the shoe has been updated."
     
                
def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    shoe_code = input("Enter the code of the shoe you would like to view: ")
    for e in shoe_list:
        if e.code == shoe_code:
            print(e.__str__())
    return "Shoe has been displayed"

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    number = 0
    for e in shoe_list:
        number += 1
        value = int(e.cost) * int(e.quantity)
        print(f'''Shoe:{number}
              Name: {e.product}
              value = {value}\n''')
    return "Value per item for all shoes has been displayed"

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    amount_shoe = []
    for a in shoe_list:
        temp = a.quantity
        amount_shoe.append(temp)
        amount_shoe.sort()
    
    for e in shoe_list:
        if e.quantity == amount_shoe[-1]:
            print(e.__str__())
            print(f"This item will now be on sale!")
    return "Shoe with the highest quantity has been put on sale"

read_shoes_data()
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    option = int(input(''''
    1 - Add Shoe
    2 - View all Shoes 
    3 - Re-Stock a Shoe
    4 - Search a Shoe
    5 - View Value per Item
    6 - Highest Quantity
    7 - Exit
    '''))

    if option == 1:
        print(capture_shoes())
    
    elif option == 2:
        print(view_all())

    elif option == 3:
        print(re_stock())

    elif option == 4:
        print(search_shoe())

    elif option == 5:
        print(value_per_item())
    
    elif option == 6:
        highest_qty()
    
    elif option == 7:
        break

    else:
        print("Invalid input: ")
