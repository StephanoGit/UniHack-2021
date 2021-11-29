import cv2
from imutils.video import WebcamVideoStream
import numpy as np
from pyzbar.pyzbar import decode
import PIL


class VideoCamera(object):
    def __init__(self):
        self.stream = WebcamVideoStream(src=0).start()

    def __del__(self):
        self.stream.stop()

    def get_frame(self):
        image = self.stream.read()

        for barcode in decode(image):
            myData = barcode.data.decode('utf-8')
            dataList = myData.split()
            ticketNumber = dataList[0]
            Depature = dataList[1]
            Destination = dataList[2]
            Day = dataList[3]

            text = "Ticket Number: " + ticketNumber + " \nDepature: " + Depature + " \nDestination: " + Destination + " \nDay: " + Day

            for i, line in enumerate(text.split('\n')):
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(image, [pts], True, (255, 0, 255), 5)
                pts2 = barcode.rect
                cv2.putText(image, line, (pts2[0], pts2[1] + i * 30 - 100), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)


        ret, jpeg = cv2.imencode('.jpg', image)
        data = []
        data.append(jpeg.tobytes())
        return data