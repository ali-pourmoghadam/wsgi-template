From python:3.11.4

WORKDIR  app

COPY . .


Run pip install Flask
Run pip install uwsgi


cmd ["uwsgi"  , "--ini" , "app.ini"]
