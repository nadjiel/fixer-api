# Fixer API

This repository holds the API for the Fixer website, which is a portal where citizens and city hall can centralize communication about urban issues, reporting, upvoting and resolving from the most urgent to the least rushed ones.

## 🔧 Setup

First of all, you'll need to install the project dependencies, which are listed in the `requirements.txt` file. Most of the cases, it's recommended that you do so in a virtual environment. Here's how to create and activate a venv:

``` sh
python -m venv .venv
source .venv/Scripts/activate
```

Now, you can install the dependencies with:

``` sh
pip install -r requirements.txt
```

To execute this project make sure to have a `.env` file with environment variables configured as examplified in the `.env-example` file.

You'll also need a Postgres instance to which you'll connect via the variables you define. For that, a `docker-compose.yml` is provided, which spins up the required instance also using configuration from `.env`.

If it's the first time you'll run the project, you'll also need to migrate the database with:

``` sh
python manage.py makemigrations
python manage.py migrate
```

Finally, to create a default user, you can use this command:

``` sh
echo "from django.contrib.auth import get_user_model; \
  user_model = get_user_model(); user = user_model.objects.create(username='admin'); \
  user.set_password('admin'); user.is_staff = True; user.is_superuser = True; \
  user.save()" | python manage.py shell
```

## ▶️ Executing

When you have the setup ready, you'll be able to execute the project with:

``` sh
python manage.py runserver
```

## 📚 Documentation

A PostMan workspace with examples of route uses can be found [here](https://nadjiels-team.postman.co/workspace/4452a508-db89-4483-a5cc-066be3a5e30e), though currently, this is privately available.
