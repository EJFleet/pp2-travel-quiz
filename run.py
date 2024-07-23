from budget import Budget
from expense import Expense
import re
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pp3-holiday-budget-tracker')

def main():

    welcome_message()

    main_menu()


# Welcome
def welcome_message():
    """
    Display welcome message to the user with prompt to confirm entry
    """   
    print(f"Welcome to Holiday Budget Tracker!")
    input(f"Press 'Enter' to continue...\n")

# Main Menu
def main_menu():
    """
    Display Main Menu
    """
    while True:

        print("What would you like to do?")
        print("  1. Create new holiday budget")
        print("  2. Add an expense")
        print("  3. See budget breakdown")
        print("  4. Exit program")
        
        choice = input("  Enter number 1-4: ").strip()
        if choice == '1':
            new_budget = create_new_budget()
            print(f"New budget created! You have {new_budget.amount:.2f} to spend in {new_budget.name}\n")
            add_budget_sheet(new_budget)

        elif choice == '2':
            new_expense = get_expense()
            print(new_expense)

        elif choice == '3':
            budget_breakdown()
            break
            
        elif choice == '4':
            exit_program()
            break
        else:
            print('Invalid number. Please try again')

# Check input for valid number
def is_valid_amount(amount):
    """
    Checks is the number entered is a positive number with up to two decimal places
    """
    pattern = r'^\d+(\.\d{1,2})?$'
    return re.match(pattern, amount) is not None


# Create Budget - Title and Total
def create_new_budget():
    """
    Create a new budget with new name and new total
    """
    budget_name = input("Enter your destination: \n")

    while True:
        budget_amount_input = (input("Enter total of budget: \n"))

        if is_valid_amount(budget_amount_input):
            budget_amount = round(float(budget_amount_input), 2)
            new_budget = Budget(name=budget_name, amount=budget_amount)
            return new_budget
                    
        else:
            print("Invalid input.  Please enter a positive number with up to 2 decimal places.")


def add_budget_sheet(budget):
    """
    Add a new sheet to the existing spreadsheet with the budget details
    """

    # Ensure sheet name is unique
    sheet_name = budget.name
    existing_sheets = [sheet.title for sheet in SHEET.worksheets()]

    count = 2
    while sheet_name in existing_sheets:
        sheet_name = f"{budget.name} 2"
        count += 1

    # Add new budget worksheet to spreadsheet
    new_sheet = SHEET.add_worksheet(title=sheet_name, rows=100, cols=20)
    
    # Populate new sheet with budget details

    new_sheet.update(range_name='A1:B1', values=[['Destination:', budget.name]])
    new_sheet.update(range_name='A2:B2', values=[['Budget Total:', budget.amount]])
    new_sheet.update(range_name='A3:D4', values=[['Category', 'Expense Name', 'Amount', 'Budget Remaining']])

    print(f"New sheet '{sheet_name}' created with budget amount {budget.amount:.2f}")


# Add Expense
def get_expense():
    """
    Gets the details of the user's expense and adds it to the worksheet
    """
    # Choose which budget to update
    while True:
        worksheets = SHEET.worksheets()
        for i, sheet in enumerate(worksheets):
            if i == 0:
                continue
            else:
                print(f"  {i}.{sheet.title}")
        
        budget_value_range = f"[1 - {len(worksheets) - 1}]"
        selected_budget_input = input(f"Enter a budget number {budget_value_range}: \n")
        
        try:
            selected_budget_index = int(selected_budget_input)
            if selected_budget_index in range(len(worksheets)):
                selected_budget = worksheets[selected_budget_index]
                break
            else:
                print(f"Invalid budget. Please enter a number {budget_value_range}")
        
        except ValueError:
            print(f"Invalid input. Please enter a number {budget_value_range}")
        


    # Enter name of expense
    expense_name = input("Enter name of expense: \n")

    # Enter amount of expense
    
    while True:
        expense_amount_input = input("Enter expense amount: \n")

        try:
            if is_valid_amount(expense_amount_input):
                expense_amount = round(float(expense_amount_input), 2)
                break
            else:
                print("Invalid input.  Please enter a positive number with up to 2 decimal places.")
        
        except ValueError:
            print("Invalid input.  Please enter a positive number with up to 2 decimal places.")


    # Choose expense category
    expense_categories = [
            "🏨 Accommodation",
            "✈️ Travel",
            "🍔 Food",
            "🎉 Entertainment",
            "🛍️ Miscellaneous"
        ]

    while True:
        print("Select an expense category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        selected_category_input = input(f"Enter a category number [{value_range}]: \n")
        
        try:
            selected_category_index = int(selected_category_input) - 1

            if selected_category_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_category_index]
                new_expense = Expense(
                    category=selected_category, name=expense_name, amount=expense_amount, budget_name=selected_budget.title
                )
                return new_expense

            else:
                print(f"Invalid category. Please enter a number between 1 and {value_range}")
        
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {value_range}")
            

# See Budget Breakdown
def budget_breakdown():
    print("budget breakdown working")

# Exit
def exit_program():
    print("exit program working")


main()