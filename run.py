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
    input(f"Press 'Enter' to continue...")

# Main Menu
def main_menu():
    """
    Display Main Menu
    """
    print("main menu is working")

# Create Budget - Title and Total
main()

# Add Category


# Add Expense


# Update Existing Budget - Title or Total


# See Budget Breakdown


# Exit