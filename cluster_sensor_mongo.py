import RPi.GPIO as GPIO
import time
import requests
import json

mongoLabsDatabase = "!!!-REPLACE-WITH-YOUR-MLAB.COM-DB-NAME-!!!!"
mongoLabsCollection = "!!!-REPLACE-WITH-YOUR-MLAB.COM-COLLECTION-NAME-!!!!"
mongoLabsApiKey = "!!!-REPLACE-WITH-YOUR-MLAB.COM-DB-API-KEY!!!!"

# The RESP API URL Endpoint for the specified collection in your database:
mongoLabsApiURI = "https://api.mlab.com/api/1/databases/" + mongoLabsDatabase + "/collections/" + mongoLabsCollection + "/?apiKey=" + mongoLabsApiKey

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)

GPIO.setwarnings(False)

state = GPIO.input(23)

while True:
    # a value to store in the database - can be either True or False
    alarmValue = state == 1

    # requests.put - PUT a new "alarm" record in the DB
    r = requests.put( mongoLabsApiURI,
                      json = {"alarm": alarmValue}   # JSON encoded data
    )

    # verify if the response indicates a successfull requests (http code 200)
    if (r.status_code != 200):                  # if response from request is not 
        print("Something wrong has happened:") #200/OK, then alert!
        print("ERROR CODE: " + str(r.status_code))
        print("ERROR RESPONSE: " + r.text)
    else:
        print("All OK, record stored.")
