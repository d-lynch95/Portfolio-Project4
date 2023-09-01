# Happy Travels appointment booking service

HappyTravels appointment booking service is a web based booking application to allow users to book appointments in a local travel agency. The users are given the possibility to make an account, create a booking, and then edit or delete their bookings. This site  was developed using Python (Django), HTML, CSS and by storing the data in a PostgreSQL database.


[Live Website]()
![AmiResponsive Mockup](assets/media/dungeonresponsive.png)

## User Goals and Stories

### User goals
- As a user I want to
  - easily and intuitively navigate throughout the website
  - browse the website naturally and with ease
  - be able to view the website and read all information on all screen sizes
  - Create an account on the website
  - Make an appointment at my preferred time and date
  - Manage my appointments and change and delete them if needed

### Business owner goals
- As the website business owner I want to 
  - As the website business owner I want to
  - Provide users information about the services provided
  - Allow users to easily access and use the site.
  - Allow users to create appointments.
  - Allow users to manage their own appointments
  - Allow users to edit and delete their appointments
  - Collect user information
  - Allow staff to access and edit appointments
  - Provide contact information to users


### User Stories

#### As a user
  - As a user I want to visit the website and understand it’s purpose immeditately
  - As a user I want to easily understand how to use the website
  - As a user I want to be able to contact the business owner
  - As a user I want to create an account easily
  - As a user I want to input my information with ease
  - As a user I want to create an appointment with ease
  - As a user I want the ability to view my appointments
  - As a user I want the ability to change my appointments
  - As a user I want the ability to delete my appointments
  - As a user I want the ability to create multiple appointments
  - As a user I want to have an enjoyable experience
  - As a user I want to return to the site to create another appointment



#### As a website business owner
  - As a site owner I want to excite users and peak their interest
  - As a site owner I want to allow for a good user experience
  - As a site owner I want to allow the user to easily navigate the website without issues
  - As a site owner I want to encourage users to create an account
  - As a site owner I want to encourage users to create appointments
  - As a site owner I want to encourage users to create an account
  - As a site owner I want the user to have a positive experience by allowing them to edit or delete their own appointments


#### As a new user
  - As a new user I want to navigate the page intuitively and with ease
  - As a new user I want to understand the page purpose upon first viewing
  - As a new user I want to see company contact information
  - As a new user I want to be able to contact the company directly
  - As a new user I want to see the company’s social media presence
  - As a new user I want to easily create an account
  - As a new user I want to easily create an appointment
  - As a new user I want to edit or delete an appointment 
  - As a new user I want to enjoy the experience and return to make another appointment

## Design

### Font
The design of this website is a very simple style as the format template was provided by the code institute. This program predominantly focuses on the Python programming language so does not incorporate CSS or styling features. The code uses minimal colour as an homage to the original text-based adventure games. The only colour in the game is red text showing "Game Over" when the player loses the game. The game also uses ASCII text showing "Escape the dungeon" when the player starts the game

### Structure

This website has a simple single page design. This format was easiest as the template was provided by the Code institute.


### Design flow chart

This game flow and logic was designed using lucidchart. This was the first time using lucidchart so the chart is quite basic as it was made during the original genesis of the game. The game has since grown in size and stature and more text has been added to bulk up the options.


# Development

## Agile Methodology

This project was developed using the Agile methodology. All epics and user stories implementation progress was tracked through Github projects Kanban Board which can be found here.

<Insert screenshot of Kanban board>


This project had 5 main epics (Milestones)

I. Epic 1. Initial Set up
  - As a developer, I need to create the base.html page and structure so that other pages can reuse the layout
  - As a developer, I need to create static resources so that images, css and javascript work on the website
  - As a developer, I need to set up the project so that it is ready for implementing the core features
  - As a developer, I need to create the footer with social media links and contact information
  - As a developer, I need to create the navbar so that users can navigate the website from any device


II. Epic 2.  USER REGISTRATION/AUTENTHICATION
  - As a developer, I need to implement the Register page using the django-allauth module
  - As a developer, I need to implement the Login page using django-allauth module
  - As a developer, I need to implement the  Logout modal using django-allauth module
  - As a site owner, I would like the allauth pages customized to that they fit in with the sites styling
    

III. Epic 3 - Making appointments
  - As a user, I would like to be able to create a new appointment when I want to visit the travel agnecy
  - As a user, I would like to view my bookings when I need to check the information
  - As a user, I would like to be able to edit a booking so that I can make changes when needed
  - As a user I would like to delete a booking when I no longer require it




IV. Epic 4 - Deployment Epic  
  - As a developer, I need to deploy the project to heroku so that it is live for users
	
V. Epic 5 - Documentation
  - Complete readme documentation






## Technologies used
- Python
  - The main language used in this project was python
- HTML
  - The website contains a little bit of HTML
- CSS
  - The templates used from CI include some CSS
- GitHub
  - The website is hosted on GitHub
- GitPod
  - The website was developed on GitPod
- Git 
  - used to commit and push code during development
- Heroku
 - The game is hosted on heroku
- Convertio.co
  - [This](https://convertio.co/) site was used to convert jpg and png files to webp files
- LucidChart
 -The gameplay flow chart was designed on lucid chart


## Features 

### Existing Features

- __Title Graphic__

  - This graphic uses ascii text to create a large graphic that shows the game title "Escape The Dungeon". This graphic adds to the user experience and adds more flair than a simple text based game.

![Title Graphic](assets/features/ASCII-text.webp)

- __External Libraries__

  - This project used several external libraries
  - We imported the time and os modules, we also imported colorama and pyfiglet.
  
  ![Libraries](assets/features/import.png)

- __List__

  - This program includes a list which players use as an inventory
  - As players pick up items during their journey they are added to the inventory
  - Players can easily cycle through their inventory using keyboard prompts

![List](assets/features/list.png)

- __Input__

  - This game relies hevily on user input in order to progress the story.
  - This was added to the game using input boxes at each decision point

![Input](assets/features/input.png)


- __Functions__

  - This project reused a lot of sections of code. In order to save time and space functions were used heavily.
  - The main functions used regularly were fin() which allows the user to exit the game, validate() which validates user input and reprompts them if input is not valid and inventory() which allows the user to print the list containing their inventory items.
  
  ![Functions](assets/features/function.png)
  

### Features Left to Implement

- I would like to add a typewriter effect to the game when I have more time to develop it.

- I would like to add more path directions to expand on the story.

- I would also like to add more options and more interactivity with the inventory items. The user currently has two keys remaining and I would like to add more options for these keys when time permits.

## Testing 

### BUGS
 - I encountered several bugs while creating this project.

- I faced bugs when creating the views and urls files when launching the project. This was resolved using advice from tutor support.

- I also faced issues with the urls.py files in both the project folder and the app folder. This was fixed by adding the path('', include('booking.urls')), line of code to the project urls.py file. 

- I faced issues when trying to include mixins to function based views. I fixed this by changing to class based views following the advice of a youtube tutorial.

- I was having issues with the formatting of some of the database fields once they had been formatted using summertime as the html tags were still showing. I changed this using {x.name|safe}

- When creating the URLS I had both functions and class based views pointing to the same URL's. This was causing issues with loading the page. Once this was corrected the issue resolved itself.

- I was having issues getting the database information to print to the desired webpage. This was due to using the incorrect naming convention on the for loop. Once I corrected the name to object_loop the page loaded correctly.


### User Testing

The application was tested on a macbook air using the google chrome browser.


### Validator Testing 

- Python
  - No errors were found when passing through the [CI code linter](https://pep8ci.herokuapp.com/#)
  ![CI python Code Linter](assets/features/Python-Validation.webp)

### Manual Testing

#### Functional Testing 

I tested each of the pathways through the game individually to make sure there were no dead ends of any issues.
I ran through all of the functions and tested each option to record whether there were any issues. All of the functions passed the manual user testing and there were no issues with the code.

![Testing functions](assets/features/functiontest1.png)
![Testing functions](assets/features/functionTest2.png)



### Unfixed Bugs
 - There are no current bugs that we're aware of.


## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Main Branch
  - Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://escape-the-dungeon.herokuapp.com/

- Clone the Repository Code Locally
  - Navigate to the GitHub Repository you want to clone to use locally:

  - Click on the code drop down button
  - Click on HTTPS
  - Copy the repository link to the clipboard
  - Open your IDE of choice (git must be installed for the next steps)
  - Type git clone copied-git-url into the IDE terminal
  - The project will now of been cloned on your local machine for use.

- Heroku 
  - The project was deployed using Code Institutes mock terminal for Heroku

  - Deployment steps:

    - Fork or clone this repository.

    - Ensure the Profile is in place.

    - requirements.txt can be left empty as this project does not use any external libraries

    - Create a new app in Heroku

    - Select "New" and "Create new app"

    - Name the new app and click "Create new app"

    - In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list)

    - Whilst still in "Settings", click "Reveal Config Vars" and input the folloing. KEY: PORT, VALUE: 8000. Nothing else is needed here as this project does not have any sensitive files

    - Click on "Deploy" and select your deploy method and repository

    - Click "Connect" on selected repository.

    - Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section

    - Heroku will now deploy the site


## Credits 

### Content 

- The format and template for the README file was borrowed from the [Code institute](https://codeinstitute.net/ie/).

- The image conversions from jpg to webp were done with [Convertio](https://convertio.co)


### Coding help

- The outline template for the Python was provided by the [Code Institiute](https://www.codeinstitute.com)

- I also took a lot of inspiration from the Code institute I think Therefore I blog Walk through [Code Institiute](https://www.codeinstitute.com)

- A lot of the python coding was done with help from the tutorial pages at [w3schools](https://www.w3schools.com/)

- The Django documentation was one of the main resources I used during development [Django Documentation](https://docs.djangoproject.com/en/4.2/)

- The following YouTube videos were very useful in production [LearnDjangoin20minutes-TechWithTime](https://www.youtube.com/watch?v=nGIg40xs9e4&t=2s), [PythonDjangoDentistWebsite](https://www.youtube.com/@Codemycom), [BuildADoctorWebsiteWithDjango](https://www.youtube.com/watch?v=3_3q_dE4_qs), [HowToCreateABookingSystemForAHealthClinic](https://www.youtube.com/watch?v=s5xbtuo9pR0), I also used the follow along blog [HowToCreateABookingSystemForAHealthClinic](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78)

- The code for the form came from the following repository [DentistGitHub](https://github.com/flatplanet/dentistDjango/blob/master/website/templates/home.html). This was the repository for the [PythonDjangoDentistWebsite](https://www.youtube.com/watch?v=rHZwE1AK1h8&list=PLCC34OHNcOtrZnQI6ZLvGPUWfQ6oh-D6H&index=11)

- I followed the guidance of [this](https://www.youtube.com/watch?v=RwWhQTSV44Q) youtube tutorial to help create the ctud functionality for my website

- The tutor support team from codeinstitute were extremely helpful in helping me to overcome bugs in my code.

- I used countless stack overflow entries to help me to solve minor django related bugs.

- I used the following projects as inspiration for my project. [TennisBuddies](https://github.com/lucia2007/tennis_buddies), 

- I used the following tutorial for help with my requirements.txt file [LearnPython](https://learnpython.com/blog/python-requirements-file/)

 - I also received help from the following slack users for minor bugs or style changes inc21, Tatiana Ruffo, Dave T, Laura, Jo_ci and I received a lot of help and advice from my mentor Gareth McGirr and from Paul Thomas our cohort leader.
