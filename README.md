# Fixer API

This repository holds the **API** for the [Fixer website](https://fixer-web-production.up.railway.app/) (demonstration deploy), which is a **portal** where **citizens and city hall** can **centralize communication about urban issues**, **reporting**, **upvoting** and **resolving** from the most urgent to the least rushed ones.

## 🔧 Setup

First of all, you'll need to **install** the project **dependencies**, which are listed in the `requirements.txt` file. Most of the cases, it's recommended that you do so in a **virtual environment**. Here's **how to create and activate** a _venv_:

``` sh
# Creates a virtual environment in a .venv folder
python -m venv .venv
# Activates the virtual environment (bash)
source .venv/Scripts/activate
# Activates the virtual environment (powershell)
.venv/Scripts/activate
```

Now, you can **install the dependencies** from the `requirements.txt` file with:

``` sh
pip install -r requirements.txt
```

> To **execute this project** make sure to **have a `.env` file with environment variables configured** as examplified in the `.env.example` file (**don't let comments in your `.env` file**, as that's not correctly parsed by the system yet).

You'll also **need a Postgres instance** to which you'll connect via the variables you define. For that, a `docker-compose.yml` is provided, which spins up the required instance also using configuration from `.env`. Besides Postgres, the `docker-compose.yml` also runs an **instance of the API itself**.

If it's the **first time** you run the project, you'll also need to **migrate the database** with:

``` sh
# Create any new migrations from models
python manage.py makemigrations

# Apply pending migrations to the DB
python manage.py migrate
```

<!-- Finally, to create a default user, you can use this command:

``` sh
echo "from django.contrib.auth import get_user_model; \
  user_model = get_user_model(); user = user_model.objects.create(username='admin'); \
  user.set_password('admin'); user.is_staff = True; user.is_superuser = True; \
  user.save()" | python manage.py shell
``` -->

## ▶️ Executing

When you have the setup ready, you'll be able to **execute the project in development mode** with:

``` sh
python manage.py runserver
```

## 📚 Documentation

A PostMan workspace with examples of route uses can be found [here](https://nadjiels-team.postman.co/workspace/4452a508-db89-4483-a5cc-066be3a5e30e), though currently, this is privately available.
