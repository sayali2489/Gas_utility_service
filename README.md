# Django Gas Utility Service Application

This Django application is designed for a gas utility company to manage customer service requests, track request statuses, and provide tools for customer support representatives. The application allows customers to submit service requests online, view account information, and monitor the status of their requests. Customer support representatives can manage requests and assist customers through the admin interface.

## Features

1. **Service Requests**: Customers can submit requests for different types of services, provide details, and attach files if needed.
2. **Request Tracking**: Customers can view the status, submission date, and resolution date of their requests.
3. **Account Information**: Customers can view their account details, such as username and email.
4. **Request Management**: Customer support representatives can manage service requests through an admin interface, update statuses, and provide support.
5. **User Authentication**: The app supports user login, logout, and password management.

#Create a superuser for accessing the admin interface:(on terminal)
python manage.py createsuperuser

#Run the development server:
python manage.py runserver

#Access the application in your web browser:
Customer interface: http://localhost:8000/service_requests/
Admin interface: http://localhost:8000/admin/



