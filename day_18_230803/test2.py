from djitellopy import tello
import cv2
import numpy as np
import time


def drone_control(target_x, target_y):

    if target_x<130:
        drone.move_left(30)
        time.sleep(1)
    if target_x>190:
        drone.move_right(30)
        time.sleep(1)



# 이미지 가져오기
def video_stream():
    takeoffindex=False

    while True:
        img = drone.get_frame_read().frame


        if img is None:
            continue

        img = cv2.resize(img, (320,320))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channels = img.shape

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
                if confidence > 0.3:
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
                color = colors
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

                # 객체가 인식되었을 때, 드론을 움직이도록 설정합니다.
                target_x = x + w // 2
                target_y = y + h // 2


                # 드론을 추적하는 로직을 구현합니다.
                if not takeoffindex:
                    drone.takeoff()
                    time.sleep(1)
                    drone.send_rc_control(0,0,0,0)
                    time.sleep(3)
                    takeoffindex = True
                else:
                    drone_control(target_x, target_y)

        cv2.imshow('object_detection', img)


        if cv2.waitKey(70) & 0xFF == 27:
            drone.streamoff()
            drone.land()
            break



if __name__ == '__main__':

    drone = tello.Tello()
    drone.connect()
    print(drone.get_battery())

    drone.streamon()

    # Yolo 로드
    net = cv2.dnn.readNet("C:/Users/koll2/OneDrive/summer_program_2023/day_18_230803/yolov3-tiny/yolov3-tiny6_best.weights", "C:/Users/koll2/OneDrive/summer_program_2023/day_18_230803/yolov3-tiny/yolov3-tiny61.cfg")
    classes = []
    with open("C:/Users/koll2/OneDrive/summer_program_2023/day_18_230803/yolov3-tiny/obj.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = [255,255,255]

    video_stream()