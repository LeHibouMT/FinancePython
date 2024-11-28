# installation
install Python, version 3.12.6<br />
install PostgreSQL 16.4 with PgBouncer, PgAdmin and PgAgent<br />
navigate to the project folder<br />
create VM: python -m venv env<br />
activate VM: .\env\Scripts\activate<br />
deactive VM: deactivate<br />
install requirements: pip install -r requirements.txt<br />

# run and test
run the application: uvicorn app.main:app --reload<br />
test a route with the swagger from fastAPI: http://127.0.0.1:8000/docs<br />
example on how to use a curl to test a route:<br />
    - for CMD:  curl -X GET "http://127.0.0.1:8000/items/0"<br />
    - for powershell: curl.exe -X GET "http://127.0.0.1:8000/items/0"<br />

# database
use PgAdmin to manage the database<br />
create a new database: CREATE DATABASE mydatabase;<br />
create a new user: CREATE USER myuser WITH PASSWORD 'mypassword';<br />
grant privileges: GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;<br />

