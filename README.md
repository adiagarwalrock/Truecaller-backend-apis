# Truecaller like API Backend using Django REST Framework 

## Aim:
*To create a REST api to be consumed by a mobile app, which is somewhat similar to various popular apps which tell if a number is spam, or allow user to find a person’s name by searching for their phone number.*


## Terminology:
- Each registered user of the app can have zero or more personal “contacts”.
- The `global database` is basically the combination of all the registered users and their personal contacts (who may or may not be registered users).


## Data to be stored for each user:
- Name
- Phone Number
- Email Address


## Registration and Profile:
- A user has to register with at least name and phone number, along with a password, before using. He can optionally add an email address.
- Only one user can register on the app with a particular phone number.
- A user needs to be logged in to do anything; there is no public access to anything.

## Asumption
- The user’s phone contacts will be automatically imported into the app’s database -no need to implement importing the contacts.


## Spam:
- A user should be able to mark a number as spam so that other users can identify spammers via the global database. Note that the number may or may not belong to any registered user or contact - it could be a random number.


## Search:
1. A user can search for a person by name in the global database. 
   1. Search results display the name, phone number and spam likelihood for each result matching that name completely or partially. 
   2. Results should first show people whose names start with the search query, and then people whose names contain but don’t start with the search query.
2. A user can search for a person by phone number in the global database. If there is a registered user with that phone number, show only that result. Otherwise, show all results matching that phone number completely.
  
        Note: that there can be multiple names for a particular phone number in the global database, since contact books of multiple registered users may have different names for the same phone number.
3. Clicking a search result displays all the details for that person along with the spam likelihood. But the person’s email is only displayed if the person is a registered user and the user who is searching is in the person’s contact list.


## Data Population:
- For testing a script or other facility will be written that will populate the database with a decent amount of random, sample data.


<hr>


## Setting up project on Ubuntu

- Create a Virtual Environment. Here env is the environment name

        python3 -m venv env

- Activate the Environmnt to Install the dependencies:

        source env/bin/activate

- Install the dependencies from requirements.txt file:

        pip install -r requirements.txt

- Now the Django App is ready to run using:

        python manage.py runserver

<hr>

## NOTE:

* ```sqlite3``` Database is included along the code, but the code is also readyto run with MySQL databases. To do so uncomment the database config in ```apis.settings.py```

* Please perform migrations prior running databases other than what's included.

* Django Username and Password--> ```admin and admin```. 

<hr>

Contact me at  [aditya.ag1234@gmail.com](mailto:aditya.ag1234@gmail.com)