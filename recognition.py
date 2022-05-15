import json
import ntpath
import os
import cv
from deepface import DeepFace
from deepface.detectors import FaceDetector

import db as DB

######################################################################


face_req_model = DeepFace.build_model('Facenet512')
######################################################################
directory = 'img/detected/'
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']

models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]


detected_list = []
for detected_filename in os.listdir(directory):
    #print(detected_filename)
    if detected_filename.endswith(".jpg"):
        detected_list.append(directory + detected_filename)
       # print(detected_filename)

    else:
        print("Wrong file type")

df = DeepFace.find(img_path = detected_list, db_path = "img/msc_images", model_name = models[1],model=face_req_model,enforce_detection=False,detector_backend = backends[3])
print(df)
x=0
y=0
ses= 11
sem = 1
for x in range(len(df)):
    
    for y in df[x]['identity']:
        file = ntpath.basename(y)
        filename,ext = os.path.splitext(file)
        DB.insert(filename,ses,sem)
        #print(filename)

