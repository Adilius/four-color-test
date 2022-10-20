# Fourpersonalityquiz

Personality quiz written in Flask
https://fourpersonalityquiz.herokuapp.com/

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```
## Run

`python app.py`

## Database

View database:
`python .\database_viewer.py`

Fill database:
`python .\database_filler.py 100`

## Download database file from Heroku
Login to heroku:
`heroku login`

Download database file:
`heroku ps:copy app/app.db --app fourpersonalityquiz`

## Update SSL Certificate

`certbot certonly --manual --preferred-challenges dns`

`fourpersonalityquiz.com`

1. Change TXT record in namecheap to `_acme-challenge.fourpersonalityquiz.com`
2. Update value of that record to given value

## Screenshots

![image](https://user-images.githubusercontent.com/43440295/128189167-46b129c0-f499-4efa-b774-159ba942b1d5.png)
![image](https://user-images.githubusercontent.com/43440295/128189219-358377d4-a222-47fb-a29e-58ab43fdba3a.png)
![image](https://user-images.githubusercontent.com/43440295/128189337-23bcae0f-d735-49d8-a7a4-7073199578bb.png)

