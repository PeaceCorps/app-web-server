# Update Schema Guide

## Introduction

Follow this guide if you have made changes to the database schema and you want the changes to be reflected in your PostgreSQL database.

All commands are to be run on the machine where the application has been installed.

If you installed the application on a VM, start up the VM and run the following commands on the VM.

This guide assumes that the project is running on Django version **1.6.x**. If you are using Django version **1.7** and above, then you may use the built-in database migration tool (see below).

**Warning**: The instructions below will drop the current `webapp` database and all information stored in this database will be lost.

## Login to PostgreSQL Client

    psql -U myuser -d postgres -h localhost -W

You will be prompted to enter a password. If you followed **Installation Guide.md** to install the application, the default password is `mypassword`.

You can list PostgreSQL databases by running the following command:

    \l

We will be dropping the `webapp` database.

## Drop Database

Drop the `webapp` database by running the following command:

    drop database webapp;

If you list PostreSQL databases again, you should **not** see the `webapp` database in this list.

    \l

Exit the PostgreSQL client by running the following command:

    \q

## Create `webapp` Database

Create a database called `webapp` by running the following command:

    createdb -U myuser webapp

You will be prompted to enter a password. If you followed **Installation Guide.md** to install the application, the default password is `mypassword`.

## Generate Database Tables

Change directory to where `manage.py` is located.

To view the sql commands that will be generated from `syncdb`, run the command:

    python manage.py sqlall app_name_here

Then run the following command to create database tables that correspond to the Django models of the project:

    python manage.py syncdb

After running the syncdb command, you should get the following prompt. Type in `yes`:

    You just installed Djano's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): yes

Create a superuser with the following credentials (for now):

    Username: admin
    Email: your email
    Password: mypassword

## Verify Creation of Database Tables

Check that the tables were created by starting the PostgreSQL client:

    psql -U myuser -d webapp -h localhost -W

You can view database tables by running the following command:

    \dt

Make sure to exit the PostgreSQL client before proceeding to the next steps:

    \q

**You have now updated the database schema!**

For additional instructions on starting the development server and trying out the application on your browser, please refer to the instructions in **Installation Guide.md**

## Update Django REST API Serializers

If you made changes to the database models related to the API (such as adding a new model field/database column), then you may need to update the corresponding serializers found in **serializers.py** in your app directory.

## Upgrading to Django 1.7 or above

Django 1.7 introduced built-in database migration support. After this project has been ported to Django 1.7 or above, the built-in migration tool can be used instead.

[https://docs.djangoproject.com/en/dev/releases/1.7/#schema-migrations](https://docs.djangoproject.com/en/dev/releases/1.7/#schema-migrations)
