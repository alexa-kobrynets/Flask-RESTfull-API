# Flask-RESTfull-API

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Web application for analysis racing reports. 
Technologies: SQLite, YAML specification by swagger, unit testing by pytest.
Functionality of API:
- get report in different order in json or xml, 
- get information about one driver in json or xml,
- collect log files, load data to database.
	
## Technologies
Project is created with:
* Flask==2.2.2
* Flask-Bootstrap==3.3.7.1
* Jinja2==3.1.2
* SQLite
* click==8.1.3
* flasgger~=0.9.5
* peewee~=3.15.3
* pytest~=7.1.3
	
## Setup
To run this project, install it locally using npm:

```
$ git pull https://github.com/alexa-kobrynets/Flask-RESTfull-API
$ pip install -r requirements
# for load data to database
$ python3 /app/db_generate.py run 
# run app
$ flask -- app fl run
```