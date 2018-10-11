[![Build Status](https://travis-ci.org/msfernandes/review-api.svg?branch=master)](https://travis-ci.org/msfernandes/review-api)
[![Coverage Status](https://coveralls.io/repos/github/msfernandes/review-api/badge.svg?branch=master)](https://coveralls.io/github/msfernandes/review-api?branch=master)


# review-api

This project is part of a code challenge from BairesDev/ConsummerAffairs.
It's a REST API written in Python and Django and is available at https://review-api-bairesdev.herokuapp.com/ .

## Development

### Setup development environment

> I usually use Pipenv to handle my projects python dependencies, but in this project I had
some troubles with Travis-CI and I don't had much time to investigate and solve the problem.
So I decided to use only a `requirements.txt`.

To install configure, add some data and run the project:

```
pip install -r requirements.txt
./src/manage.py migrate
./src/manage.py loaddata src/core/fixtures/data.json
./src/manage.py runserver
```
After execute this commands you can access the development server at http://localhost:8000.
The test data contains three users, including an `admin` which password is `1234` and two common users (`john` and `hayden`) which both password is `321ewqdsa`.

### Testing

```
coverage run src/manage.py test src/
coverage report
flake8 src/
```

These commands run all application tests using coverage that gives a report containing the test coverage of all files. Also run a flake8 validation.

### Continous Delivery

To automate the deploy to heroku I configured a `.travis.yml` to run all the tests after each commit and if the build is succesfull this commit is deployed to Heroku.

## The API

The API is composed by two endpoints: `/api/v1/auth/token/` and `/api/v1/reviews/`.

### /auth/token/

#### POST

This endpoint is responsible to give the api token (to access the second endpoint). You must to do a POST request with a valid `username` and `password` data.

Request example:
```
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"john","password":"321ewqdsa"}'  \
    http://localhost:8000/api/v1/auth/token/
```

And the endpoint will return the access token (if the credentials are valid):

```
{"token":"200f89b69a305243491277e23051a11659477dff"}
```

### /reviews/

Once you have an access token, you can make a request to the `/api/v1/reviews/` endpoint. You can perform two operations:

#### GET

Will return a list of Reviews made by the user that the access token belong.

Request example:
```
curl --header "Content-Type: application/json" \
    --header "Authorization: Token access_token" \
    --request GET http://localhost:8000/api/v1/reviews/
```

Response:
```
[
    {
        "id":2,
        "rating":3,
        "title":"Deserunt mollit anim id est laborum",
        "summary":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "ip":"127.0.0.1",
        "company":{
            "id":1,"name":"Company Test"
        },
        "reviewer":{
            "id":2,
            "username":"john",
            "first_name":"John",
            "last_name":"Doe",
            "email":"john@email.com"
        },
        "submission_date":"2018-10-06T00:43:06.756000Z"
    },
    {
        "id":3,
        "rating":1,
        "title":"consectetur adipisicing elit",
        "summary":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "ip":"198.142.8.76",
        "company":{
            "id":1,"name":"Company Test"
        },
        "reviewer":{
            "id":2,
            "username":"john",
            "first_name":"John",
            "last_name":"Doe",
            "email":"john@email.com"
        },
        "submission_date":"2018-10-06T00:43:24.854000Z"
    }
]
```

#### POST

Create a review. Your request data must follow this pattern:

```
{
    "rating": 1,
    "title": "Title",
    "summary": "Summary",
    "company": {
        "name": "Company"
    }
}
```

Note that it's missing some informations that will be filled automatically:
* `ip` will be catch through request headers
* `reviewer` is the user that the access token belongs
* `submission_date` will be filled when the object is saved on the database

Request example:
```
curl --header "Content-Type: application/json" \
    --header "Authorization: Token access_token" \
    --request POST \
    --data '{"rating": 3, "title": "Review Title", "summary": "Review summary", "company": {"name": "Company Name"}}'  \
    http://localhost:8000/api/v1/reviews/
```

If the review creation is successfull, the API will return a JSON with the created review:
```
{
    "id":6,
    "rating":3,
    "title":"Review Title",
    "summary":"Review summary",
    "ip":"127.0.0.1",
    "company":{
        "id":4,
        "name":"Company Name"
    },
    "reviewer":{
        "id":2,"
        username":"john",
        "first_name":"John",
        "last_name":"Doe",
        "email":"john@email.com"
    },
    "submission_date":"2018-10-06T03:26:16.102514Z"
}
```

## Admin panel

The administration panel is available through `/admin/` and you can manage all access tokens, users, companies and reviews. If you executed all steps from **Setup development environment** you already have an user account with admin privileges:

* username: *admin*
* password: *1234*

With these credentials you can enter into admin panel.
