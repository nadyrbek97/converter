# Youtube Video Downloader

## Installation Project and Dependencies

### In command line 

    $ git clone https://github.com/nadyrbek97/converter
    $ virtualenv venv -p python3
    $ source venv/bin/activate
    $ cd converter
    $ pip install -r requirements.txt
    
### Before running project server 

#### 1. Create .env file in project directory and add SECRET_KEY
    
    $ SECRET_KEY = "your_secret_key"
    
#### 2. Migrate migration files

    $ python manage.py migrate
  
#### 3. Create superuser 

    $ python manage.py createsuperuser
    
#### 4. And run your server 

    $ python manage.py runserver
    
### Test

    $ python manage.py test