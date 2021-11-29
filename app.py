from flask import Flask, render_template, request, Response
from camera import VideoCamera
import pandas as pd
import machine
import cv2
import time
import json

app = Flask(__name__)

@app.route('/')
def index():
    title = "Rental Car Time Prediction"
    return render_template("index.html", title=title)

@app.route('/results', methods=["POST"])
def results():
    title = "Expected Time"

    departure = request.form.get("departure")
    destination = request.form.get("destination")
    date = request.form.get("date")
    day = int(pd.Timestamp(date).dayofweek) + 1

    final_result = machine.getFromString(departure, destination, int(day))

    return render_template("form.html", title=title,
            departure=departure, destination=destination, day=day, final_result=final_result)

@app.route('/cam')
def sign_page():
    return render_template("camera.html")

@app.route('/camera',methods=['POST'])
def camera():
    cap=cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite("static/cam.png",img)

        time.sleep(0.1)
        return json.dumps({'status': 'OK', 'result': "static/cam.png"})
        if cv2.waitKey(0) & 0xFF ==ord('q'):
            break
    cap.release()
    return json.dumps({'status': 'OK', 'result': "static/cam.png"});

def gen(camera):
    while True:
        data = camera.get_frame()
        frame=data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0')