#!/usr/bin/python3
import os
import sys
import subprocess
import logging, coloredlogs
import time



class DjangoHerokuDeploy():

# pypi needs this instead of print statement

    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG', logger=logger)


# I:THE DJANGO PART-SETTING UP EVERYTHING

# ask the user to enter the project-name
    project_name = input('Whats your project name:')

   
    try:
        os.system('pip install gunicorn psycopg2-binary django-heroku dj-database-url')
        logger.debug('DONE: All packages are installed successfully')

    except FileExistsError:
        logger.debug('DONE: All packages are installed successfully')


    time.sleep(4)

# create a requirements.txt file
    try:
        os.system('pip freeze > requirements.txt')
        logger.debug('DONE: requirements.txt file created')

    except FileExistsError:
        logger.debug('DONE: requirements.txt file created')


    time.sleep(4)

# create a Procfile
    try:
        with open('Procfile', 'x') as f:
            # make sure the project name is correct
            f.write('web: gunicorn ' + project_name + '.wsgi:application')
        logger.debug('DONE: Procfile created')


    except FileExistsError:
        logger.debug('DONE: Procfile created')


# project_directory = os.getcwd()
# split_dirs = project_directory.split('/')
# project_folder = split_dirs[-1] 

    time.sleep(3)

# a function to prepend the import statement
    to_settings = os.chdir(project_name)

    def line_prepender(filename, line):
        with open(filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)

    try:
        line_prepender('settings.py', 'import dj_database_url')
        line_prepender('settings.py', 'import django_heroku')

    except FileExistsError:
        logger.debug('DONE: All packages are imported')





    time.sleep(3)

    logger.debug('Remember to push everything on Github')


# II: HEROKU PART-DEPLOYMENT

    try:
        logger.debug("INFO: Please login to heroku...")
        # os.system('heroku login')
    
    except:
        logger.debug('INFO: Please login to heroku')


    time.sleep(2)

# creating a heroku domain-name
    domain_name = input('Choose the app name: ')
    os.system('heroku create' +' '+ domain_name)

    reading_file = open('settings.py', 'r')
    new_file_content = ""

    ALLOWED_HOSTS = domain_name + '.herokuapp.com'
    link = ALLOWED_HOSTS.split(' ')

    for line in reading_file:
      stripped_line = line.strip()
      new_line = stripped_line.replace(
          'ALLOWED_HOSTS = []', f'ALLOWED_HOSTS = {link}')  # user should not rewrite ALLOWED_HOSTS
                                                            # before the script. Let it handle everything
      new_file_content += new_line + "\n"


    reading_file.close()
    writing_file = open('settings.py', 'w')
    writing_file.write(new_file_content)

    writing_file.close()


# push to heroku

    logger.debug('INFO: Deploying...')
    time.sleep(4)

    os.system('heroku config:set DISABLE_COLLECTSTATIC=1')
    os.system('heroku git:remote -a' + ' ' + domain_name)
    os.system('heroku config:set DISABLE_COLLECTSTATIC=1')
    os.system('git push heroku master')

    logger.debug('Setting up database...')
    time.sleep(3)

    os.system('heroku run python manage.py makemigrations')
    os.system('heroku run python manage.py migrate')

    time.sleep(2)
    logger.debug('DONE: SUCCESSFUL DEPLOYED!')
