# boutique_ado_v1

[Link to deployed site]()
<hr>
Description

![amiresponsive]()

# Table Of Content

-   [User Experience](#user-experience)
    -   [User Stories](#user-stories)
    -   [Site Goals](#site-goals)
    -   [Scope](#scope)
-   [Design](#design)
    -   [Colour Scheme](#colour-scheme)
    -   [Database Schema](#Database-Schema)
    -   [Fonts](#Fonts)
    -   [Wireframes](#Wireframes)
    -   [Agile Methodology](#Agile-Methodology)
         -   [Overview](#overview)
         -   [EPICS(Milestones)](#epicsmilestones)
         -   [User Stories issues](#user-stories-issues)
         -   [MoSCoW prioritization](#moscow-prioritization)
         -   [GitHub Projects](#github-projects)
-   [Features](#features)
    -   [Navbar](#Navbar)
    -   [Footer](#Footer)
    -   [Home](#Home)
        -   [Hero Section](#hero-section)
        -   [Search Form](#search-form)
        -   [Recent Listings](#recent-listings)
        -   [Listing Card](#listing-card)
    -   [Listings Page](#listings-page)
    -   [Create Listing](#create-listing)
    -   [Profile Page](#profile-page)
    -   [My Listings](#my-listings)
    -   [My Favourites](#my-favourites)
    -   [Remove From Favourites](#remove-from-favourites)
    -   [Edit Listing](#edit-listing)
    -   [Delete Listing](#delete-listing)
    -   [View Listing](#view-listing)
    -   [User account and User account listings](#user-account-and-user-account-listings)
    -   [Sign In Page](#sign-in-page)
    -   [Sign Up Page](#sign-up-page)
    -   [Sign Out Confirmation](#sign-out-confirmation)
    -   [Edit Profile](#edit-profile)
    -   [Delete Profile Confirmation](#delete-profile-confirmation)
    -   [We are sorry to see you go](#we-are-sorry-to-see-you-go)
    -   [Password reset](#password-reset)
    -   [Enter a new password](#enter-a-new-password)
    -   [Password Reset Completed](#password-reset-completed)
    -   [Error Pages](#error-pages)
-   [Future Features](#future-features)
-   [Testing](#testing)
-   [Bugs](#Bugs)
-   [Technologies And Languages](#technologies-and-languages)
    -   [Languages Used](#languages-used)
    -   [Python Modules](#python-modules)
    -   [Technologies and programs](#technologies-and-programs)
-   [Deployment](#deployment)
    -   [Before Deployment](#before-deployment)
    -   [Deployment on Heroku](#deployment-on-heroku)
    -   [Creating A Fork](#creating-a-fork)
    -   [Cloning Repository](#cloning-repository)
-   [Credits](#credits)
    -   [Media](#media)
    -   [Code](#code)
    -   [Acknowledgements](#acknowledgements)
    -   [Comments](#comments)


## User Experience

### User Stories

USER STORY A1 Developer Create the project's Django structure <hr>
USER STORY A2 Developer Connect database and media storage<hr>
USER STORY A3 Developer Initial deployment<hr>
USER STORY A4: Developer Wireframes and Layout<hr>
USER STORY A5: Responsive layout<hr>
USER STORY B1 About Page<hr>
USER STORY B2 About Page Site Owner<hr>
USER STORY B3 Guest Profile Page - **Future Feature**<hr>
USER STORY B4 Home Page<hr>
USER STORY B4.1 Home Page - Hero Carousel<hr>
USER STORY B4.2: Home Page - Cottages Section<hr>
USER STORY B4.3: Home Page - Reviews Section<hr>
USER STORY B4.3: Home Page - Reviews Section Pagination<hr>
USER STORY B5 Reservations - **Future Feature**<hr>
USER STORY B6 Navigation<hr>
USER STORY B7 Footer<hr>
USER STORY B8.1 Cottage Detail Page - Cottage Carousel<hr>
USER STORY B8.2 Cottage Detail Page - Cottage Detail<hr>
USER STORY B8.3 Cottage Detail Page - Cottage Review<hr>
USER STORY B8.4 Cottage Detail Page - Cottage Review Entry<hr>
USER STORY B8.5 Cottage Detail Page - Cottage Review Edit<hr>
USER STORY B8.6 Cottage Detail Page - Cottage Review Delete<hr>
USER STORY B8.7 Cottage Detail Page - Cottage Review Pagination<hr>
USER STORY B9.1 Review Detail Page - Cottage 1 Reviews<hr>
USER STORY B9.2 Review Detail Page - Cottage 2 Reviews<hr>
USER STORY B9.2 Review Detail Page - Cottage Reviews Pagination<hr>
USER STORY C1.1 Create Account<hr>
USER STORY C1.2 Admin Edit Account<hr>
USER STORY C2 User Password Reset<hr>
USER STORY C3 User Profile Page View/Edit Reviews & Reservations - **Future Feature**<hr>
USER STORY C4 Create Reservations - **Future Feature**<hr>
USER STORY C5 Edit Reservation - **Future Feature**<hr>
USER STORY C6 Delete Reservation - **Future Feature**<hr>

### Site Goals

1. To provide the users with a place to book a holiday.
2. To provide a range of available dates for cottages to potential letters.
3. To provide a place for the users to browse cottage and tourist amenities offered as well as the prices.
4. To make the website available and functional on every device.

### Scope
The project aims to develop an online booking and reviewing platform called "Happy Valley Holidays" that facilitates users in viewing, booking, reviewing and managing reservations and reviews. The platform will be responsive and user-friendly, providing features for user registration, reservation and review creation, profile management, messaging, favoriting listings, and seamless navigation.

Key Features:

1. Initial Project Setup:

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.

2. Responsive Design:
-The website will be responsive, allowing users to access it on both desktop and mobile devices.

3. User Authentication:
- Users can register an account, providing access to all functionality of Happy Valley Holidays.
- Registered users can log in to view their profile, reservationss and reviews.

4. Profile Management: (Future feature)
- Registered users can view and edit their profiles, including personal details and profile pictures.
- Users can reset their passwords in case they forget them.
- Users can delete their profiles and associated reviews and reservations.

5. Review Management:
- Users can perform CRUD on their reviews and profiles.
- The highest rated reviews will be displayed above the footer on the landing page.
- Reviews and (reservations) will include title, description and images.

6. Pagination:
- Pagination will be implemented for easy navigation through pages of reviews.

7. Notification Messages:
- Users will receive notification messages when performing CRUD operations, login/logout, and signup actions.

8. Benefits:

1. User-Centric Experience: The platform focuses on the user's needs, allowing efficient browsing, reservation and review creation, and communication.
2. Efficient Navigation: Users can easily navigate through different sections of the website for seamless access.
3. Effective Communication: Notification messages enhance user communication.

## Design
### Colour Scheme
The website features a calming and professional color palette that combines shades of blue, violet, and green with complementary neutrals. <br>
Overall, this color scheme creates a professional and user-friendly environment, with subtle variations in hue and transparency to guide users' attention and enhance the visual appeal of the website.


### Database Schema
![Database ERD]()


#### Models
1. Allauth User Model

The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, name, password, and more. This model is used for user authentication, hence why changes directly to this model are not advised. The User model is connected to the Profile model with one to one relationship. 

2. ...

3. ...

4. ...

5. ...

6. ...

### Fonts
The font used in this project is... <br>

### Wireframes
- Home
![desktop]()



### Agile Methodology
#### Overview
This project was created using agile principles. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### EPICS(Milestones)
The user stories are grouped into eight EPICS or Milestones. An additional Milestone called Project Backlog was created to manage any additional features, bugs, or tasks that may arise during development. <br>


#### User Stories issues
The structure of the user story issue consists of the user story, acceptance criteria, and tasks that outline the steps that are required for this issue to be completed. <br>

During development where possible, the commit messages are connected to their corresponding issues. <br>


#### MoSCoW prioritization
This prioritization technique was used to effectively prioritize the features and requirements of the project based on their importance. The acronym "MoSCoW" stands for "Must have, Should have, Could have, and Won't have." Each category helps categorize and prioritize features to guide the development process and ensure that the most critical elements are addressed first. <br>


#### GitHub Projects
The project was created using a basic Kanban Board structure, divided into columns such as Todo, In Progress, Done, and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow. <br>


## Features
### Navbar
The navbar is a component that is present on all pages. It was created using Bootstrap and is fully responsive. The HVH logo which serves as a link to the homepage is located on the left side on the navbar. On the right are the nav links which allow the user to easily navigate through the website from any point. If the user is not authenticated the links displayed are Home, Listings, and Login/Signup.

![Navbar]()

 If the user is authenticated they will see Home, About, Change Password and Logout. The user's username is displayed to indicate that the user is logged in. For a better user experience, each nav link when active is bolded to let the user know the page they are currently on.

 ### Footer
 The footer consists of information about boutique ado and their contact details. To help the users connect with boutique ado there are icons with links to social media which open in a new tab. 

 ![Footer]()

### Home
#### Hero Section
The choice of hero image carousel for the website serves a specific purpose: it immediately communicates the main purpose of the website. The text overlay, "Find Your Next Holiday" directly connects the image to the website's purpose. It encourages users to take action and search for their ideal vacation, making the website's primary function clear right from the start. The image of the three main attractions, Hafren forest, Llanidloes town and Llyn Clywedog reservoir were carefully selected to create an immediate and powerful connection between the user and the website's mission, inviting them to explore the website further.

![hero carousel]()

#### Home Page Section
This section displays...

![Home Page Section]()

#### Next Section
The next section is designed to present...

![Next Section]()

### Next Section

The next section is designed to present...

![Next Section]()

The next section is designed to present...

![Next Section]()

The next section is designed to present...

### About Page
This page displays a picture of the site owner with a decription of the purpose of the site.

![About Page]()

### Profile Page
This page can be accessed only by authenticated users. It consists of a sidebar menu with links for Profile, My Reservations, and My Reviews. The profile page is essentially a large card that includes the user's profile details like name, user name, email, and about me. Underneath, there are two buttons one for edit profile and one for delete profile.


#### Toast Messages
Toast messages were used every time the user performs CRUD operation, sign in, and sign out.

![Messages]()

### Sign In page
Consist of a form with username and password. Below it has a link to reset password, followed by a sign in button which submits the form. The register link is position below that.

![Sign In]()

### Sign Up page
Consists of a form with name, email, username, password, and password confirmation. Below it has a link to log in if the user already has an account. Below that is the signup button. The user is sent a welcome email to the email provided and is redirected to the profile page update form to customize their profile

![Sign up]()

### Sign out confirmation
When the user clicks on the log out link in the nav, they are redirected to the confirmation page. This page consist of warning message and two buttons- one to go back and one to log out.

![Sign out]()

### Edit Profile
The edit profie page renders a form with prefilled fields with the existing information for this user. It consists of profie image, name, username, email, phone, town, county and about me section. Below that is the submit button which will update the profile details once submitted. 

### Delete Profile Confirmation
This page consists of warning message with two buttons - one to go back and one to delete the profile. Delete profile is in red to indicate danger. Once clicked the profile is deleted and the user is redirected to We are sorry to see you go page

### We are sorry to see you go
This page confirms that the profile was deleted. The user is presented with a flash message confirming the profile was deleted successfully. Below that there is a button to go back to the home page.

### Password reset
This page prompts the user to enter their email address. An email with instructions is then sent to their email and the user is redirected to a page that informs them about the email being sent.

![Password Reset]()

### Enter a new password
When the user follows the link from the email, they are sent to a page to set up their new password.

### Password Reset Completed
Once the form is submitted the user is redirected to a page advising them the password reset was completed followed by a log-in button.

### Error Pages
- 404

![Password Reset]()


## Future Features
1. 
2. 
3. 
4. 

## Testing
Testing documentation can be found [here.](/testing.md)

## Bugs

|Bug|Status|
| ---| ---|
|[BUG: Deployment error]()

## Problems Solved


## Technologies And Languages
### Languages Used
- HTML
- CSS
- JavaScript
- Bootstrap
- Python
- Django
- Toast
- Cloudinary
- PostgresQL


### Python Modules

- dj-database-url - This library is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.

- gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

- Pillow - Pillow is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

- psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

- whitenoise - Whitenoise is a middleware for serving static files directly from your Django application.


### Technologies and programs

- [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as a starting point for the project.
- [Pixelmator Pro](https://www.pixelmator.com/pro/) was used for creating the mockup images of the website during planning stage as well as formatting images.
- [Google Fonts](https://fonts.google.com/) was used to import fonts.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used during the testing of the website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Js Hint](https://jshint.com/) was used to validate the JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.

## Deployment
### Before Deployment
To ensure the application is deployed correctly on Heroku it is mandatory to update the requirements.txt. This is a list of requirements that the application needs in order to run.

- To create the list of requirements we use the command pip3 freeze > requirements.txt. This will ensure the file with the requirements is updated.

- Then commit and push the changes to GitHub.

! Before pushing code to GitHub ensure all credentials are in an env.py file, which is included in the .gitignore file. This tells Git not to track this file which will prevent it from being added to Github and the credentials being exposed.

### Deployment on Heroku
- To deploy the project on Heroku, first create an account.
- Once logged in, create a new app by clicking on the create app button
- Pick a unique name for the app, select a region, and click Create App.
- On the next page select the settings tab and scroll down to Config Vars. If there are any files that should be hidden like credentials and API keys they should be added here. In this project, there are credentials that need to be protected. This project requires credentials added for:

1. SECRET_KEY
2. DATABASE_URL
3. CLOUDINARY_URL

- Scroll down to Buildpacks. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python
- From the tab above select the deploy section.
- The deployment method for this project is GitHub. Once selected, confirm that we want to connect to GitHub, search for the repository name, and click connect to connect the Heroku app to our GitHub code.
- Scroll further down to the deploy section where automatic deploys can be enabled, which means that the app will update every time code is pushed to GitHub. Click deploy and wait for the app to be built. Once this is done, a message should appear letting us know that the app was successfully deployed with a view button to see the app.

### Creating a fork
1. Navigate to the repository
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description 
4. Choose to copy only the main branch or all branches to the new fork. 
5. Click Create a Fork. A repository should appear in your GitHub

### Cloning Repository
1. Navigate to the repository
2. Click on the Code button on top of the repository and copy the link. 
3. Open Git Bash and change the working directory to the location where you want the cloned directory. 
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.

## Credits
### Media
- [Images]()
- [More images]()
- [More images]()
- [404 image]()


### Code
- Learned how to setup django project and deploy to Heroku from CI Django Blog walkthrough, MS3 project and www.codemy.com youtube videos.
- I learned how to use advanced Django concepts from Feddie my django tutor, referred by my mentor Brian.

### Acknowledgements
- Huge thank you to my mentor Brian...
- The Slack community and especially Steven Powell, Axe DeKlerk and Robert Jonah Lewis  who listened to my struggles during development.
- Feddie G. for the brilliant Django suggestions to research.

### Comments

user logins:

Admin:
User:

This project consists of x apps - ... 

