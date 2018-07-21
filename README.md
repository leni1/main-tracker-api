# Maintenance Tracker API
[![Build Status](https://travis-ci.org/leni1/main-tracker-api.svg?branch=develop)](https://travis-ci.org/leni1/main-tracker-api/)
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
