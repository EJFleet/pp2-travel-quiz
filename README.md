# Holiday Budget Tracker

## Intro

For my third portfolio project, I created an app to track the budget and spending for a user's holiday. 

![Screenshot of welcome page of Holiday Budget Tracker](/documentation/features/pp3-welcome-screen.png)

Visit the deployed site here: [Holiday Budget Tracker](https://pp3-holiday-budget-tracker-e4ed60461481.herokuapp.com/)

View Holiday Budget Tracker on [Github](https://github.com/EJFleet/pp3_holiday_budget_tracker)

Access data from the Google Sheet (read-only) [Google Sheet](https://docs.google.com/spreadsheets/d/18XqLjhsr8qBJOFHBoCdBUixmuBwP4GbWJ5870NgJcqY/edit?usp=sharing)

![GitHub last commit](https://img.shields.io/github/last-commit/ejfleet/pp3_holiday_budget_tracker)
![GitHub language count](https://img.shields.io/github/languages/count/ejfleet/pp3_holiday_budget_tracker)
![GitHub top language](https://img.shields.io/github/languages/top/ejfleet/pp3_holiday_budget_tracker)


---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Planning](#planning)
  * [Imagery](#imagery)
 
* [Features](#features)
  * [Functions](#function-descriptions)
  * [Classes](#class-definitions)
  * [Error Messages](#error-messages)
  * [Future Implementations](#future-implementations)
  * [Limitations & Future Scalability](#limitations-and-future-scalability)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Creating a New Repository](#creating-a-new-repository)
  * [Activating the Google Drive & Sheets API](#activating-the-google-drive--sheets-api)
  * [Setting up the Gitpod Workspace for the APIs](#setting-up-the-gitpod-workspace-for-the-apis)
  * [Initial Code for connecting to our API with Python](#initial-code-for-connecting-to-our-api-with-python)
  * [Deploying to Heroku](#deploying-to-heroku)
  * [How to Fork](#forking-the-github-repository)
  * [How to Clone](#clone-this-github-repository)

* [Testing](#testing)
  * [Functionality](#functionality)
  * [Code Validation](#code-validation)
  * [Solved Bugs](#solved-bugs)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### User Stories

As a user, I want to:

* Have an app that I can use to track my holiday spending
* Keep track of my spending and budget
* Be able to create my own budgets
* Be able to navigate through the app easily
* Be alerted to any error I may have made in input and instructed how to try again

#### First-time Visitor Goals

I want to: 
* Understand the purpose of the app
* Start the app with minimal instruction
* Navigate the site easily
* Have a smooth experience in creating/viewing a budget and entering expenses

#### Returning/ Frequent Visitor Goals

I want to: 
* Easily access budget information
* See a budget breakdown
* Enter new expenses to a chosen budget


## Design

### Planning

#### Flowchart

Before starting to code, I designed a flowchart with [Lucid](www.lucid.app) to visualise how a user would move through the app and to break down exactly what needed to be done.  
During the development process, the design of the app became more streamlined and effective than initially envisoned in the flowchart.
<details>
<summary>Flowchart</summary>

![Flowchart](/documentation/features/pp3-flow-chart.png)

</details>

#### Google API Setup

Prior to starting any program function code, the relevant Credentials and API set up needed to take place. This process is detailed in the [Deployment & Local Development](#deployment--local-development) section. Security was an important factor with the connecting of a Google Account to access the Google Sheets worksheet. Steps were followed carefully to ensure that no important files like, CREDS.json, were pushed to the cloud for the public to view. Guidance for the setting up of these authorisations and credentials, was provided through the Code Institute's Full Stack Software Development course.


#### Google Sheets

Google Sheets was used to store any entered user data and called upon when data was manipulated and updated. It was used to simulate a database, as the user will have no direct interaction with the actual worksheets. All data entry and manipulation takes place within the terminal.  Clear instructions are printed in the terminal instructing the user in how to enter the data, so that it may be displayed correctly on its output, within the scope of this project. 

### Imagery

#### Emojis

I used emojis to add some visual interest to the list of categories and added one to the display after a new budget is created.

![Emojis](/documentation/features/pp3-categories-with-emojis.png)

![Emojis2](/documentation/features/pp3-budget-created.png)

### ASCII Art

I used a [text-to-ASCII converter](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) to make the welcome message more inviting.

![Welcome Art](/documentation/features/pp3-welcome-screen-small.png)


## Features

### Function Descriptions

* **`main()`**: The entry point of the program. It displays a welcome message and directs the user to the main menu for further interactions.

* **`welcome_message()`**: Displays a welcome message to the user and prompts them to press 'Enter' to continue. Clears the screen before and after the message.

* **`main_menu()`**: Displays the main menu with options to create a new holiday budget, add an expense, view a budget breakdown, or exit the program. Processes user input to navigate to the corresponding functionality.

* **`clear_screen()`**: Clears the terminal screen to provide a clean interface for user interaction.

* **`is_valid_amount(amount)`**: Validates if the input amount is a positive number with up to two decimal places using a regular expression.

* **`create_new_budget()`**: Prompts the user to enter a destination and budget amount, validates the input, and creates a new budget object if valid.

* **`add_budget_sheet(budget)`**: Adds a new worksheet to the existing spreadsheet with the budget details and ensures the sheet name is unique.

* **`get_expense()`**: Prompts the user to enter expense details such as category, name, and amount, and returns an expense object.

* **`select_budget()`**: Displays a list of existing budgets and prompts the user to select one. Validates the selection and returns the corresponding budget worksheet.

* **`get_expense_amount()`**: Prompts the user to enter an expense amount, validates the input, and returns the amount if valid.

* **`choose_expense_category()`**: Displays a list of expense categories and prompts the user to select one. Validates the selection and returns the chosen category.

* **`add_expense_to_budget(expense)`**: Updates the selected budget worksheet with a new expense row.

* **`sum_expenses(budget_worksheet)`**: Calculates the total amount spent from a particular budget by summing up all expenses listed in the worksheet.

* **`calculate_remaining_budget(budget_name, budget_amount)`**: Calculates the remaining budget amount by subtracting the total expenses from the initial budget amount.

* **`budget_breakdown(selected_budget)`**: Displays a breakdown of the selected budget, showing the total spent and the remaining budget amount.

* **`exit_program()`**: Prompts the user to either restart the program or exit. Clears the screen and terminates the program if the user chooses to exit.

### Class Definitions

#### Budget Class

```python
class Budget:
    def __init__(self, name=None, amount=0):
        self.name = name if name else "Unnamed"
        self.amount = round(amount, 2)

    def __repr__(self):
        return f"Budget: {self.name}, Total: {self.amount}"
```

The Budget class represents a budget for a holiday. It initializes with a name and amount, defaulting to "Unnamed" and 0, respectively, if not provided. The amount is rounded to two decimal places. The __repr__ method returns a string representation of the budget details.

#### Expense Class

```python
class Expense:
    def __init__(self, category, name, amount, budget_name):
        self.category = category
        self.name = name
        self.amount = amount
        self.budget_name = budget_name

    def __repr__(self):
        return (f"Expense added: {self.name} for {self.amount:.2f} in "
                f"{self.category} for {self.budget_name}.\n")
```
The Expense class represents an expense within a budget. It includes details such as category, name, amount, and the associated budget name. The __repr__ method provides a formatted string summarizing the expense details.

### Error Messages

I have included error messages to be displayed if the user inputs a value that is not valid.

#### Invalid Input - Main Menu

- **Description**: If the user enters an invalid input in the main menu, an error message will be displayed instructing them to enter a number between 1 and 4.
- **Message**: "Invalid input. Please enter a number 1 - 4"
<details>
<summary>Invalid input main menu screenshot</summary>

  ![Invalid Input - Main Menu](/documentation/errors/pp3-error-main-menu.png)
</details>

-----

#### Invalid Budget Amount

- **Description**: When creating a new budget, if the user enters an invalid amount, an error message will be displayed instructing them to enter a positive number with up to two decimal places.
- **Message**: "Invalid input. Please enter a positive number with up to 2 decimal places."
<details>
<summary>Invalid budget amount screenshot</summary>

  ![Invalid Budget Amount](/documentation/errors/pp3-error-budget-amount.png)
</details>

-----

#### No Budgets Found

- **Description**: If there are no budgets available when the user tries to select one, an error message will inform them to create a budget first.
- **Message**: "No budgets found. Please create a budget first."
<details>
<summary>No budgets found screenshot</summary>

  ![No Budgets Found](/documentation/errors/pp3-error-no-budgets-found.png)
</details>

-----

#### Invalid Budget Selection

- **Description**: When selecting a budget, if the user enters an invalid number, an error message will be displayed instructing them to enter a valid budget number.
- **Message**: "Invalid budget. Please enter a number [1 - X]" (where X is the number of available budgets)
<details>
<summary>Invalid Budget Selection</summary>

  ![Invalid Budget Selection](/documentation/errors/pp3-error-budget-number.png)
</details>

-----

#### Invalid Input for Budget

- **Description**: When selecting a budget, if the user enters something that is not a number, an error message will be displayed instructing them to enter a valid input.
- **Message**: "Invalid input. Please enter a number [1 - X]" (where X is the number of available budgets)
<details>
<summary>Invalid budget input screenshot</summary>

  ![Invalid Budget Input](/documentation/errors/pp3-error-budget-input.png)
</details>

-----

#### Invalid Expense Amount

- **Description**: When entering an expense amount, if the user enters an invalid amount, an error message will be displayed instructing them to enter a positive number with up to two decimal places.
- **Message**: "Invalid input. Please enter a positive number with up to 2 decimal places."
<details>
<summary>Invalid expense amount screenshot</summary>

  ![Invalid Expense Amount](/documentation/errors/pp3-error-expense-amount.png)
</details>

-----

#### Invalid Category Selection

- **Description**: When choosing an expense category, if the user enters an invalid number, an error message will be displayed instructing them to enter a valid category number.
- **Message**: "Invalid category. Please enter a number [1 - 5]"
<details>
<summary>Invalid category selection screenshot</summary>

  ![Invalid Category Selection](/documentation/errors/pp3-error-category-number.png)
</details>

-----

#### Invalid Input for Category

- **Description**: When choosing an expense category, if the user enters something that is not a number, an error message will be displayed instructing them to enter a valid input.
- **Message**: "Invalid input. Please enter a number [1 - 5]"
<details>
<summary>Invalid category input screenshot</summary>

  ![Invalid Category Input](/documentation/errors/pp3-error-category-input.png)
</details>

-----


### Instructions for Using Holiday Budget Tracker

1. **Open the Application**:

   - Visit the deployed site: [Holiday Budget Tracker](https://pp3-holiday-budget-tracker-e4ed60461481.herokuapp.com/)


2. **Welcome Screen**:

   - You will see a welcome message. Press 'Enter' to continue.

     ![Welcome Screen](/documentation/features/pp3-welcome-screen.png)


3. **Main Menu**:

   - Choose an option by entering the corresponding number:

     1. Create new holiday budget
     2. Add an expense
     3. See budget breakdown
     4. Exit program

     ![Main Menu](/documentation/features/pp3-main-menu.png)


4. **Create New Holiday Budget**:

   - Enter the destination name.
   - Enter the total budget amount. Ensure it is a positive number with up to two decimal places.
   - A confirmation message will be displayed with the budget details.

     ![Create Budget](/documentation/features/pp3-budget-created.png)

   - A new blank worksheet in the Google Sheets document will be created.

   - ![Google Sheets](/documentation/features/pp3-blank-budget.png)


5. **Add an Expense**:

   - Select a budget from the list.
   - Choose an expense category.
   - Enter the name of the expense.
   - Enter the expense amount. Ensure it is a positive number with up to two decimal places.
   - A confirmation message will be displayed with the expense details.

     ![Add Expense](/documentation/features/pp3-expense-created.png)

   - The new expense will be added to the worksheet.

     ![Added Expense](/documentation/features/pp3-expense-added.png)


6. **See Budget Breakdown**:

   - Select a budget from the list.
   - The total spent and remaining budget will be displayed.

     ![Budget Breakdown](/documentation/features/pp3-budget-breakdown.png)


7. **Exit Program**:

   - Choose option 4 from the main menu to exit the program.
   - A goodbye message will be displayed with an option to restart the program.

     ![Exit Program](/documentation/features/pp3-exit-screen.png)



### Future Implementations

I would add features that would allow the user to do the following:
* Delete an expense
* Delete a budget
* Update a budget total
* Rename a budget
* See how much they have spent in a particular category
* See a warning if they have only a certain amount left in a budget
* Add in how long the trip will be and calculate a daily budget

### Limitations and Future Scalability

Currently, the app uses Google Sheets to store budget and expense data. While this is convenient for small-scale projects, it has limitations that can affect scalability, such as row and column limits, performance issues with large datasets, and limitations on concurrent users.

To support larger-scale applications, I would expect to migrate to a more robust database solution.


## Technologies Used


### Languages Used

The program was created with Python 3.12.2.

### Frameworks, Libraries & Programs Used

* gspread - to add, remove and manipulate data in the connected Google Sheets worksheets.
* google.oauth.service_account - for the authentication needed to access the Google APIs for connecting the Service Account with the Credentials function.
* os - to add the clear_screen function to assist in creating a neater flow.
* sys - for exiting the program.
* re - for checking the format of the user input for budget amount and expense amount.
* time - for adding a delay to the clear_screen function
* Google Sheets - for storing and retrieving the budgets and expenses.
* Google Cloud Platform - for the API for connecting to Google Sheets.
* Git - for version control.
* Github - to save and store the files for the website.
* Gitpod - for developing the site.
* Heroku - for deploying the app.
* ChatGPT - I used this when I needed answers to get unstuck and to help find bugs that I couldn't find myself.
* [Lucid.app](lucid.app) for creating the flowchart.
* [Codebeautify.org](https://codebeautify.org/python-formatter-beautifier) - for formatting the code.
* [Code Insitute PEP8 Validator](https://pep8ci.herokuapp.com/#) - for validating the Python code.
* [Shields.io](https://shields.io/) for adding badges to the readme.
* [Text to ASCII by patorjk.com](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) for the welcome message.

##  Deployment & Local Development    
  
The below steps to creating and setting up a new Python workspace and API credentials has been guided by and adapted from the [Code Institute's](https://codeinstitute.net/ie/) Python walkthrough project 'Love Sandwiches'. Please check each step is relevant to your project needs and change the data entered to suit it.

### Creating a new repository 

The [Code Institute's Python Essential Template](https://github.com/Code-Institute-Org/python-essentials-template) was used to create a terminal for my Python file to generate its output. To use this template, please take the following steps.

<details>
<summary>Steps to create a new repository</summary>  

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above Python template repository.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the green '**Gitpod**' button to generate a new workspace.   

</details> 
  
-----  

### Activating the Google Drive & Sheets API

To access the data in a Google Sheets worksheet using Python code, an API is required. Please take the following steps to set up your APIs.

<details>
<summary>Steps to activate the APIs</summary>

1. Navigate to the [Google Cloud Platform](https://cloud.google.com), using an email address/Google account that is registered to you alone.
2. Click on 'Dashboard' which will bring you to your Google Cloud Platform Dashboard. Create a new project by clicking on the project selection menu in the top left corner and choosing the '**New Project**' option. Give your new project a name and click '**Create**'. (Your access credentials are unique to each project, so create a new project for every project that you build.) 
3. Use the project selector menu to bring you to your project page.
4. Click the hamburger icon at the top left of the page.  Select '**APIs and Services**' from the left side menu, then select '**Library**'.
5. Use the search bar to search for the two APIs needed for this project, Google Drive API and Google Sheets API. One at time, choose the APIs from the search and click '**Enable**' on their main page. Follow the below steps for the Google Drive API, but only click '**Enable**' for the Google Sheets API. There is no need to download credentials again for it.
6. On the API overview page, click '**Create Credentials**' to generate some credentials which will allow us access to our Google Drive from our Python code.
7. Fill out the forms fields and dropdown menus with the information that is relevant to your project. For mine, I chose **Google Drive API -> Application Data -> No, I'm not using them** (regarding using Kubernetes, App Engine etc)
8. Under Service Account Details, choose a Service Account name and click '**Create**'.
9. In the Role Dropdown box choose **Basic -> Editor** then press '**Continue**'. Click '**Done**' to finish the form if you do not need to grant users access to the service account if it is a personal project.
10. On the next page, click on your new Service Account that has been created, then click on the '**Keys**' tab to '**Add Key**'. Select '**Create New Key**'.
11. Select JSON and '**Create**'. Your json file containing your API credentials will be downloaded to your machine.

</details>

-----  

### Setting up the Gitpod workspace for the APIs

<details>
<summary>Steps for workspace setup</summary>
  
1. In the new Gitpod workspace you've created with the Python Essentials template, click and drag the json file that you created in the above steps, into the Gitpod workspace.  
2. Rename it to `creds.json`, if you wish, and open the file. Find the client_email address, copy it without the quotes around it.
3. In the Google Sheets file that you have created for this project, click the '**Share**' button and paste the email address into the field, choose '**Editor**', untick '**Notify People**' and click '**Share**'. This allows our project access to the spreadsheet.
4. To ensure the private credentials that you have created do not make their way to the cloud for others to view, add the `creds.json` file to your `gitignore` file before you commit any changes to your repository, and push them to the cloud.
5. Use the command `git status` to check that the `creds.json` file is not staged to be committed.

</details>  
  
-----  

### Initial Code for connecting to our API with Python

<details>
<summary>Steps to including the Python/API connection code</summary>

1. The code needed to ensure your APIs connect correctly can be found at the top of the `run.py` file connected to this project. It is important that you remember to pass the exact same name as your spreadsheet to the `SHEET = GSPREAD_CLIENT.open('your-filename-here')` code, or else gspread will throw an error.
2. The command `pip3 install gspread google-auth` is needed to install the gspread package for handling the worksheet data and the google-auth package to allow access to the Google Sheets account via the Credentials we downloaded earlier. Use the above command in the Gitbash terminal to install.
3. Please refer to the `run.py` file for the import, SCOPE, CREDS, SCOPED CREDS, GSPREAD CLIENT, SHEET code that is needed to connect the APIs and change any data that is personal to your project.

</details>
  
-----

### Deploying to Heroku  

Heroku has been used to deploy this project as Python is used as a back-end language. To allow for accurate testing, I deployed the project to Heroku early on using Automatic Deployment to update the program everytime new code was pushed to my GitHub repository. Here are the steps that I followed to set my project up, guidance was provided by the [Code Institute's](https://codeinstitute.net/ie/) 'Love Sandwiches' project.     

<details>
<summary>Steps for deploying to Heroku</summary>

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'.
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. In KEY enter `CREDS`, in VALUE, paste in the text content of your `CREDS.json` file. Select '**Add**'.  
5. Repeat this process with a KEY:VALUE pair of `PORT` and `8000`.
6. In the Settings tab, in the Buildpack section, click '**Add Buildpack**', located near the bottom, right of the refreshed screen. One at a time, choose the '**Python**' pack, save changes, then choose the '**NodeJS**' buildpack and save changes. **NB: the Python buildpack _must_ be above the NodeJS buildpack.**
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9. Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Automatic' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site.

</details> 
  
-----

### Forking the GitHub Repository

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository.

<details>
<summary>Steps for forking GitHub Repository</summary>

1. Navigate to GitHub and log in.  
2. Once logged in, navigate to this repository using this link [Holiday Budget Tracker Repository](https://github.com/EJFleet/pp3_holiday_budget_tracker).
3. Above the repository file section and to the top, right of the page is the '**Fork**' button, click on this to make a fork of this repository.
4. You should now have access to a forked copy of this repository in your Github account.

</details>

-----

### Clone this GitHub Repository

A local clone of this repository can be made on GitHub. Please follow the below steps.

<details>
<summary>Steps for cloning GitHub Repository</summary>

1. Navigate to GitHub and log in.
2. The [Holiday Budget Tracker Repositiory](https://github.com/EJFleet/pp3_holiday_budget_tracker) can be found at this location.
3. Above the repository file section, locate the '**Code**' button.
4. Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the '**Copy**' button.
5. Open your Git Bash Terminal.
6. Change the current working directory to the location you want the cloned directory to be made.
7. Type `git clone` and paste in the copied URL from step 4.
8. Press '**Enter**' for the local clone to be created.

</details>

-----

## Testing

### Functionality

Extensive testing was performed to ensure that the program ran correctly.

#### Manual Testing

![Manual Testing Checklist](/documentation/testing/pp3-holiday-budget-tracker-manual-testing.png)


### Code Validation

The code was validated using PEP8 standards to ensure readability and maintainability.

<details>

<summary> Validation for run.py </summary>

![run.py validation](/documentation/testing/pp3-linter-1.png)

</details>

<details>

<summary> Validation for expense.py </summary>

![expense.py validation](/documentation/testing/pp3-linter-expense.png)

</details>

<details>

<summary> Validation for budget.py </summary>

![budget.py validation](/documentation/testing/pp3-linter-budget.png)

</details>


### Solved Bugs

|Bug|Solution|Fixed?|
|-----|-----|-----|
|Title and ID of worksheet being printed out rather than just the name| Use selected_budget.title rather than selected_budget | Yes | 
|If user doesn't enter a name for the budget, it is saved as blank rather than 'Unnamed'| Change structure of self.name in Budget class | Yes |
|Screen not clearing after user presses Enter if error message has displayed| Add clear_screen() to top of main_menu() and add clear_screen(3) to other functions | Yes |
|User could enter two budgets with same name but program froze if a third was attempted| Changed how sheets were named in the add_budget_sheet function | Yes |

**There were no other known bugs at the time of submitting the project.**

## Credits

### Code Used

- [Amy Richardson's README](https://github.com/kera-cudmore/Bully-Book-Club/tree/main) and [Monika Mak's README](https://github.com/monika-mak/budget_planner_PP3/blob/main/README.md) for examples of what to include in the README sections.
- [Pixegami's video tutorial](https://www.youtube.com/watch?v=HTD86h69PtE&ab_channel=pixegami) for the method to create a new expense and to display the categories.
- Code Institute 'Love Sandwiches' walkthrough project.
- Code Institute's sample README for ideas of what to put in each section.
- [Real Python](https://realpython.com/if-name-main-python/) - explanation and code to use for Name-Main
 
  
### Acknowledgments

* My mentor Brian Macharia for his help and clear explanations of what needed to be done
* Amy Richardson for facilitating our weekly standups and being a font of information and encouragement
* My friends and family for testing the project on their devices and offering words of encouragement
* My dog Po for making me take breaks from my desk