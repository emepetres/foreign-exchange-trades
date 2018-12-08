# foreign-exchange-trades
Dummy foreign exchange trades web application, based on Django 2.1

NOTES:
* Two decimal precision for trade amounts
* Four decimal precision for trade rate
* MAX trade amount: 99,999,999.99

TODO:
* MORE COMMENTS!
* TESTS!
* PRODUCTION/DOCKER

TO IMPROVE:
* Validate data again on the server against Fixer.io, before creating the trade.
* Ensure uniqueness in trade Id generation, by checking if the generated id exists in the system.


## Deploy

# Production environment
To Be Done

# Development environment
**Requirements** The deployment requires a machine with _python 3_, _pip_ and _virtualenv_, and virtualenv must be accesible by the command `virtualenv3` in the path.

0. Navigate to _fetrades_ folder
1. Copy _settings.ini.example_ to _settings.ini_ and edit the latter:
	* Set `SECRET_KEY` to an alphanumeric random string
	* Set `DEBUG=False` for production environments
	* Set the list of allowed hosts in `ALLOWED_HOSTS`, separated by comma.
	* Set `FIXER_API_KEY` to the appropiate _fixer.io_ api key. Get one for free at https://fixer.io/. 
2. Run `./setup-dev.sh`. The script will ask the information to create a new _admin_ user.
3. Run `./up-dev.sh` to run the application on http://localhost:8000.

