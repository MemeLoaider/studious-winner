# Welcome to my repo!
This is a special repo for memer affairs.

Folder **different-stuff** contains some many things that relate to my work in most universal manner. Feel free to peek inside!

Folder **party-service** contains a simple microservice project on python with flask framework. For running in docker-compose (or any other variant) a file with environment variables has to be created. For example, **.env**.
The list of environment variables:
* FLASK\_ENV - specifies current environment.
* SQLALCHEMY\_DATABASE\_URI - URI for connecting to the database with object relational mapping. Example of URI: "mysql+pymysql://root:1234@db:3306/mysql". Pay closer attention to the hostname of database, because when application is run via docker-compose the name of database is equal to the name of service that uses database image inside **docker-compose.yml** file.
* MYSQL\_ROOT\_PASSWORD - represents DB root password.
* MYSQL\_DATABASE - represents base database. For example, mysql.
* MYSQL\_USER - specifies database user.
* MYSQL\_PASSWORD - specifies db user's password.
Example for **.env** file in **party-service**:
```
#party-service .env file#
FLASK_ENV=local
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:1234@db:3306/mysql

MYSQL_ROOT_PASSWORD=1234
MYSQL_DATABASE=mysql
MYSQL_USER=someuser
MYSQL_PASSWORD=someuser
```

Folder **party-service-testing** contains a simple testing project for testing **party-service** api.
For testing in environment special file called **.env** has to be created (you can call it whatever you want but it should contain environment variables).
The list of enviroment variables for testing:
* ENV - specifies current environment where tests are run.
* PARTY\_SERVICE\_URL - tells you basic url for party-service (hostname)
* GET\_ALL\_PARTIES\_ENDPOINT - an endpoint for getting all parties.
* GET\_SINGLE\_PARTY\_ENDPOINT - an endpoint for getting single party.
* CREATE\_PARTY\_ENDPOINT - an endpoint for creating a party.
* UPDATE\_HOST\_ENDPOINT - an endpoint for updating pary host.
* DELETE\_PARTY\_ENDPOINT - an endpoint for deleting party.
* DB\_URL - a url for connecting to database with parties. It has to be configured for using with sqlalchemy, so the example can be like: "mysql+pymysql://username:usrpassword@localhost:3306/party"

Example for **.env** file in **party-service-testing**
```
###Local Config for testing###
ENV=LOCAL
PARTY_SERVICE_URL=http://localhost:5050
GET_ALL_PARTIES_ENDPOINT=/party
GET_SINGLE_PARTY_ENDPOINT=/party/ #Append party_id after this slash.
CREATE_PARTY_ENDPOINT=/party
UPDATE_HOST_ENDPOINT=/party/update-host
DELETE_PARTY_ENDPOINT=/party/ #Append party_id after this slash.

###Database connection###
DB_URL=mysql+pymysql://root:1234@localhost:3306/party

```


