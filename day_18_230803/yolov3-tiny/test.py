from djitellopy import Tello
import cv2
import numpy as np
import keyboard
import threading
import time

# Tello 드론 연결
drone = Tello()
drone.connect()
print(drone.get_battery())

# 드론 카메라 기능 시작
drone.streamon()

# 전체 창 크기
frameWidth = 1000
frameHeight = 750

# 중앙 사각형 범위
deadZone = 130

# YOLO 로드
net = cv2.dnn.readNet("path_to_yolov3_tiny_weights", "path_to_yolov3_tiny_cfg")
classes = []
with open("C:/Users/koll2/OneDrive/summer_program_2023/day_18_230803/yolov3-tiny/obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# 드론 이륙 함수
def takeoff():
    drone.takeoff()

# 드론 착륙 함수
def land():
    drone.land()


# # 드론을 움직이는 함수
# def move_drone(cx, cy, frame_width, frame_height):
#     if cx < int(frame_width / 2) - deadZone:
#         # 객체가 왼쪽에 위치할 때, 드론을 왼쪽으로 이동
#         drone.move_left(30)
#     elif cx > int(frame_width / 2) + deadZone:
#         # 객체가 오른쪽에 위치할 때, 드론을 오른쪽으로 이동
#         drone.move_right(30)
#     elif cy < int(frame_height / 2) - deadZone:
#         # 객체가 위에 위치할 때, 드론을 상승
#         drone.move_up(30)
#     elif cy > int(frame_height / 2) + deadZone:
#         # 객체가 아래에 위치할 때, 드론을 하강
#         drone.move_down(30)
#     else:
#         # 객체가 중앙에 위치할 때, 드론 멈춤
#         drone.send_rc_control(0, 0, 0, 0)

# 이미지 가져오기
def video_stream():
    # takeoff()  # 이륙

    while True:
        img = drone.get_frame_read().frame

        if img is None:
            continue

        img = cv2.resize(img, (640, 480))
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

        # 객체가 중앙에 인식되도록 드론 제어
        if len(boxes) > 0:
            cx = (boxes[0][0] + boxes[0][2]) // 2
            cy = (boxes[0][1] + boxes[0][3]) // 2
            # move_drone(cx, cy, frame_width=frameWidth, frame_height=frameHeight)

        # 화면에 객체 감지 결과를 표시
        cv2.imshow('object_detection', img)

        # 객체 인식과 드론 제어를 병렬로 처리하기 위해 일시적으로 정지
        time.sleep(0.01)

        # esc 키를 누르면 종료
        if cv2.waitKey(20) & 0xFF == 27:
            drone.streamoff()
            drone.land()
            break

if __name__ == '__main__':
    # 쓰레드 생성
    video_thread = threading.Thread(target=video_stream)

    # 쓰레드 시작
    video_thread.start()

    # 쓰레드 종료 대기
    video_thread.join()
