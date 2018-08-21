# Maintenance Tracker API
[![Build Status](https://travis-ci.org/leni1/main-tracker-api.svg?branch=develop)](https://travis-ci.org/leni1/main-tracker-api/)
[![Maintainability](https://api.codeclimate.com/v1/badges/7b26ed0f64d520f1360f/maintainability)](https://codeclimate.com/github/leni1/main-tracker-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/leni1/main-tracker-api/badge.svg?branch=develop)](https://coveralls.io/github/leni1/main-tracker-api?branch=develop)

An API that allows users to make maintenance/repair requests to operations or repairs department and monitor the status of their request.

## Features
The API should have the following API endpoints working:

Endpoint | Functionality
-------- | -------------
GET /api/v1/users/requests | Get all requests
GET /api/v1/users/requests/`<requestId>` | Get a request
POST /api/v1/users/requests | Create a request
PUT /api/v1/users/requests/`<requestId>` | Modify a request

## Note
This API will use data structures to store data.

### Instructions

1. Clone the repository as follows:

    `git clone https://github.com/leni1/main-tracker-api.git`

2. Checkout the `develop` branch:

    `git checkout develop`

3. Create a virtual environment in the source code folder through **either** of the following commands:

    `python -m venv name-of-virtual-environment`

    or

    `virtualenv name-of-virtual-environment`

4. Activate the virtual environment and install the dependencies in `requirements.txt`

    `source name-of-virtual-environment/bin/activate`

    `pip install -r requirements.txt`

5. Export the application as an environment variable and set the `flask` environment to production

    `export FLASK_APP=api`

    `export FLASK_ENV=production`

6. Run the application using `flask run` and test the endpoints with sample data using Postman or `curl`.

### Tests
To run tests, follow steps 1 to 4 (if you haven't already done so) and then enter `pytest tests/` at the command prompt.

### Author

Leni Kadali Mutungi
