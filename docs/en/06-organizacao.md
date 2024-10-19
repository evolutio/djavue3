# 🗂️ Folders and project organization

## 🦄 Backend

### Layers

```
                                           ___ Models
                                          /
 Client -->   API       --> Services --> ORM
             urls+views                   \___ Manager
             Schemas        Rules

```

- **Client**: Anything that does HTTP calls to the API
- **API**: It has route definitions and input data validation, with little or no business rules. Redirects the data to the service layer.
- **Services**: Pure Python modules with the implementation of business rules; it is the layer that must be tested the most.
- **ORM**: Data mappping in the database

### Folders structure

Overview

```shell
twitterclone                       👉 Root folder
 ├── README.md
 ├── manage.py                     👉 Django CLI (Entry point)
 ├── requirements.txt              👉 Main dependencies
 ├── requirements-dev.txt          👉 Local dependencies (may change in Poetry mode)
 ├── docker-compose.yml            👉 Docker descriptor to run locally
 ├── Dockerfile                    👉 Recipe to run the project
 ├── tox.ini
 ├── uwsgi.ini
 └── twitterclone                  👉 Project base
    ├── base                       👉 App for rules outside the "core"
    │   └── ...
    ├── accounts                   👉 App related to users and authentication
    │   └── ...
    ├── core                       👉 Main app with the core business
    │   └── ...
    └── twitterclone               👉 Centralizes project settings
        ├── api.py
        ├── settings.py            👉 Main Django settings
        ├── urls.py                👉 Main/initial configuration of Django routes
        └── wsgi.py
```

Django has the concept of "apps", with the goal of separating your project contexts. Instead of having everything in the main app, we are able to create new apps (e.g. sales, purchases, inventory, reports, blog) in order to group similar functionalities. Each app follows the structure below:

```
   urls --> views --> service --> models
   1) Routes          2) Rules    3) Database
```

```shell
├── core                       👉 Django app root to centralize a solution for a given context
│   ├── apps.py                👉 As an app\'s __init__
│   ├── urls.py                👉 1) Routes definition (with django-ninja the urls are empty)
│   ├── views.py               👉 1) Routes implementation
│   ├── schemas.py             👉 1) Definition of the name/type attributes
│   ├── service                👉 2) Business rules implementation
│   ├── models.py              👉 3) Definition of the tables to store the data
│   ├── migrations             👉 3) History of how to create/alter tables in the database
│   ├── admin.py               👉 Configuration of the data accessible through the back-office
│   ├── tests                  👉 Centralizes app tests
│   └── templates              👉 Not used in API apps, but can generate HTML page

```
## 🎨 Frontend

::: danger 🚧 TODO

You can help here!
:::