# Server that holds pokémon data.

## Requirements:
* Python 3
* Flask 1.1.1
* Flask-RESTful 0.3.8
* Flask-SQLAlchemy 2.4.1
* SQLAlchemy 1.3.13
* xmltodict 0.12.0
* dicttoxml 1.7.4

## Server setup using Docker
### Step 1. Build Server image

Run the below command to Generate application docker image:

`make build`

### Step 2. Run Docker container

Spin up application container based on this docker image:

`make run`

note: To clean an existing setup use: `make clean` comand.
## Accessing the application
Go to the below URL to access the application.
http://0.0.0.0:5000/<api-endpoint>

Note: in case the application is not available you can check the IP of your application with the below command.

`make inspect`

## Server setup without using Docker
### Step 1. Install Python 3
### Step 2. Install the required python packages with the below command.

`pip install --no-cache-dir -r requirements.txt`
### Step 3. Setup the DB with the below command.

`flask create-db`
### Step 3. Start the application server with the following command within the pokemon directory

`python3 app.py`
