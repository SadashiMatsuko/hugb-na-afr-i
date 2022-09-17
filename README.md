All programming and testing were done in Pycharm

Quick start guide running the application(PC):
Under the app folder in src there is another folder called STthLane, that is the root folder for the django project.
Start by creating a venv in the django project root.
Then activate the venv by running the active file in the scripts folder under the venv folder.
Then install django, django-nose, coverage and psycopg2 (you might have to install the binary version: psycopg2-binary).
After that in the terminal write "./manage.py runserver" this will.


Quick start guide to Testing the project(PC):
The root folder for testing is src (otherwise it's a pain to import from the application).
From a command Promt window find your way to the project-group-17\src\app\STthLane folder.
There you should run the command manage.py test ../../test --keepdb.