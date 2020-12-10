# from distutils.core import setup
from os import path
from setuptools import setup


doc_dir = path.abspath(path.dirname(__file__))
with open(path.join(doc_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='djangoroku',        
    packages=['djangoroku'],   # Chose the same as "name"
    version='0.1.0',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',

    
    description='A package that helps to deploy django application to heroku',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Stanley Ruheza',                 
    author_email='2001stany@gmail.com',
       
    # link to your github 
    url='https://github.com/ioi2908/djangoroku',
   
    download_url='https://github.com/ioi2908/djangoroku/archive/v_01.tar.gz',
    
    keywords=['django', 'heroku', 'deploy django', 'django heroku'],
    
    install_requires=[            
        'coloredlogs',
        'wheel',
        'setuptools',
        
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ],
)
