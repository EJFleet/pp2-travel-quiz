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
            create_new_budget()
            break
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


# Create Budget - Title and Total
def create_new_budget():
    print("create new budget working")

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