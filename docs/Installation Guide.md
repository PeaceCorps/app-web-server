# Installation Guide
## Requirements

This tutorial assumes that the user is installing and running the project under the Ubuntu Virtual Machine that is provided by PeaceCorps.

## Table of Contents
1. [Install Python3.6](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#install-python3.6)
2. [Install git](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#install-git)
3. [Clone Project](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#clone-project)
4. [Install Django and PostgreSQL](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#install-django-and-postgresql)
5. [Install VirtualBox and Vagrant](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#install-virtualbox-and-vagrant)
6. [Download PeaceCorps Ubuntu Virtual Machine](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#download-peacecorps-ubuntu-virtual-machine)
7. [Using Vagrant](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#using-vagrant)
8. [Install Project Dependencies](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#install-project-dependencies)
9. [Setup PostgreSQL](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#setup-postgresql)
10. [Update settings.py](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#update-settingspy)
11. [Generate Database Tables Corresponding to Django Models](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#generate-database-tables-corresponding-to-django-models)
12. [Run Development Server](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#run-development-server)
13. [Try out Mobile App Control Center](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#try-out-mobile-app-control-center)
14. [Exit the Virtual Machine](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md#exit-the-virtual-machine)

## Install Python3.6

By default, your PC has Python 2.7 installed. To install Python 3.6, follow the steps below:

To install some build dependencies:

    sudo apt install build-essential checkinstall
    sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

Then, download Python 3.6 source code from python.org by the following command:
    
    wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz

Next, we extract the tarball:

   tar xvf Python-3.6.0.tar.xz

Now change directory into the source directory, configure the build environment and install:

    cd Python-3.6.0/
    ./configure
    sudo make install

## Install git

If you don't already have git, you can download it [here](http://git-scm.com/downloads). You must then install git.

## Clone Project

Clone the project from GitHub by running the following command:

    git clone project_url_here

For our project, this would correspond to:

    git clone https://github.com/systers/macc.git

## Install Django and PostgreSQL

If you are installing and running the project on your local machine and not on the PeaceCorps VM, then you will need to download and install the following software:

1. [Django](https://www.djangoproject.com/download/) (version == 1.11)
2. [PostgreSQL](http://www.postgresql.org/download/) (version >= 9.5.5, version 9.6 preferred)

Skip the next two sections if not using the PeaceCorps VM and jump to the section '**Install Project Dependencies**'. 


**Skip this section if you are installing and running the project on the PeaceCorps VM, as Django and PostgreSQL are already included in the PeaceCorps VM.**

## Install VirtualBox and Vagrant

The Virtual Machine provided by PeaceCorps will be downloaded in a later step. We must first install VirtualBox and Vagrant.

The VirtualBox and Vagrant installers can be downloaded from the following websites:

1. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](http://www.vagrantup.com/downloads.html)

Install VirtualBox and Vagrant by running the installers.

## Download PeaceCorps Ubuntu Virtual Machine

A Vagrant file is located in the [top level directory for the project.](https://github.com/systers/macc/blob/develop/Vagrantfile) found on GitHub. In case you do not have a copy of this Vagrant file, here are it's contents:
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provider :virtualbox do |vb|
    vb.gui=true
  end
  config.vm.box = "pc-web-dev"

  # config.vm.box_url = "../box/pc-web-05192014-i386.box"
  config.vm.box_url = "http://54.183.32.240/vagrant/box/pc-web-05192014-i386.box"

Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 80, host: 8080,
  auto_correct: true
end
  config.vm.network "forwarded_port", guest: 8000, host: 8001
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network "public_network"

end
```
Save this file as **Vagrantfile** (if you don't already have this file) in the top level directory for the project.

To download the VM, run the following command:

    vagrant up

You must wait a few minutes for the VM to be downloaded completely.

## Using Vagrant

The `vagrant up` command also boots the Virtual Machine.

Once the VM download has completed, upon boot, it may ask you to choose an `Available bridged network interface`. The first option wil work in most cases.

You may come across a message that says `default: Warning: Remote connection disconnect. Retrying...` This message means that the VM is still booting up which is why we cannot establish a connection with it. It is normal to wait on this message for a few minutes (~5 minutes in my case) before we are able to get a connection to the VM. You may need to wait a few minutes until you get a message saying `default: Machine booted and ready!`.

File syncing will work properly after you receive this message: `default: Mounting shared folders`. Please wait for this message before proceeding to the next steps.

Once the VM booted up (and you were able to receive the messages specified above), you can ssh onto the VM by running the command:

    vagrant ssh

You will notice that the project is now synced to this VM by changing directory to **/vagrant** in the virtual machine.

    cd /vagrant

When you make any changes to the project locally, these changes are also reflected (synced) to the project files located in **/vagrant**, and vice versa.

## Install Project Dependencies

On the VM, update and upgrade:

    sudo apt-get update
    sudo apt-get upgrade

Install project dependencies:

    sudo apt-get install python3-dev
    sudo apt-get install python3-psycopg2
    sudo apt-get install libpq-dev
    sudo apt-get install python3-pip
    
Install Python's Virtual Environment (**Only for users not using Peacecorp's VM**)

    sudo pip3 install virtualenv
    
Create Python's Virtual Environment (**Only for users not using Peacecorp's VM**), by moving to the top level directory of the project containing **manage.py** and create your virtual environment, type :

    virtualenv venv
    
Activate Python's Virtual Environment (**Only for users not using Peacecorp's VM**)

    source venv/bin/activate
    
Now, your prompt will change to indicate that you are now operating within the virtual environment. It will look something like this (venv)user@host:~/myproject$.

**From here on the process is same whether using Peacecorp's VM or not**

Install all Python dependencies specified in the [requirements.txt](https://github.com/systers/app-web-server/blob/develop/requirements.txt) file using pip:
    
    sudo pip3 install -r requirements.txt
    
Or install one by one

    sudo pip3 install Django==1.11
    sudo pip3 install Jinja2==2.9.6
    sudo pip3 install MarkupSafe==1.0
    sudo pip3 install Pillow==4.1.1
    sudo pip3 install dj-database-url==0.4.2
    sudo pip3 install dj-static==0.0.6
    sudo pip3 install django-toolbelt==0.0.1
    sudo pip3 install djangorestframework==3.6.3
    sudo pip3 install gunicorn==19.7.1
    sudo pip3 install psycopg2==2.7.1
    sudo pip3 install static3==0.7.0
    sudo pip3 install django-rest-swagger==2.1.2
    sudo pip3 install PyYAML==3.12

**Configure autoenv**

    sudo pip3 install autoenv
    echo "source `which activate.sh`" >> ~/.bashrc
	
Changing Directory to the cloned directory will automatically resolve export settings error

    cd macc (cloned directory)
    
## Setup PostgreSQL

We will now setup PostgreSQL by first running the postgres client as root:

    sudo -u postgres psql

Next, we will create a user called `myuser` with a password `mypassword` (for now) with the permissions to be able to create roles, databases and to login with a password:

    create role myuser with createrole createdb login password 'mypassword';

Next, exit the postgres client by running the command:

    \q

We will need to change the **pg_hba.conf** file to indicate that users will authenticate by md5 as opposed to peer authentication. To do this, first open the **pg_hba.conf** file by running the command:
```
sudo nano /etc/postgresql/x.x/main/pg_hba.conf
```
(where x.x is the version number of postgres)

Change the line `local all postgres peer` to `local all postgres md5`

Also, change the line `local all all peer` to `local all all md5`

After making these changes, make sure to save the file.

Restart the postgresql client:

    sudo service postgresql restart

Now, we will be able to login to the postgres client with the `myuser` user that we created by running the following command:

    psql -U myuser -d postgres -h localhost -W

You will be prompted to enter a password, which is `mypassword`

Next, exit the postgres client again:

    \q

We will now create a database called `webapp`:

    createdb -U myuser webapp;

We can now login to the postgres client for the `webapp` database:

    psql -U myuser -d webapp -h localhost -W

You will be prompted to enter a password, which is `mypassword`

To view a list of tables for the `webapp` database, run this command under the postgres client:

    \dt

We can now manipulate the database by running the appropriate sql commands under this postgres client.

Make sure to exit the postgres client before proceeding to the next steps:

    \q

## Update settings.py

Update the database settings in **settings.py** in the **infohub** directory to look like this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'webapp',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
	    'HOST': 'localhost',
    }
}
```
Update the smtp settings in **settings.py** in the **infohub** directory to look like this:
```
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'pc.mobile.control.center@gmail.com'
SERVER_EMAIL = 'pc.mobile.control.center@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'pc.mobile.control.center.com'
EMAIL_HOST_PASSWORD = 'alphadeltaepsilon'
EMAIL_PORT = 465
```
The following lines need to be commented or kept as such if already commented:
```
#import dj_database_url
#DATABASES['default'] = dj_database_url.config()
```

## Generate Database Tables Corresponding to Django Models

Change directory to where you can find the **manage.py** file (this is located in the top level directory for the project). If you are installing the project on the VM, the project will be located within the **/vagrant** directory.

To view the sql commands that will be generated from `migrate`, run the command:

    python3 manage.py sqlmigrate app_name_here migration_name

For example, 
    
    python3 manage.py sqlmigrate malaria_web 0001_initial

To generate the database tables that correspond to the Django models, run the command:

    python3 manage.py makemigrations malaria_web malaria_api webhub signup profiles pcsa pcsa_GHN pcsa_safety_tools social_django
    python3 manage.py migrate

After running the `migrate` command, you should run the following command to create a superuser:

    python3 manage.py createsuperuser

Create a superuser with the following credentials (for now):
```
Username: admin
Email: your email
Password: mypassword
```

If the models are updated in any way, you need to delete the database and then migrating the fields once more. This can be done by:

    python3 manage.py flush
    python3 manage.py makemigrations
    python3 manage.py migrate

Check that the tables were created by starting the postgres client and viewing the tables using the `\dt` command.
```
psql -U myuser -d webapp -h localhost -W
```
```
\dt
```
Make sure to exit the postgres client before proceeding to the next steps:

    \q

## Run Development Server

Change directory to where you can find the **manage.py** file (this is located in the top level directory for the project).

Start the development server by running the command (this runs the development server on the VM):

    python3 manage.py runserver [::]:8000


## Try out Mobile App Control Center

You can now try out the project by going to [http://localhost:8000](http://localhost:8000) on a browser on your local machine.

Try logging in with your superuser credentials. After clicking on `Submit` you will get the following message:

    No Pcuser associated! Add a pcuser from admin

We need to create a pcuser that is associated with the superuser we created previously. To do this, go to the Django admin panel at [http://localhost:8000/admin](http://localhost:8000/admin) on your browser.

On the Django admin login page, login with your superuser credentials.

Once you have logged in, click on `Add` beside `Pcusers`.

In the form, enter in these fields:
```
User: admin
Location: Your location
Phone: Your phone number
Gender: Your gender
Reset pass: 1 (not sure what this field does)
Verified: 1 (not sure what this field does)
```
Click on `Save` and logout.

Go back to [http://localhost:8000](http://localhost:8000)

Login again with your superuser credentials, it should work since we have associated our superuser with a pcuser. You are now free to try out the application.

## Exit the Virtual Machine

Once you are done with testing out and running the project, you may want to exit the VM and suspend or shut it down by running these commands:

Exit out of the ssh session with the VM by running:

    exit

To put the VM in suspend mode, run the command:

    vagrant suspend

Alternatively, to shut down the VM, run the command:

    vagrant halt
