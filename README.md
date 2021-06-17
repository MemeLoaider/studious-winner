# Welcome to my repo!
This is a special repo for memer affairs.

Folder **different-stuff** contains some many things that relate to my work in most universal manner. Feel free to peek inside!

Folder **party-service** contains a simple microservice project on python with flask framework. Work in progress...

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


