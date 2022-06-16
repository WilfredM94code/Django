# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# -----------------------------------------------------------------

# Django is a framework used to create web app/sites. It is meant to
# provide an ecosystem including a layer for user, for admin, CRUD 
# within databases. For the particular purpuse of this chapther, 
# there will be created a web app to plan/schedule meetings

# Django follows the MVT design pattern (Model View Template).

# 1 - Model - The data you want to present, usually data from a database.
# 2 - View - A request handler that returns the relevant template and 
# content - based on the request from the user.
# 3 - Template - A text file (like an HTML file) containing the layout 
# of the web page, with logic on how to display the data.

# This particular Django content will be structured in a different way,
# which means that there will be two folders within the resources folder:
# one with the lessons enumerated and separated between .py, .html., .css 

# For this project there will be created a virtual environment

# Once created and activated a virtual environment there has to be created
# a Django project by using the next command in the terminal:

# django-admin startproject appname

# Where 'appname' is (you guessed right) the name of de app meant to be 
# developed. In wichever is the CWD for this virtual environment a new folder
# will be created with the name of the web app. This provides a project 
# template within this file. On the 'appname' folder there will be created 
# a file called 'manage.py' and another file with the appname. Within this 
# embeded folder there will be created several files listed below

# __init__.py
# asgi.py
# settings.py
# urls.py
# wsgi.py

# Each of this files are created by the command 'django-admin startproject appname'
# Each file is filled with a stablished Django format, and in some cases a 
# particular syntax meant to be interpreted by the Django user

# To run the Django server there has to be used the next command line
# In the webapp main folder (not the embeded one)
# Note that for this particular charter there has been used a Mac PC for
# which every command will be adapted to that reality

# python3 manage.py runserver

# Once runned the server there will be created a file within the embeded
# 'appname' folder called 'db.sqlite3'

# When running the server, it's content will be accesible within the 
# 'http://127.0.0.1:8000/' addres from every prefered web browser available
# in the PC. It will display an awesome default website when accessed. 
# This site will be available whenever the server is in DEBUG mode.

# Django will be also be displaying  the HTTP log from the terminal offering 
# a view on the requests made to the server, the response offered to the 
# user and time as shown below:

# [12/Jun/2022 08:24:14] "GET / HTTP/1.1" 200 10697
# [12/Jun/2022 08:24:14] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
# [12/Jun/2022 08:24:15] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
# [12/Jun/2022 08:24:15] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
# [12/Jun/2022 08:24:15] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
# Not Found: /favicon.ico
# [12/Jun/2022 08:24:15] "GET /favicon.ico HTTP/1.1" 404 2110
# [12/Jun/2022 08:28:22] "GET / HTTP/1.1" 200 10697
# [12/Jun/2022 08:28:22] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
# [12/Jun/2022 08:28:22] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 304 0
# [12/Jun/2022 08:28:22] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
# [12/Jun/2022 08:28:22] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0



# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# --------------------- Creating a Django app ---------------------
# -----------------------------------------------------------------

# A Django webapp is considered as a folder storing a set of Python files
# meant to interact with each other and to be deployed in a Django server

# A WEBAPP can contain several APPS and it is considered a good practice to
# store each app or functionallity separated one from another. This means
# that SEVERAL APP CREATE A WEB APP

# To start an app in Django there has to be used the next line of code within
# a terminal that previously acceded the virtualenv:

# Note that the terminal must be in the 'appname' main directory

# python3 manage.py startapp app_1

# This execution will result in a new folder  called 'app_1' nested in the
# 'appname' main directory containing a folder called 'migrations' and the next
# set of Python files:

# __init_.py
# admin.py
# apps.py
# models.py
# tests.py
# views.py 

# For the purpose of this course there will be erased every file within this 
# app besides the '__init_.py' and 'views.py' file. 

# To make an app visible to Django there app name, which in this case
# is 'app_1' has to be included within the 'settings.py' file, particulary in
# the 'INSTALLED_APPS' list, at the end of it. Note that is required to ad a 
# comma at the end of the app name

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ------------------------- Adding a page -------------------------
# -----------------------------------------------------------------

# To create a page there has to be accessed the 'views.py' within the app
# from this file there has to be created a view function, which is a function
# created to designate how a webpage will behave. To create a view function then
# there has to be provided a function using the corresponding syntax shown 
# below

# from django import HttpResponse

# def welcome (response):
#     return HttpResponse('Welcome to the first app developed in Django, feel yourself proud')

# To asign an URL to the web page there has to be included within the 'urls.py'
# the instruction to import the view function designed for this new page and 
# then there has to be added within the 'urlpatterns' list a 'path' object
# containing the name of the URL for this new page and the view function as 
# an argument. This process will result in a 'urls.py' that looks like this

# from app_1.views import welcome

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('welcome.html', welcome),
# ]

# Once create this web page it can accessed after running the server and then
# providing the right url  which in this case is

# http://127.0.0.1:8000/welcome.html

# For practical porpuses the 'welcome' view function will be linked to an empty
# URL. The empty URL is the landing page

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ---------------------- Django flow control ----------------------
# -----------------------------------------------------------------

# The flow control of a Django application will be dictated by the view function
# which will be proccessed by the Django server for every HTTP request recieved 
# by an user.

# Once the Django server is running it will recieve an HTTP request linked to
# a particular URL, and whenever this happens the server calls the view 
# function associated with that URL and the will format a response according
# to the return of the view function. The view function will be executed 
# whenever the URL associated is requested in the Django server

# Any URL requested without an view function will return an error 

# Django server refreshes the execution of each file if a change is detected
# alowwing to run always the most updated version of the webapp without
# interrupting any functionallity.

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ----------------------- Initial migrations ----------------------
# -----------------------------------------------------------------

# Django modules are Python classes. In Django a Model class is mapped to a
# database tables, subsequently each object of that model can be stored in a 
# row in a table. This means that any time a model class is modified the 
# corresponding table/columns has to be seted to store the required object
# and this process is automate by migrations. This automates the process
# of creating databases and tables by only setting the migrations.

# By default there will be several migrations 'pending' to be setted up. 
# This is displayed in the terminal whenever the server is running under the
# following message 

# You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
# Run 'python manage.py migrate' to apply them.

# These migrations can be detailed using the next command in the terminal.
# Note that to display correctly this info the terminal CWD must be the 
# 'nameapp' main directory

# python3 manage.py showmigrations

# This command will return the following result

# admin
#  [ ] 0001_initial
#  [ ] 0002_logentry_remove_auto_add
#  [ ] 0003_logentry_add_action_flag_choices
# auth
#  [ ] 0001_initial
#  [ ] 0002_alter_permission_name_max_length
#  [ ] 0003_alter_user_email_max_length
#  [ ] 0004_alter_user_username_opts
#  [ ] 0005_alter_user_last_login_null
#  [ ] 0006_require_contenttypes_0002
#  [ ] 0007_alter_validators_add_error_messages
#  [ ] 0008_alter_user_username_max_length
#  [ ] 0009_alter_user_last_name_max_length
#  [ ] 0010_alter_group_name_max_length
#  [ ] 0011_update_proxy_permissions
#  [ ] 0012_alter_user_first_name_max_length
# contenttypes
#  [ ] 0001_initial
#  [ ] 0002_remove_content_type_name
# sessions
#  [ ] 0001_initial

# This default migrations, once applied, will create a table within the 
# database for every app of the Django webapp, building columns corresponding 
# to each field previously displayed

# Each migration is a Python script that makes a change to the database 
# corresponding to a piece of Python code in a Model class

# This migrations can be applied using the next command:

# python3 manage.py migrate

# Once executed it will return the next content:

# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying auth.0012_alter_user_first_name_max_length... OK
#   Applying sessions.0001_initial... OK

# This execution has taken place in the 'db.sqlite3' database which content
# can be displayed using SQLite3 DB browser.

# For instance, this migration creates a table using the next SQL statement:

# CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE) 

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# -------------------------- Model class --------------------------
# -----------------------------------------------------------------

# A new app will be created called 'app_2'. From this new app there will
# removed the 'apps.py' and 'test.py' file. This app will be setted 
# within the Django app

# To the create a model this has to be declared withi 'models.py' file
# and then there has to be created a class using the following syntax:

# from django.db import models

# Create your models here.

# class App2(models.Model):
#     date = models.DateTimeField() 
#     title = models.CharField(max_length=200)

# The App2 inherits the attribute 'Model' from the class 'model' of the 
# 'django.db' module

# This particular class instantiates several methods of the 'models' module.
# These methods

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ---------------------- Creating and running ---------------------
# --------------------------- Migrations --------------------------
# -----------------------------------------------------------------

# Once modified the 'models.py' file by adding new models and attributes
# each model can create new migrations meant to stage changes within the 
# webapp database. To create such migrations there hasve to be executed 
# the next command on the terminal

# python3 manage.py makemigrations

# Once executed this command there will be displayed on the terminal
# the next output:

# Migrations for 'app_2':
#   app_2/migrations/0001_initial.py
#     - Create model App2

# This means that fro the 'app_2' there has been created a migration file
# places within the next path:

# app_2/migrations/0001_initial.py

# This created the model 'App2' which is the only model declared within the
# 'models.py' file.

# The '0001_initial.py' contains the Django abstraction of a SQL query which
# can be deployed using multiple SQL paradigms such as SQLite, PostgreSQL,
# MySQL, etc.

# This abstraction is written in Python and has the next structure:


# from django.db import migrations, models

# class Migration(migrations.Migration):

#     initial = True

#     dependencies = [
#     ]

#     operations = [
#         migrations.CreateModel(
#             name='App2',
#             fields=[
#                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('title', models.CharField(max_length=200)),
#                 ('date', models.DateTimeField()),
#             ],
#         ),
#     ]


# To stage this migrations there has to be executed the next command:

# python3 manage.py sqlmigrate app_2 0001

# Note that to stage the migrations from a file there can be provided just the
# number or id of the migration and it will be executed. Once executed, such 
# command will return the next output:

# BEGIN;
# --
# -- Create model App2
# --
# CREATE TABLE "app_2_app2" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "date" datetime NOT NULL);
# COMMIT;

# If runned the server it will display this particular message refering to the
# unapplied migrations:

# You have 1 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): app_2.
# Run 'python manage.py migrate' to apply them.

# To apply this migrations there has to be executed the next command line
# as previously shown:

# python manage.py migrate

# Once executed the terminal will display the next message:

# Operations to perform:
#   Apply all migrations: admin, app_2, auth, contenttypes, sessions
# Running migrations:
#   Applying app_2.0001_initial... OK

# The result can be seen in the 'db.sqlite3' file where the 'app_2_app2' table was
# created refering to the 'app_2' app of the 'webapp' Django app and the 
# 'App2' model from the 'models.py' file

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ------------------------ Admin interface ------------------------
# -----------------------------------------------------------------

# This is an autogenerated interface provied by Django. It's useful to create
# and edit Model data. The Model meant to be managed by the admin has to be 
# registred within the 'admin.py'. To do so there has to be employed the next
# syntax:

# from .models import App2

# admin.site.register (App2)

# Note that to provide the submodule 'models.py' to the submodule 'admin.py'
# when being both submodules of the same app a '.' has to be provided to the
# imported submodule

# Once this instruction is saved there has to be created a superuser which
# will be the user role allowed to manage the webapp

# To create such user there has to be provided from the 'webapp' main folder
# the next command:

# python3 manage.py createsuperuser

# Once executed the terminal will return several messages to setup a superuser

# To check the creation of the superuser the application must be runnig and
# then accessed the 'http://127.0.0.1:8000/admin' URL and then log in using
# the superuser info. This will display the admin interface.

# From it there will be provided access to the available app from the 'admin.py'
# file called 'app_2' and to the 'App2' model database. Once accessed this
# particular Model there can be provided input to this data by using the 
# '+add' button, filling the fields and the saving the values by clicking
# one of the saving options availables. Once saved, this values will be 
# displayed as an 'App2 object' and by selecting it there can be modified,
# saved or removed such values


# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ----------------------- Adding fields to ------------------------
# ----------------------- an existing model -----------------------
# -----------------------------------------------------------------

# Whenever a Model is modified it will return the next message if the model was
# previously used to provide a migration and if the related table had stored
# values

# It is impossible to add a non-nullable field 'duration' to app2 without specifying a default. This is because the database needs something to populate existing rows.
# Please select a fix:
#  1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
#  2) Quit and manually define a default value in models.py.
# Select an option:

# This means that there has to be provided a default value to the field of the
# already stored data within the database since these values cannot be NULL
# or not existing.

# Whatever this value is there has to be considered that a default value will 
# be placed for such fields

# To add a default value within the 'models.py' file there has to be provided
# the 'default' keyword and a value as shown below.

# from datetime import time
# # Create your models here.

# class App2(models.Model):
#     title = models.CharField(max_length=200)
#     date = models.DateField()
#     start_time = models.TimeField(default=time(9))
#     duration = models.IntegerField(default=1)

# In the admin interface, whenever is provided a new registry for the database
# and stored the panes shows 'App2 object'. To provide a specific text for 
# every row theres a megic method meant to be setted and has to be provided
# in the format below:

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# --------------------- Model and migrations ----------------------
# --------------------------- workflow ----------------------------
# -----------------------------------------------------------------

# 1 - Every new Model has to defined inheriting the 'models.Model' class methods
# 2 - Once defined the new model and saved there has to be executed the 
# 'python3 manage.py makemigrations' command on the terminal having the 
# webapp folder as CWD
# 3 - Once the migrations are included within the 'migrations.py' file there
# has to be executed the next command from the terminal 
# 'python3 manage.py migrate' 

# To stablish a relation between two tables of a database there has to be
# provided the column within the Model definition and it has to be used the
# next syntax:

# class App2(models.Model):
#     title = models.CharField(max_length=200)
#     date = models.DateField()
#     start_time = models.TimeField(default=time(9))
#     duration = models.IntegerField(default=1)
#     room = models.ForeignKey(App3, on_delete = mode.CASCADE) 
#     def __str__(self):
#         return f'Meeting for {self.title} at {self.start_time} on {self.date}'

# class App3(models.Model):
#     name = models.CharField(max_length=200)
#     floor = models.IntegerField()
#     room_number = models.IntegerField()
#     def __str__(self):
#         return f'{self.name}: Room {self.room_number} on floor {self.floor}'

# Note that within the 'App2' Model theres a reference to the 'App3' Model
# This relation supposes the creation of a column that references as a 
# foreign key the 'App3' Model. The 'on_delete' dicatetes the behaviour of
# the table row of the model 'App2' if a referenced row of the 'App3' model
# is deleted. In this case, if a referenced row is deleted the rest of the 
# entries will be deleted.

# To have a cleaner code there will be deleted the database and the migrations
# app file. There will be staged every step made until this point including
# creating a new superuser

# It will also be deleted the 'app_1' from the project

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ---------------------- Model View Template ----------------------
# ---------------------------- Pattern ----------------------------
# -----------------------------------------------------------------

# As seen at the beginning Django follows the MVT design pattern 
# (Model View Template).

# 1 - Model - The data you want to present, usually data from a database.
# 2 - View - A request handler that returns the relevant template and 
# content - based on the request from the user.
# 3 - Template - A text file (like an HTML file) containing the layout 
# of the web page, with logic on how to display the data.

# There will be created a new app called 'website' and every file created 
# whit the app creation command will be erased except for the __init__.py
# and 'views.py'

# To store templates there has to be created a 'templates' folder within the
# 'website' folder. It is considered a good practice to create a folder 
# for every app of the Django app. Since the app dedicated to process the
# website is the 'website' there will be created a folder within the 
# 'template' folder called 'website'. Take a rest, you just saw too much
# redundance. Within this folder there will be created a file called
# 'home.html' 

# Given this particular configuration of folders there has to be provided a
# change within the 'settings.py' file, particulary in the 'TEMPLATES'
# variable. Within this variable there's a 'DIR' keyword. The value has
# to be changed to the next value:

# 'DIRS': [BASE_DIR / 'website/templates'],

# This way Django will look within the templates folder 'within' the 'website'
# app folder

# Within the 'website' app there has to be created a view function in
# the 'views.py' file that calls the 'home.html' file and it has to be called
# within the 'urls.py' file. 

# Kind of confusing, I know. This mindfuck can be reverted if created a 
# 'templates' folder within the 'webapp' folder and then nesting the folder
# of each app within this 'templates' folder. This way there has to be
# modified the 'DIRS' keyword of the 'settings.py' file. The value will be
# the following:

# 'DIRS': [BASE_DIR / 'templates'],

# This fix will be canon, IDK, IDC.


# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ----------------------- Template Variable -----------------------
# ------------------------------ and ------------------------------
# ------------------------ Dynamic content ------------------------
# -----------------------------------------------------------------

# The templates used by Django employ HTML files that are processed and then
# passed as an HTML file with dynamic generated data to the user.

# This templates allows to pass variables that are declared within the HTML
# format. This have the same syntax as the Jinja variables, looking like
# this:

# <p>{{ message }}</p>

# To pass such value to the template there has to be provded a dictionary 
# containing the variable name as the keyword and the value meant to be
# passed to the variable.

# This dictionary has to be passed as an extra argument of the 'render()'
# function returned by the viewfunction as shown below

def welcome (resquest):
    return render(resquest,'website/home.html',{'message': 'Beautiful static variable'})

# This variables can be placed in any place of the template

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ----------------------- Reading data from -----------------------
# -------------------------- a database ---------------------------
# -----------------------------------------------------------------

# Django allows to call data from a database an pass it as a template variable

# Data is meant to be called usign the Model. This model has to be called 
# from the 'views.py' file and the data processed within the function view 

# There are seveal data that can be requested from the database unsing the 
# model methods. There's an example below

def welcome (resquest):
    variables = {
        'message': 'Beautiful static variable',
        'num_meetings' : App2.objects.count(),
    }
    return render(resquest,'website/home.html',variables)

# Every model has its own method that can be used within the view fucntion.
# In the next example there will be shown a particular  example onto how to 
# call data from the database using Model methods

def details (resquest,id):
    detail = App2.objects.get(pk=id)
    variables = {
        'meeting': detail,
    }
    return render(resquest,'app_2/detail.html',variables)


# Note that this view function will 'get' values from the database using a 
# primary keyword to identify the particular row. Note that this can only 
# happen if there's an ID provided. This ID will be provided (temporarily) by
# the user from the URL. To allow Django to recieve such value from the user
# in the form of the URL it has to be specified whenever the user provides
# the URL. This is specified using the next syntax:

# path('meetings/<int:id>', details)

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ----------------------- Return a 404 page -----------------------
# -----------------------------------------------------------------

# Whenever is requested a non existing/defined URL from the server Django 
# provides a particular either error page which is useful to the developer.
# Besides of being useful to the developer is 'unfriendly' to the user, that's
# why it comes handy to provide a friendly page when the server returns a 404
# response

# Django provides a way to deal with the error providing a 404 response page 
# for any pages with server errors

# This is achieved by importing the 'get_object_or_404' object.
# This object is used the next way:

from django.shortcuts import render, get_object_or_404
from .models import App2

def details (resquest,id):
    detail = get_object_or_404 (App2, pk=id)
    variables = {
        'meeting': detail,
    }
    return render(resquest,'app_2/detail.html',variables)

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ----------------------- Adding data to the ----------------------
# --------------------------- home page ---------------------------
# -----------------------------------------------------------------

# To dynamically add data to a site there has to be called an iterable in the 
# view function and passed in the 'render' function. This way the iterable
# can be processed from the server to dynamically add data to the website.

# The template has to provide the loop instruction with a particular syntax
# shown below:

# <ul>
#     {% for meeting in meetings %}
#     <li>
#         <a href="/meeting/{{ meeting.id }}"> {{ meeting.title }} </a>
#     </li>
#     {% endfor %}
# </ul>

# The logic block starts with the {% for meeting in meetings %} and defines
# a variable for each iteration (meeting) of the iterator (meetings). This 
# proces recreates the structure standing from the start of the logic block
# to the end denotated by the {% endfor %} instruction for each iteration.

# A set of objects passed to the 'render' function can be called using the 
# next model methods:

# App2.objects.all()

# The data gathered from this method will return every value related to the
# table associated to the model in the form of an iterable that can be
# processed and displayed as the template indicates

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ------------------------- Link building -------------------------
# -----------------------------------------------------------------

# If changed an 'href' attribute within a template there has to be modified the 
# 'urls.py' reference to such URL and the same is applied to the opposite 
# modification. Whenever a change is done to an URL there has to be modified
# any reference to such URL making the maintenance of such code complicated
# if a Django app consist's in 10th on 100th templates interconnected

# Link building allows to preserve a link rerference whenever is required to
# maintain the code alowwing to keep an consistent URL grid. 

# Within the urlpaths of the 'urls.py' file there has to be added a keyword 
# called 'name' which value has to be expressed as a string aliasing the URL.

# path('meetings/<int:id>', details, name = 'detail'),

# Then this value can be referenced by appliying the template variable as 
# shown below:

# <ul>
#     {% for meeting in meetings %}
#     <li>
#         <a href="{% url 'detail' meeting.id %}"> {{ meeting.title }} </a>
#     </li>
#     {% endfor %}
# </ul>

# Note that the argument passed to the URL is (an attribute) 'meeting.id'

# This proccess is repeated to provide a home button within the 'details'
# template

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ------------------------- Listing rooms -------------------------
# -----------------------------------------------------------------

# To provide a list with al rooms there has to be created a view funtion,
# an dedicated url and a template. This data will be linked to the home page.

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ---------------------- Best practices for -----------------------
# --------------------- URL, Mappings and Apps --------------------
# -----------------------------------------------------------------

# To handle app's URLs there can be created a file storing the set 'URL' paths
# for each app and then call, from the Django app 'urls.py', the set of URLs.

# This process demands the next steps: 
# 1 - Creation of an 'urls.py' file within the app folder
# 2 - Setting the path objects with the urls, view functions and names:

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('rooms', room_list, name = 'room_list'),
#     path('rooms/<int:id>', room, name = 'room'),
#     path('<int:id>', details, name = 'detail'),
# ]


# 3 - Import the app's new urls.py file from the Django app ulrs.py and include
# the content properly

# from django.contrib import admin
# from django.urls import path, include

# from website.views import welcome

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', welcome, name = 'welcome'),
#     path('meetings/', include('app_2.urls')),
# ]

# Note that when creating the reference to the 'app/urls.py' file there is
# provided a prefix. This prefix will be placed before every URL declared 
# within the 'app/urls.py' file.

# Note that there has to be imported the include object from the django.urls
# module. It recieves the string that includes the name of the app and the 
# name of the file sotirng the path objects. 

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# ------------------- Create a template with a --------------------
# --------------------------- ModelForm ---------------------------
# -----------------------------------------------------------------

# A ModelForm is an object used by the viewfunction to provide a relation 
# between a Model and a form which provides to a template the capability
# to pass data directly from a form to a database.

# This is achieved by importing the 'modelform_factory' function from
# the 'django.forms' module

# The syntax used to create a ModelForm object is shown below:

ModelForm = modelform_factory(App2,exclude=[])

# Note that this function recieves the model and also a keyword called 
# 'exclude'. This keyword recieves a list with the fields meant to be 
# ingnored within the form of a string with the name of the field as shown 
# below:

ModelForm = modelform_factory(App2,exclude=['date'])

# The way this object is included within the view function is shown below

def form(request):
    variables = {
        'form' : ModelForm()
    }
    return render(request,'app_2/form.html',variables)

# The ModelForm object is an object meant to be rendered under a template 
# variable that once interpreted will provide a set of fields directly on the
# HTML file. For this, the template has to provide the variable and this way
# offer an HTML file with every field linked to a Model/ database table. 

# The template and the URL has to be provided to the Django app to run properly

# Django creates these forms considering the type of data for which the Model
# defines each field.

# To submit a form there has to be provided a button that is meant to pass 
# the for data to server. This button has to be place within the form tag 
# of the template. To alow the form to pass data to the server it has to be
# provided the attriute method with the value 'POST' as shown below:

# <form method="POST">
#     <table>
#         {{ form }}
#     </table>
#     <button type="submit">Create meeting</button>
# </form>

# There's a piece of information required by Django to proceed with the 
# acceptance of a submission to the database and it is a CSRF token.

# CSRF stands for CROSS SITE REQUEST FORGERY which is an attack on which
# another user, using logged-in users credentials, tries to create an HTTP
# request with the methods POST, PUT, or DELETE to interact with the DB.
# To avoid these type of attacks on the server Django allows the usage of a
# token to prevent this type of attack and such token is provided within the
# form tag meant to be protected as shown below

# <form method="POST">
#     <table>
#         {{ form }}
#     </table>
#     {% csrf_token %}
#     <button type="submit">Create meeting</button>
# </form>

# If excluded such token there wont be a possibility to proceed with the
# POST method of the HTTP request.

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# --------------------- Processing user input ---------------------
# -----------------------------------------------------------------

# Even there can be passed data to the server, if the viewfunction doesn't
# provide way to process the POST method of the HTTP request the data
# wont be passed to the DB table. Thats why there has to be created a 
# flow control within the viewfunction to provide a behaviour whenever the
# request has the 'POST' method.

def form(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = ModelForm()
        variables = {
            'form' : form
        }
    return render(request,'app_2/form.html',variables)

# The request method is checked, in case there has been recived a 'POST'
# method there will be passed the post attribute of the request to the
# designated ModelForm for this particular Model. This object has the 
# method 'is_valid()' to check if each field is recieving data according
# to the actual conditions/constraints of each field/column of the 
# Model/table of the database. 

# Thanks to the 'is_valid()' method user will recieve a message whenever 
# the user provides an problematic input

# -----------------------------------------------------------------
# ----------------------------- Django ----------------------------
# --------------------- Custom form fields and --------------------
# -------------------------- validations --------------------------
# -----------------------------------------------------------------

# Django provides the flexibility to actually create a validation of a form
# allowing a safe way to recieve data from the user without compromising the
# database and app integrity.

# To provide a particular setting to a form within of the app there has to 
# be created a 'form.py' file. Within this 'form.py' file there was 
# provided a code to deliver this solution easily. This example was created
# to adap to the needs of this simple webapp

from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

from .models import App2

class App2ModelForm(ModelForm):
    class Meta:
        model = App2
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': TimeInput(attrs={"type": "time"}),
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "4"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meetings cannot be held in the past")
        return d

# There is a particular Django submodule that allows to format the fields
# of a ModelForm object. This is the 'django.forms' sub module. It provides
# a set of pbjects that Django processes as the settings of the form fields
# related to a Model. For this example this set of objects are:
# ModelForm, DateInput, TimeInput, TextInput, IntegerField

# Django also provides a set of exceptions that can be used whenever
# there is an invalidation of the data passed to the server within a form.
# In this case the 'django.core.exceptions' provides a 'ValidationError'
# exception that can be raised by the missmatching of a condition. This
# exceptions are shown in the webpage to the user whenever such missmaching
# condition occurs

# The class App2ModelForm inherits its atructure from the ModelForm.
# To provide the adequate constraints for each field in a way that is shwon
# within the browser form, there has to be provided a class called Meta
# which has to store several attributes to give format to the App2ModelForm
# class. These attributes are:
# model : The model that provides the structure of the form
# fields: an specification of the fields meant to be considered of the Model
# widgets: A dictionary containing as a keywords every field meant to be 
# formated which values are the object that matches the description of the
# field when the model was defined (To have a clear idea there can be useful
# to check the 'models.py' file of the webapp and whatch to the 
# corresponding object assigned from the 'django.db' module and match
# the object type). This object recieves a set of attributes in the form of 
# a ditionary under the 'attrs' keywordargument.
# To validate the data theres defined (or overrided) the method 
# 'clean_date()' which checks for the data provided in each field and 
# validates if such value is in conditions. 

# To make this code run there has to be importe to the 'view.py' file that
# will employ this tweeked version of the 'ModelForm' object