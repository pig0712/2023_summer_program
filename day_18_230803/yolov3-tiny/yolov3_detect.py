from djitellopy import tello
import cv2 as cv2
import numpy as np
import time

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()

# 전체 창 크기
frameWidth = 1000
frameHeight = 750

# 중앙 사각형 범위
deadZone=130

# Yolo 로드
net = cv2.dnn.readNet("C:/Users/koll2/OneDrive/summer_program_2023/day_18_230803/yolov3-tiny/yolov3-tiny6_best.weights", "C:/Users/koll2/OneDrive/summer_program_2023/day_18_230803/yolov3-tiny/yolov3-tiny61.cfg")
classes = []
with open("C:/Users/koll2/OneDrive/summer_program_2023/day_18_230803/yolov3-tiny/obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# 이미지 가져오기
def video_stream():
    while True:
        img = drone.get_frame_read().frame

        if img is None:
            continue

        img = cv2.resize(img, (640,640))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # 정보를 화면에 표시
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
                    # 좌표
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[0]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

        cv2.imshow('object_detection', img)

        if cv2.waitKey(20) & 0xFF == 27:
            drone.streamoff()
            break


if __name__ == '__main__':
    video_stream()


