# Djangoroku


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/ioi2908/djangoroku)

Djangoroku is the package that helps you to deploy a django application on Heroku. No need to create files required or installing third-party packages. Djangoroku handles all!

#### How?

  - Configures the `settings.py` file for deployment
  - Installs all the necessary packages in your project
  - Deploys the application while coding
  - Configures the default database, `sqlite` in heroku 

### Tech

Djangoroku involves these tech:

* [Django](https://docs.djangoproject.com/en/3.1/) - Python backend framework
* [Heroku](https://dashboard.heroku.com/apps) - PaaS for build and deploy apps
* [Python](https://www.python.org/) - Server side language

### Installation and Uses

To install `djangoroku` run these commands. Make sure you're at the root directory of your project.
```sh
$ pip install djangoroku
$ cd djangoroku
$ python3 djangoroku.py
```

The script will start running and do it for you. You'll only needed to provide:
 - Your project name
 - Choose the app name (which will be the heroku domain name)
 - Needed to be logged in your heroku account (emphasized)

Make sure your project runs with no error in `localhost`, while developing. Note that, the package only helps you to deploy and not debug your coding errors.


### Todos

 - Display and interprete heroku logs for debugging during deployment.
 - Setting up all types of databases.
 

License
----

MIT




