# asset-api

## Setup
1. Create a virtual environment using  below command although it is optional:
   ```
   python3 -m venv venv
   ```
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run server:
   ```
   python manage.py runserver
   ```

## Directory structure
```text
asset_management/
├── assets/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── asset_management/
│ ├── settings.py
│ ├── wsgi.py
│ └── urls.py
├── manage.py
├── requirements.txt
└── README.md
``

