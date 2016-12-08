# morning_night
The Final Project for EE810-internet of things

## Description
This project aims to be a full service automated soft alarm clock. 
The time when you need to wake up is automatically pulled from your google calendar so you wake up in time for your first event.
The website also records statistics on how long it took you to wake up and how you felt. 

## Setup
1. Change the super user in Morning/views.py and in Night/viewspy in the detail function. Change author to your account name and password.
2. Get an Oauth2 token for your google calendar, download the json file and replace the secret.json file with yours. 

## Dependancies
there is a way to use omxplayer wrapper to play the music (local file or url)
https://github.com/willprice/python-omxplayer-wrapper

install:
sudo pip install omxplayer-wrapper

the first time running will fail,so you can do player.play twice in your code .not work very well

install:
sudo pip install -U django

sudo pip install -U djangorestframework

sudo pip install -U markdown

sudo pip install -U requests

## Future Work
1. Creating Master server for everyone to connect to so each user doesn't have to set up their own.
2. Suggestions on how to wake up better based on the statistics we gather.
3. Give users options about music they want to play.
4. Make interface more elegant and user-friendly.


## Authors
Songian 
and Matthew
