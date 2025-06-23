Description:
------------
A full-stack Django web application that allows users to register, login, and manage their own card collection.

This project was focused on showing Django built-in features.
This application makes use of Django objects, forms, authentication, SQLite database, template tags, and Q queries.

Users will register an account, login into their account and then have an empty card table which they can add cards to with the "Add Card" button.
This will take the user to the add card form where the information related to the card can be entered and then added to the database.
Existing cards can be updated with the "Edit" button or removed from the database with the "Delete" button.

The cards can be filtered with the search bar which will filter the cards based on what is searched for, showing only cards that match the query.

Authentication is done using the built-in Django authentication and users’ card lists are associated with only their account and must be logged in.


How to use:
-----------

Clone the repository
--------------------
git clone https://github.com/MitchBresette/DjangoCardApp.git
cd card_app

Create and activate a virtual environment
-----------------------------------------
python -m venv venv
.\venv\Scripts\activate

Install dependencies
--------------------
pip install -r requirements.txt

Run migrations to set up the database
-------------------------------------
python manage.py migrate


Run server
----------
python manage.py runserver

Access at the link provided
---------------------------
 http://127.0.0.1:8000/

