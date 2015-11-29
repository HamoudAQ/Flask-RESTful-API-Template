[![Build Status](https://travis-ci.org/HamoudAQ/Flask-RESTful-API-Template.svg?branch=master)](https://travis-ci.org/HamoudAQ/Flask-RESTful-API-Template)

# Introduction Flask-RESTful-API-Template-

I have created this project to be tamplate for creating RESTful api project based on Flask and its extensions.
It is expected to make the the beginning of development easier by defining the structure for in addition to implement most used functionality (such as authentication).

#Usage

-Install Requirements:At the beginning you need to install dependencies ( you need 'pip' ):
pip install -r requirements.txt

-Define Your Model :The Model file (Model.py) is mapping for your Database tables so define it there.
for more information check : http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/

-Create Resource:Most of your work will be with resources , so define a resource in /resources directory 
and once you have defined a resource add route to it in app.py

-Data Validation:in case you want to validate data , you can define your validation in /Common/Validation.py

-Run Your Application:simply by 'python Run_Server.py'
