import cv2,os,urllib.request
import numpy as np
import face_recognition
from PIL import Image

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success,image = self.video.read()

        recs = []

        #test_img = face_recognition.load_image_file(image)
        test_img = image

        try:
            test_img_rec = face_recognition.face_locations(test_img)
            for j in range(len(test_img_rec)):
                recs.append(j)     
        except:
            pass

        for i in range(len(recs)):
            cv2.rectangle(test_img,(test_img_rec[recs[i]][3],test_img_rec[recs[i]][2]),(test_img_rec[recs[i]][1],test_img_rec[recs[i]][0]),(255,0,255),2)

        frame_flip = cv2.flip(test_img,1)

        ret,jpeg = cv2.imencode('.jpg',frame_flip)
        #return len(recs)
        return jpeg.tobytes()