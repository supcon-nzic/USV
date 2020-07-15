from flask import Flask, render_template, Response
import cv2
import numpy as np
import time

class Hot_fram():
    def __init__(self,back_path):
        self.cap = cv2.VideoCapture(0)
        #self.cap.set(cv2.CAP_PROP_FPS,1)
        self.cap.set(3,480)
        self.cap.set(4,320)
        resize_fr = np.zeros((32,32,3),dtype=np.uint8)
        self.jpeg = cv2.imencode('.jpg', resize_fr)
    def getPicture(self):
        ret, frame = self.cap.read()
        if ret == True:
           #print(frame.shape)
           resize_fr = cv2.resize(frame,(320,480))
           #resize_fr = frame
           #ret, self.jpeg = cv2.imencode('.jpg', resize_fr,[int(cv2.IMWRITE_JPEG_QUALITY), 55])
           ret, self.jpeg = cv2.imencode('.jpg', resize_fr)
        print(len(self.jpeg)/1000,"kB")
        return self.jpeg.tobytes()

 

app = Flask(__name__)

@app.route('/')  
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.getPicture()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed') 
def video_feed():
    return Response(gen(Hot_fram('back.jpg')),
                    mimetype='multipart/x-mixed-replace; boundary=frame')   

if __name__ == '__main__':
    ip,port = '192.168.8.100',703
    app.run(host=ip, debug=True, port=port) 
