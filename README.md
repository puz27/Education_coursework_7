"# Education_coursework_7" 

## WORK WITH DJANGO DRF
### Allow to create habits scheduler and make notification to user telegram bot
## Requirements.
* Python
* Rest
* Postgres
## Installation
* Download repo
* Install requirements (pip install -r requirements.txt)
* Run service Rest
## Prepare 
* prepare .env file (examples in .env_sample)
* create database for postgres
* prepare migrations (python .\manage.py makemigrations)
* make migrate (python .\manage.py migrate)
* prepare test user (optional) (python .\manage.py prepare_platform)
* prepare telegram bot for send information (you can use default configuration @habitscheduler2023_bot)
## Start service
* run command: celery -A config worker -l INFO
* run command: -A config beat -l info -S django
* python manage.py runserver
## Work with API (habits)
* http://127.0.0.1:8000/api/v1/habits/ - show all habits that user has access
* http://127.0.0.1:8000/api/v1/habit/<int:pk>/ - show user's habit detail information
* http://127.0.0.1:8000/api/v1/habit/create/ - create habit
* http://127.0.0.1:8000/api/v1/habit/update/<int:pk>/ - update habit
* http://127.0.0.1:8000/api/v1/habit/delete/<int:pk>/ - delete habit
* http://127.0.0.1:8000/api/v1/share_habits/ - show all public habits
## Work with API (users)
* http://127.0.0.1:8000/api/v1/users/show/ - show all users
* http://127.0.0.1:8000/api/v1/users/show/<int:pk>/ - show user's detail information
* http://127.0.0.1:8000/api/v1/users/update/<int:pk>/ - update user information
* http://127.0.0.1:8000/api/v1/users/delete/<int:pk>/ - delete user information
* http://127.0.0.1:8000/api/v1/users/registration/ - register user
* http://127.0.0.1:8000/api/v1/users/token/ - get token for user
* http://127.0.0.1:8000/api/v1/users/token/refresh/ - refresh user token

## Examples work with interface
### User authorization
![authorization.PNG](authorization.PNG)
### User registration
![registration.PNG](registration.PNG)
### Habit creation
![create.PNG](create.PNG)

### Description Create Request format
* place - place of user habit
* action - what to do
* award - what user get for his not pleasant habit
* duration - duration of habit (less than 121 seconds)
* is_public - public or private habit
* is_pleasant - flag for pleasant or not pleasant (usual) habit
* frequency - daily habit or you can check day of week (MONDAY-SUNDAY)
* time - when execute user habit
* link_pleasant - usual (not pleasant) habit can have pleasant habit(in this case no award)

## Additional
* Author: Avramenko Nikolay
* Date of release: 2023/08/09