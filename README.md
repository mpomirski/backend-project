# REST API example application
 <a href="#">
    <img src="https://raw.githubusercontent.com/MikeCodesDotNET/ColoredBadges/master/svg/dev/languages/python.svg" alt="python badge" style="vertical-align:top margin:6px 4px">
  </a>
   <a href="https://starfish-app-urx9y.ondigitalocean.app/docs  ">
    <img src="https://raw.githubusercontent.com/MikeCodesDotNET/ColoredBadges/master/svg/dev/services/digitalocean.svg" alt="digitalocean badge" style="vertical-align:top margin:6px 4px">
  </a>  

This is a simple REST API providing access to currency data

# Check it out at

https://starfish-app-urx9y.ondigitalocean.app/docs  

https://starfish-app-urx9y.ondigitalocean.app/exchanges/GBP/2023-01-02

https://starfish-app-urx9y.ondigitalocean.app/exchanges/minmax/gbp/100

https://starfish-app-urx9y.ondigitalocean.app/exchanges/differences/gbp/100

## Docker

    docker build -t web-api .
    docker run --publish 80:80 web-api

## Install

    pip install -r requirements.txt

## Run the app

    python -m uvicorn src.main:app

## Run the tests

    python -m pytest ./tests/

# REST API

The REST API to the example app is described below.

After deployment, documentation avaliable also at http://127.0.0.1:8000/docs

## Given a date (formatted YYYY-MM-DD) and a currency code, provides its average exchange rate

### Request

`GET /exchanges/{currency}/{date}/`

    curl http://127.0.0.1:8000/exchanges/GBP/2023-01-02

### Response

    HTTP/1.1 200 OK
    date: Fri, 21 Apr 2023 23:19:40 GMT
    server: uvicorn
    content-length: 6
    content-type: application/json

    5.2768

## Given a currency code and the number of last quotations N (N <= 255), provides the max and min average value 

### Request

`GET /exchanges/minmax/{currency}/{N}`

    curl http://127.0.0.1:8000/exchanges/minmax/gbp/100

### Response

    HTTP/1.1 200 OK
    date: Fri, 21 Apr 2023 23:22:46 GMT
    server: uvicorn
    content-length: 27
    content-type: application/json

    {"min":5.2086,"max":5.4638}

## Given a currency code and the number of last quotations N (N <= 255), provides the major difference between the buy and ask rate

### Request

`GET /exchanges/differences/{currency}/{N}`

    curl http://127.0.0.1:8000/exchanges/differences/gbp/100

### Response

    HTTP/1.1 200 OK
    date: Fri, 21 Apr 2023 23:24:38 GMT
    server: uvicorn
    content-length: 27
    content-type: application/json

    {"max": 0.1096}
