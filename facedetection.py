
import numpy as np
from deepface import DeepFace
from deepface.detectors import FaceDetector
import matplotlib.pyplot as plt
from matplotlib.pyplot import show
from mtcnn import MTCNN
from PIL import Image
import mtcnn
import cv2
detectors= ['opencv','dlib','ssd','mtcnn','retinaface']
#pix = 'img/test/msc2.jpeg'
pix = 'img/test/not_ub/c6.jpg'
newimg = plt.imread(pix)
detector = mtcnn.MTCNN()

def extract_face_from_image(faces,image , required_size=(130, 130)):
    face_images = []

    for face in faces:
        # extract the bounding box from the requested face
        x1, y1, width, height = face['box']
        x2, y2 = x1 + width, y1 + height
        # extract the face
        face_boundary = image[y1:y2, x1:x2]
        # resize pixels to the model size
        face_image = Image.fromarray(face_boundary)
        face_image = face_image.resize(required_size)
        face_array = np.asarray(face_image)
        face_images.append(face_array)

    return face_images

faces = detector.detect_faces(newimg)
extracted =  extract_face_from_image(faces,newimg, required_size=(128, 128))
i=0
class_details = 'GSS101_2'
while i <  len(extracted):
    face = Image.fromarray(extracted[i])
    face.save('img/detected/detected_face_' + str(i)+ '.jpg')
    i=i+1

