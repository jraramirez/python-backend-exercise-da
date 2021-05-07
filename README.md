# Introduction 

Python Backend Blueprint

# Getting Started
## 1. Installation Process
1. Python `3.6` or `3.7`
2. Install VirutalEnv [Installation instructions](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html)
3. Create Virtualenv

    In the `termnial`, go to project's directory and run

        python3 -m venv env

4. Run virtual environment

    While still on the terminal and on the projects directory run

        source venv/bin/activate

5. Install project dependencies 

    make sure virtual environment is activated

        pip install -r requirements.txt

6. Run this project

    make sure virtual environment is activated

        python manage.py runserver

## API Endpoints

    items/


## Exercise

1. Using the ORM, add an additional field `color` to the `Item` model. Use the appropriate field type that you think is the best. Add a default value for existing items. When done, migrate the changes.

2. Using the ORM, create a new model `Vehicle`. Add fields `id`, `name`, and `manufacturer`. When done, migrate the changes.

3. Create an endpoint for the new model created in number 2. This endpoint should be able to accept GET and POST methods