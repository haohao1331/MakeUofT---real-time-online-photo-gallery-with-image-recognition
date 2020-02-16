import cv2
import io
import wikipedia
import sys
import numpy as np
import argparse
import os, time
from gtts import gTTS
from pygame import mixer
from addPost import *
import keyboard

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="key.json"
filepath = "./src/components/Posts.tsx"
alreadyadded = []
Gadded = []
Gremoved = []
parser = argparse.ArgumentParser()
parser.add_argument('inputs', type = str, help='image directory')
parser.add_argument('output', type = str, help='output directory')
toweb = "src/Image"
args = parser.parse_args()

def yolo(args):
    for remove in Gremoved:
        os.remove(args.output+'/'+remove)
        if remove != "pic1.jpg":
            os.remove(toweb + '/' + remove)
    if Gadded == []:
        return 0
    time.sleep(0.5)
    updatedetection()

    # Load Yolo
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))


    for images in Gadded:

        # Loading image
        img = cv2.imread(args.inputs+'/'+images)
        img = cv2.resize(img, None, fx=0.4, fy=0.4)
        height, width, channels = img.shape

        # Saving image in web directory

        cv2.imwrite(toweb + '/' + images, img)
        updatePosts(filepath, images, alreadyadded)


        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        output = []
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                output.append(label)
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

        cv2.imwrite(args.output+'/'+images, img)

        # read out speech

        if detect_landmarks(toweb + "/" + images):
            return True

        audio = "There "
        if (len(output) == 0):
            audio += "is nothing"
        elif (len(output) == 1):
            audio = audio + "is " + output[0]
        else:
            objects = {i:output.count(i) for i in output}
            audio += "are "
            for i in range(len(list(objects))):
                audio += str(list(objects.values())[i])
                if (list(objects.values())[i] == 1):
                    audio = audio + ' ' + list(objects)[i] + ','
                else:
                    audio = audio + ' ' + list(objects)[i] + "s,"

        mp3 = gTTS(text=audio, lang='en', slow=False) 
        mp3.save("result.mp3")

        mixer.init()
        mixer.music.load("result.mp3")
        mixer.music.play()

    return 0
        # with open(args.output+"/result.txt", 'a') as save:
        #     for item in output:    
        #         save.write('%s ' % item)
        #     save.write('\n')

def detectreset():
    global alreadyadded
    if keyboard.is_pressed('r'):
        restart(filepath)
        print("Image directory is reset")
        alreadyadded = []
    return True

def updatedetection():
    global Gadded
    global Gremoved
    inputs = dict([(f, None) for f in os.listdir(args.inputs)])
    outputs = dict([(f, None) for f in os.listdir(args.output)])
    Gadded = [f for f in inputs if not f in outputs]
    Gremoved = [f for f in outputs if not f in inputs]


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
    wikistring = wikipedia.summary(landmarkName, sentences=2)
    mp3 = gTTS(text=wikistring, lang='en', slow=False)
    mp3.save("result.mp3")

    mixer.init()
    mixer.music.load("result.mp3")
    mixer.music.play()
    return True

while 1:
    time.sleep (1)
    updatedetection()
    yolo(args)
    detectreset()


