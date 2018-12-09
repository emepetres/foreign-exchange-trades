# foreign-exchange-trades
Dummy foreign exchange trades web application, based on Django 2.1

NOTES:
* Two decimal precision for trade amounts
* Four decimal precision for trade rate
* MAX trade amount: 99,999,999.99

TODO:
* PRODUCTION/DOCKER


## Deploy

### Standalone
The standalone deployment uses a local database from SQLite and a lightweight server, and it is not meant for production.

**Requirements** _python 3.7_ and _pipenv_.

**WARNING:** _DO NOT USE THIS SERVER IN A PRODUCTION SETTING_

0. Navigate to _fetrades_ folder
1. Copy _settings.ini.example_ to _settings.ini_ and edit the latter:
	* Set `WEBNAME` to the title of the website
	* Set `SECRET_KEY` to an alphanumeric random string
	* Set `DEBUG=False` for production-like environments
	* Set the list of allowed hosts in `ALLOWED_HOSTS`, separated by comma.
	* Set `FIXER_API_KEY` to the appropiate _fixer.io_ api key. Get one for free at https://fixer.io/. 
2. Run `./setup.sh`. The script will ask the information to create a new _admin_ user.
3. Run `./up.sh` to run the application on http://localhost:8000.

### Production environment
A production environment with Postgres, Gunicorn and Nginx.

**Requirements** _Docker_ and _Docker Compose_.

0. Navigate to _docker_ folder
1. Copy _example.env_ to _.env_ and edit the latter:
	* Set `WEBNAME` to the title of the website
	* Set `SECRET_KEY` to an alphanumeric random string
	* Set `DEBUG=False` for production-like environments
	* Set the list of allowed hosts in `ALLOWED_HOSTS`, separated by comma.
	* Set `FIXER_API_KEY` to the appropiate _fixer.io_ api key. Get one for free at https://fixer.io/.
	* Change `PORT` to serve the website in a port different from 1337.
	* Change `SQL_DATABASE` to use a different database name.
	* Change `SQL_USER` to use a different user name to access the database.
	* Change `SQL_PASSWORD` to use a different password to access the database.
2. Run `sudo docker-compose build` to build the container
3. Run `sudo docker-compose up -d` to run the application on http://localhost:8000.


## Test
In a standalone deployment, use `./test.sh` to run all the tests available. Internally it uses _django.test_ module, a wrapper of _unittest_ module.


## Development
The source code follows the pep8 style guide, using flake8 and pylint as linters.

To make modifications, the standalone deployment is the right one. Use `/setup-dev.sh` instead of `./setup.sh` to install autopep8, flake8 and pylint.

_Suggestions to improve:_
* Validate data again on the server against Fixer.io, before creating the trade.
* Ensure uniqueness in trade Id generation, by checking if the generated id exists in the system.

