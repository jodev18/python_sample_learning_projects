import RPi.GPIO as GPIO
import time
import requests
import json

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

GPIO.setwarnings(False)

authKey = 'Bearer PUT YOUR KEY HERE'

rq = requests.get("https://api.ciscospark.com/v1/rooms", headers={'Authorization':authKey})

roomToSearch = None
roomIdToMessage = None
x = True

while(x):
    roomToSearch = str(input("Search room:"))
    rooms = r.json()['items']
    
    for room in rooms:
        if(ro['title'].find(roomToSearch) != -1):
            x = False
            roomIdToMessage = room['id']
            print("Room found," + roomIdToMessage)
            break
    
    if(roomIdToMessage == None):
        print("Sorry wala")
    
#     jsonData = r.json()
#     messages = jsonData['items']
#     lastMessageId =None
    
    while True:
        time.sleep(1)
        print("Next iteration is starting ...")
        getMessagesUrlParameters = {"roomId":roomIdToMessage,"max":1}
        
        r = requests.get("https://api.ciscospark.com/v1/messages",params=getMessagesUrlParameters,headers={'Authorization':authKey})
        
        jsonData = r.json()
        messages = jsonData['items']
        message = messages[0]
        
        if(lastMessageId == message['id']):
            print("No new messages")
        else:
            print("New Message: " + message['text'])
            lastMessageId = message['id']
            
            if(message['text'] == 'Lumiere'):
                messageId = message['id']
                print("Found the secret magic word")
                
                GPIO.output(17,True)
