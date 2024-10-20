The Library Management System API is designed to manage library resources, allowing users to borrow, return, and view books. Built using Django and Django REST Framework (DRF), this API handles backend logic, database management, and efficient API design. It includes features such as user authentication, book management, and transactional tracking of borrowed books.

Table of Contents
Features
Project Setup
API Endpoints
Models
Authentication
Technologies Used
Future Enhancements
License
Features
Books Management (CRUD):

Create, Read, Update, and Delete books.
Books include attributes such as Title, Author, ISBN, Published Date, and Number of Copies Available.
Validation of unique ISBN numbers.
Users Management (CRUD):

Create, Read, Update, and Delete library users.
Users include attributes such as Username, Email, Date of Membership, and Active Status.
Check-Out and Return Books:

Endpoint to allow users to check out and return available books.
Tracks the date of borrowing and returning, adjusting available book copies.
View Available Books:

Endpoint to view all books and filter by availability.
Query filters for searching by Title, Author, or ISBN.
Authentication:

Basic authentication using Django’s built-in system.
Optionally, token-based authentication (JWT) can be implemented.
Overdue Book Tracking (Stretch Goal):

Tracks overdue books with potential penalty systems for late returns.
Project Setup
Prerequisites
Python 3.8 or higher
Django 4.x
Django REST Framework
MySQL database
Steps to Install and Run the Project
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/LibraryManagementSystemAPI.git
cd LibraryManagementSystemAPI
Create a virtual environment and activate it:

bash
Copy code
python3 -m venv env
source env/bin/activate  # For Windows, use `env\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up MySQL database:

Install and configure MySQL.
Create a new database for the project.
bash
Copy code
CREATE DATABASE library_management;
Update settings.py to configure MySQL:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_management',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Run migrations:

bash
Copy code
python manage.py migrate
Create a superuser for accessing the admin panel:

bash
Copy code
python manage.py createsuperuser
Run the server:

bash
Copy code
python manage.py runserver
API Endpoints
Endpoint	Method	Description
/api/books/	GET	List all books or create a new book
/api/books/<int:id>/	GET	Retrieve, update, or delete a book
/api/users/	GET	List all users or create a new user
/api/users/<int:id>/	GET	Retrieve, update, or delete a user
/api/transactions/	POST	Check out or return a book
/api/available-books/	GET	View all available books
Example Request for Creating a Book
bash
Copy code
POST /api/books/
Content-Type: application/json
{
    "title": "Django for Beginners",
    "author": "William S. Vincent",
    "isbn": "9781735467221",
    "published_date": "2020-05-21",
    "available_copies": 10
}
Models
Book Model
title: CharField
author: CharField
isbn: CharField (unique)
published_date: DateField
available_copies: IntegerField
User Model
username: CharField
email: EmailField
date_of_membership: DateField
is_active: BooleanField (for user status)
Transaction Model
user: ForeignKey (related to User)
book: ForeignKey (related to Book)
date_borrowed: DateTimeField
date_returned: DateTimeField (nullable)
Authentication
Django’s Session Authentication is implemented.
Permissions are set so that only authenticated users can access certain endpoints.
Technologies Used
Django: Web framework for the backend.
Django REST Framework: For building the RESTful API.
MySQL: As the database to store and manage information.
Python: Backend programming language.
Future Enhancements
Implement JWT for token-based authentication.
Track overdue books and impose penalties.
Send email notifications for overdue or available books.
Add pagination and search functionality to the API.
License
