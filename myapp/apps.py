from django.apps import AppConfig

# Define a custom AppConfig for your 'myapp' app

class MyappConfig(AppConfig):
    # Specify the default auto-generated field for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
