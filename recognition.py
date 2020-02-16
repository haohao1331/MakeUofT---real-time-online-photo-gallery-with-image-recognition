import io
import os
import wikipedia
import sys
import paramiko
from scp import SCPClient

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from gpiozero import LED, Button
import time
from random import randrange
print(randrange(10))

led = LED(17)
button = Button(23)

previousState = 2


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="/home/pi/Desktop/pic/key.json"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.43.37', username='haohao1331', password='j89k382k0')
scp = SCPClient(ssh.get_transport())
        



def detect_landmarks(path):
    """Detects landmarks in the file."""

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    
    try:
        print(landmarks[0].description)
    except:
        print("not a landmark")
        return False
    
    
    landmarkName = landmarks[0].description
    print (wikipedia.summary(landmarkName, sentences=2))
    return True
    
    
def recognize_objects(path):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)
        
