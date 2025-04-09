To set up the development environment:

1. Prerequisites:
- PyCharm for Professionals
- PostgreSQL (Use default configurations, KNOW YOUR PASSWORD)
- Python installed on System (3.9+)
- Git and Github

2. Creating a New Django Project in PyCharm
a. Open PyCharm -> New Project
b. Choose Django
c. Set the following
- Location: your project folder
- (Note: If not done already, can create a git repository by checking the respective box)
- Interpreter type: Project venv
- Under Advanced Settings, Check "Enable Django Admin"

3. Install psycopg2 (PostgreSQL adapter for Python)
- In terminal type: pip install psycopg2-binary

4. Run the Queries listed in Discord
  
5. Configure settings.py and update the DATABASES section:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mood_tracker',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

6. Make Migrations and Run Server
In terminal type the following:
- python manage.py makemigrations
- python manage.py migrate
- Python manage.py runserver
