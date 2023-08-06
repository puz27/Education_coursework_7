"# Education_coursework_7" 
coverage run --source='.' manage.py test
coverage report
python3 manage.py test habits.tests.HabitTestCase