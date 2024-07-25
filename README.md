# Holiday Budget Tracker

## Intro

For my third portfolio project, I created an app to track the budget and spending for a user's holiday. 

![Screenshot of welcome page of Holiday Budget Tracker](/documentation/testing/pp3-welcome-screen.png)

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
    * [Flowchart](#flowchart)
    * [Google API Setup](#google-api-setup)
    * [Google Sheets](#google-sheets)
 
* [Features](#features)
  * [Functions](#function-definitions)
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
  * [Browser Compatibility](#browser-compatibility)
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

![Flowchart](/documentation/pp3-flow-chart.png)

</details>

#### Google API Setup

Prior to starting any program function code, the relevant Credentials and API set up needed to take place. This process is detailed in the [Deployment & Local Development](#deployment--local-development) section. Security was an important factor with the connecting of a Google Account to access the Google Sheets worksheet. Steps were followed carefully to ensure that no important files like, CREDS.json, were pushed to the cloud for the public to view. Guidance for the setting up of these authorisations and credentials, was provided through the Code Institute's Full Stack Software Development course.


#### Google Sheets

Google Sheets was used to store any entered user data and called upon when data was manipulated and updated. It was used to simulate a database, as the user will have no direct interaction with the actual worksheets. All data entry and manipulation takes place within the terminal.  Clear instructions are printed in the terminal instructing the user in how to enter the data, so that it may be displayed correctly on its output, within the scope of this project. 


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

The program was created entirely with Python 3.12.2

### Frameworks, Libraries & Programs Used

* gspread - to add, remove and manipulate data in the connected Google Sheets worksheets.
* google.oauth.service_account - for the authentication needed to access the Google APIs for connecting the Service Account with the Credentials function.
* os - to add the clear_screen function to assist in creating a neater flow.
* sys - for exiting the program.
* re - for checking the format of the user input for budget amount and expense amount.
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


##  Deployment & Local Development    
  
The below steps to creating and setting up a new Python workspace and API credentials has been guided by and adapted from the [Code Institute's](https://codeinstitute.net/ie/) Python walkthrough project 'Love Sandwiches'. Please check each step is relevant to your project needs and change the data entered to suit it.

### Creating a new repository 
<details open>
<summary>Steps to create a new repository.</summary>  

The [Code Institute's Python Essential Template](https://github.com/Code-Institute-Org/python-essentials-template) was used to create a terminal for my Python file to generate it's output. To use this template, please follow these steps:
1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above Python template repository.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the green '**Gitpod**' button to generate a new workspace.   

</details> 
  
-----  

### Activating the Google Drive & Sheets API
<details>
<summary>Steps to activate the APIs</summary>
To access the data in a Google Sheets worksheet using Python code, an API is required. Please follow these steps to set up your APIs:  

1. Navigate to the [Google Cloud Platform](https://cloud.google.com), using an email address/Google account that is registered to you alone.
2. In the Google Cloud Platform Dashboard, create a new project by clicking on the '**Select a Project**' button and choosing the '**New Project**' option. Give your new project a name and click '**Create**'. (Your access credentials are unique to each project, so create a new project for every project that you build.) 
3. Click '**Select Project**' in the blue banner to bring you to your project page.
4. Select '**APIs and Services**' from the left side menu, then select '**Library**'.
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
2. Rename it to `CREDS.json`, if you wish, and open the file. Find the client_email address you previously entered, copy it without the quotes around it.
3. In the Google Sheets file that you have created for this project, click the '**Share**' button and paste the email address into the field, choose '**Editor**', untick '**Notify People**' and click '**Share**'. This allows our project access to the spreadsheet.
4. To ensure the private credentials that you have created do not make their way to the cloud for others to view, add the `creds.json` file to your `gitignore` file before you commit any changes to your repository, and push them to the cloud.
5. Use the command `git status` to check that the `creds.json` file is not staged to be committed.

</details>  
  
-----  

### Initial Code for connecting to our API with Python
<details>
<summary>Steps to including the Python/API connection code</summary>

1. The code needed to ensure your APIs connect correctly can be found at the top of the `run.py` file connected to this project. It is important that you remember to pass the exact same name as your spreadsheet to the `SHEET = GSPREAD_CLIENT.opn('your-filename-here')` code, or else gspread will throw an error.
2. The command `pip3 install gspread google-auth` is needed to install the gspread package for handling the worksheet data and the google-auth package to allow access to the Google Sheets account via the Credentials we downloaded earlier. Use the above command in the Gitbash terminal to install.
3. Please refer to the `run.py` file for the import, SCOPE, CREDS, SCOPED CREDS, GSPREAD CLIENT, SHEET code that is needed to connect the APIs and change any data that is personal to your project.

</details>
  
-----  

### Deploying to Heroku  

Heroku has been used to deploy this project as Python is used as a back-end language. To allow for accurate testing, I deployed the project to Heroku early on using Automatic Deployment to update the program everytime new code was pushed to my GitHub repository. Here are the steps that I followed to set my project up, guidance was provided by the [Code Institute's](https://codeinstitute.net/ie/) 'Love Sandwiches' project.     

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
<details>
<summary>Create new app</summary>
<img src ="documentation/readme/heroku_1.png">
</details>  

3. Enter an app name and choose your region. Click '**Create App**'.
<details>
<summary>Enter app name</summary>
<img src ="documentation/readme/heroku_2.png">
</details>  
  
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. In KEY enter `CREDS`, in VALUE, paste in the text content of your `CREDS.json` file. Select '**Add**'.  
5. Repeat this process with a KEY:VALUE pair of `PORT` and `8000`.
6. In the Settings tab, in the Buildpack section, click '**Add Buildpack**', located near the bottom, right of the refreshed screen. One at a time, choose the '**Python**' pack, save changes, then choose the '**NodeJS**' buildpack and save changes. **NB: the Python buildpack _must_ be above the NodeJS buildpack.**
  
<details>
<summary>Choose Buildpacks</summary>
<img src ="documentation/readme/heroku_bp.png">
</details>  
  
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9. Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Automatic' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site.

  
-----  

### Forking the GitHub Repository

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:  

1. Navigate to GitHub and log in.  
2. Once logged in, navigate to this repository using this link [Holiday Budget Tracker Repository](https://github.com/EJFleet/pp3_holiday_budget_tracker).
3. Above the repository file section and to the top, right of the page is the '**Fork**' button, click on this to make a fork of this repository.
4. You should now have access to a forked copy of this repository in your Github account.

-----  

### Clone this GitHub Repository

A local clone of this repository can be made on GitHub. Please follow the below steps:

1. Navigate to GitHub and log in.
2. The [Holiday Budget Tracker Repositiory](https://github.com/EJFleet/pp3_holiday_budget_tracker) can be found at this location.
3. Above the repository file section, locate the '**Code**' button.
4. Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the '**Copy**' button.
5. Open your Git Bash Terminal.
6. Change the current working directory to the location you want the cloned directory to be made.
7. Type `git clone` and paste in the copied URL from step 4.
8. Press '**Enter**' for the local clone to be created.

## Testing

### Functionality

Extensive testing was performed to ensure that the program ran correctly.

#### Manual Testing

![Manual Testing Checklist](/documentation/testing/pp3-holiday-budget-tracker-manual-testing.png)


### Browser Compatibility

The website was tested on:
* Chrome
* Edge
* Safari
* Firefox
* Chrome for Android


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
|Title and ID of worksheet being printed out rather than just the name| Use selected_budget.title rather than selected_budget | Yes| 
|If user doesn't enter a name for the budget, it is saved as blank rather than 'Unnamed'| ? | No |
|Screen not clearing after user presses Enter if error message has displayed| ? | No |



## Credits

### Code Used

[Amy Richardson's README](https://github.com/kera-cudmore/Bully-Book-Club/tree/main) and [Monika Mak's README](https://github.com/monika-mak/budget_planner_PP3/blob/main/README.md) for examples of what to include in the README sections.

[Pixegami's video tutorial](https://www.youtube.com/watch?v=HTD86h69PtE&ab_channel=pixegami) for the method to create a new expense and to display the categories.

Code Institute 'Love Sandwiches' walkthrough project.

Code Institute's sample README for ideas of what to put in each section.

[Real Python](https://realpython.com/if-name-main-python/) - explanation and code to use for Name-Main
 
  
### Acknowledgments

* My mentor Brian Macharia for his help and clear explanations of what needed to be done
* Amy Richardson for facilitating our weekly standups and being a font of information and encouragement
* My friends and family for testing the project on their devices and offering words of encouragement