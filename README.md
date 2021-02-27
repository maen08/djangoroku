# Djangoroku

[![Made in Tanzania](https://img.shields.io/badge/made%20in-tanzania-008751.svg?style=flat-square)](https://github.com/Tanzania-Developers-Community/made-in-tanzania)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/ioi2908/djangoroku)


- [Djangoroku](https://github.com/maen08/djangoroku)  **By [@username](https://twitter.com/maentechie)**


Djangoroku is the package that helps to deploy Django application on Heroku. 

#### How

  - Configures the `settings.py` file for deployment
  - Installs all the necessary packages in your project
  - Deploys the application while coding
  - Configures the default database, `sqlite` on Heroku 

### Tech

Djangoroku involves these tech:

* [Django](https://docs.djangoproject.com/en/3.1/) - Python backend framework
* [Heroku](https://dashboard.heroku.com/apps) - PaaS for build and deploy apps
* [Python](https://www.python.org/) - Server side language

### Installation and Uses

To install and use `djangoroku` run these commands. Make sure you're at the root directory of your project.
```sh
$ pip install djangoroku
$ echo "from djangoroku import *" > deploy.py
$ python3 deploy.py
```

The script will start running and do everything for you. You'll only needed to provide:
 - Your project name
 - Choose the app name (which will be the Heroku domain name)
 - Needed to be logged in your Heroku account (emphasized)

Make sure your project runs with no errors on `localhost`, while developing. Note that, the package only helps you to deploy and not debug your coding errors.


### Todos

 - Display and interprete Heroku logs for debugging during deployment.
 - Setting up all types of databases.
 

License
----

MIT




