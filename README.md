Notes App
A simple and user-friendly Notes Management Web Application built using Django and Django REST Framework (DRF).
The application allows users to create, view, edit, and delete notes through a Django-based frontend. It also provides a REST API for performing CRUD operations on notes.

Features
Create new notes
View all notes
Edit existing notes
Delete notes
Add categories to notes
Pin notes
Archive notes
Display note creation date
Django template-based frontend
Django REST Framework API
DRF Browsable API
SQLite database
Responsive dark-themed UI

Technologies Used
Python
Django
Django REST Framework
HTML
CSS
JavaScript
SQLite
Git & GitHub

Note Model
The application uses a Note model with the following fields:
Field -	Description
title -	Title of the note
content -	Main content of the note
category -	Category of the note
is_pinned -	Indicates whether the note is pinned
is_archived -	Indicates whether the note is archived
created_at -	Date and time when the note was created
updated_at -	Date and time when the note was last updated

CRUD Operations
The application supports all four basic CRUD operations.
Create
Users can create a new note by entering:
    Title
    Content
    Category
    Pinned status
    Archived status

Read
All saved notes are displayed on the home page.

Update
Users can click the Edit button to modify an existing note.

Delete
Users can delete an existing note using the Delete button.

Django REST Framework API
The project also provides a REST API using Django REST Framework.
Method    	Endpoint	          Operation
GET      	/api/notes/	        Get all notes
POST	    /api/notes/     	  Create a note
GET	      /api/notes/<id>/  	Get a specific note
PUT	      /api/notes/<id>/  	Update a note
PATCH	    /api/notes/<id>/  	Partially update a note
DELETE	  /api/notes/<id>/  	Delete a note

Serializer
NoteSerializer is responsible for converting Django model instances into JSON data and validating incoming API data.

ModelViewSet
NoteViewSet provides the standard CRUD operations automatically.

Router
DefaultRouter automatically creates the API URL patterns for the ViewSet.

Learning Objectives
This project demonstrates practical knowledge of:
Django project and app structure
Django Models
Django Views
Django Templates
Django Template Tags
Django URL routing
HTML forms
CSRF protection
CRUD operations
Django ORM
Django REST Framework
Serializers
ModelViewSet
Routers
REST API endpoints
SQLite
Git and GitHub
