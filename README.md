# foreign-exchange-trades
Foreign exchange trades dummy web application, based on Django 2.1

## Deploy
**Requirements** The deployment requires a machine with _python 3_, _pip_ and _virtualenv_, and virtualenv must be accesible by the command `virtualenv3` in the path.

WARNING: Production deployment not automated yet.

1. Copy _settings.ini.example_ to _settings.ini_ and edit the latter:
	* Set `SECRET_KEY` to an alphanumeric random string
	* Set `DEBUG=False` for production environments
	* Set the list of allowed hosts in `ALLOWED_HOSTS`, separated by comma.
2. Run `./setup-dev.sh`. The script will ask the information to create a new _admin_ user.
3. Run `./up-dev.sh` to run the application on http://localhost:8000.


NOTES:
* MAX trade amount: 99,999,999.99
* DECIMAL format to have precision

## Development

NOTES:
* -

TODO:
* COMMENTS!
* TESTS!
