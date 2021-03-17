# full_throttle
1)Install all the requirements from the requirement.txt file.
2)Go the settings.py file and change Database configuration according to your system (i have used DB as PGAdmin)
3)Navigate to project folder which has manage.py and Run below commands:
a)python manage.py makemigrations
b)python manage.py migrate

4)python manage.py runserver 127.0.0.1:<port_no> 

5)Once server is up and running , go and hit the urls (present in task_app/urls.py) using postman

ex:
http://127.0.0.1:8001/task/register/


Param to pass with below apis:

path(r'save_org/', views.save_org_api),
no param , data is taken from task_project.config

path(r'register/', views.register_api),
firstName
lastName
email
password
confirm_password
username
org_id
mobile_no
address
logitude
latitude

path(r'login/', views.login),
username
password

path(r'add_task/', views.add_task_api),
assigned_to (pass user_id value from UserProfile table)
task_name
status (pass 2 which denotes assigned)

Note :
1)user_id of currently logged in user will be taken from request.user.id
2)In task table , the data for assigned_by and assigned_to will have id not user_id from UserProfile 

path(r'get_task/', views.get_task_api),
user_id

(This user id will be the data from ser_id field of UserProfile)