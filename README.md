# AlphaChallenge

If you are reading this, thank you for your interest in this project.

This a python/django based project consists in building a tool that can extract
stock market values from a public source, and register it in a database. The
data source used was the website [ValorInveste](https://valorinveste.globo.com/cotacoes/).

The project also gives the possibility to create price alerts, which will check 
for the option price change, and will send a message when gets to the defined value. 

For developpers, I used python with django for developping the whole backend, 
redis and celery with celery beat for periodic tasks and scheduling jobs, and
for database postgres.

Despite the challenge don't define a frontend technology, I decided to create some
user interface. For that, I used Django Templates.


## How It Works

The main part of the whole project is the scrapper.py file.

There I created a ScrapperClient which is cappable of request a website, access
his content, extract the important data, and saves it to the database.

After we have run the scrapper and extracted all the data, we can create a price
alert, which is linked to a option code and have a target price. Once the option
gets to the value, the user is informed and the alert is considered done.


## Periodic Tasks

We have two periodic tasks that run every 5 minutes, one runs the scrapper 
collecting data and other checks for all the prices alerts.

The both of them are described in settings.py by the CELERY_BEAT_SCHEDULE
variable. If you want to change the execution interval, you change there.

The only part important here, is that the both tasks have the same inverval, so
that way, every time we update our prices we also check for price alerts.


## How to run the project

All things here are inside docker containers, so you will not have much work.

### Check for docker installation

Before running anything you need to have installed docker and docker compose api.

To test that you can run in your terminal `docker version` and `docker compose version`.

If everything is working fine, you should see some output like that:
```sh
    >>> docker version 
        Client: Docker Engine - Community
        Version:           23.0.1
        API version:       1.42
        Go version:        go1.19.5
        Git commit:        a5ee5b1
        Built:             Thu Feb  9 19:46:56 2023
        OS/Arch:           linux/amd64
        Context:           default
```

```sh
    >>> docker compose version
        Docker Compose version v2.16.0
```

### Building and running your containers

In the root directory we have a docker-compose.yml file that have all the
services and configuration for them.

To build your containers you can run:
```sh
    docker compose build`
```

Once the build is complete, to start the project just run:
```sh
    docker compose up -d
```

With the containers running you can access the project in [localhost:8000](http://localhost:8000/)

P.s.: The `-d` flag is optional and make the containers run on daemon mode, wich
basically leaves you with your terminal free.


### Seeing the logs

So at that point we are already runing our project, but if you running it on
daemon mode (used the -d flag) you are not seeing any log from the containers.

To solve that, you can manually run in your terminal:
```sh
    docker compose logs celery
```

You can change `celery` to other service name, but in that example, once the
celery is the responsible for running our periodic tasks, you will be able to
see all the log from commands.

Remember that the periodic tasks are running every 5 minutes, so if you just
started the application you probably won't see many logs. If so, just wait for
the task interval and check the logs again.


### Whats happening on up??

Everytime you run your containers the `entrypoint.sh` file will be executed.

When the entrypoint is runned, he will look for migrations, migrate the tables,
runs the scrapper and verify the price alerts. It also creates a django 
superuser, but only in the first time you run the project.


## User flow

Once you are running the project, you probably will want to test it.

The default [localhost](http://localhost:8000/) url will show a landing page, 
with a very friendly user experience.

There you can navigate into pages, create a new account, see all the prices, and
create a price alert. I really encourage you to create a new user, it`s simple,
but because we created a superuser on the previous step, you can just make login
using the credentials:

```py
Username="admin"
password="admin"
```


## Django Admin.

Another common and very usefull thing Django gives us is the admin panel.

To get to the panel just access [localhost/admin](http://localhost:8000/admin),
and login with the same credentials of our superuser.
```py
Username="admin"
password="admin"
```

Remember here that users created through the user creation form don't have any
superuser privilegies, so you will not be able to login in admin with that user.


## Final Disclaimer

This project consist's in showing knowledge about technologies, and in principal,
python and django. It's also part of an application proccess.

Everything here was made in a short period of time and may have some
inconsistency and unnecessary features. I know many things can be optimized but
it would take a lot of time.

If you want to contact me, you can reach my
[linkedin profile](https://www.linkedin.com/in/vitorstoledo/).
