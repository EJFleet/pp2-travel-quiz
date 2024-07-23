from budget import Budget
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

budget = SHEET.worksheet('budget-tracker')

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
        print("  2. Update existing budget")
        print("  3. See budget breakdown")
        print("  4. Exit program")
        
        choice = input("  Enter number 1-4: ").strip()
        if choice == '1':
            new_budget = create_new_budget()
            print(f"New budget created! You have {new_budget.amount} to spend in {new_budget.name}"
)           break
        elif choice == '2':
            add_expense()
            break
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
    print("create new budget working")
    budget_name = input("Enter your destination: \n")

    while True:
        budget_amount_input = (input("Enter total of budget: \n"))

        if is_valid_amount(budget_amount_input):
            budget_amount = float(budget_amount_input)
            new_budget = Budget(name=budget_name, amount=budget_amount)
            return new_budget
                    
        else:
            print("Invalid input.  Please enter a positive number with up to 2 decimal places.")



# Add Expense
def add_expense():
    print("add expense working")

# See Budget Breakdown
def budget_breakdown():
    print("budget breakdown working")

# Exit
def exit_program():
    print("exit program working")


main()