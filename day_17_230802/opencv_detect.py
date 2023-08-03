# 필요 라이브러리
from djitellopy import tello
import cv2
import numpy as np


# tello 드론 연결
drone = tello.Tello()
drone.connect()
print(drone.get_battery())


# 카메라 기능 작동 시작
drone.streamon()

# 전체 창 크기
frameWidth = 1000
frameHeight = 750

# 중앙 사각형 범위
deadZone=130

def empty(a):
    pass

# HSV 값을 조정하는 창 생성
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",60,179,empty)
cv2.createTrackbar("HUE Max","HSV",100,179,empty)

cv2.createTrackbar("SAT Min","HSV",107,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)

cv2.createTrackbar("VALUE Min","HSV",89,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)

# 에지 검출을 위한 시작과 끝 임계값 조절 창 생성
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",166,255,empty)
cv2.createTrackbar("Threshold2","Parameters",171,255,empty)
cv2.createTrackbar("Area","Parameters",3750,30000,empty)


# 여러개의 이미지창을 하나로 쌓아서 보여주는 함수
def stackImages(scale,imgArray):


    rows = len(imgArray)
    cols = len(imgArray[0])


    rowsAvailable = isinstance(imgArray[0], list)

    # 첫번때 원소(이미지)의 가로세로 값
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]




    # 수평으로 이미지 쌓기
    if rowsAvailable:

        # 이미지의 크기를 조정하고 흑백이미지면 컬러로 변환함
        for x in range ( 0, rows):
            for y in range(0, cols):

                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1],imgArray[0][0].shape[0]), None, scale, scale)

                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)

        # 0으로 이루어진 행렬을 생성하여 빈 이미지 생성
        imageBlank = np.zeros((height, width, 3), np.uint8)

        # rows개의 빈 이미지 리스트 생성
        hor = [imageBlank]*rows

        # hor 리스트의 이미지를 수직으로 쌓아 최종 이미지 반환
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)




    # 수직으로 이미지 쌓기
    else:
        # 이미지의 크기를 조정하고 흑백이미지면 컬러로 변환함
        for x in range(0, rows):

            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        # 이미지를 수평으로 쌓음
        hor = np.hstack(imgArray)

        # 최종 이미지 반환
        ver = hor


    return ver



# 중앙 사각형에서 벗어났을시 벗어난 위치에 빨간표시, 검출된 물체의 윤곽선의 크기 값
def getContours(img,imgContour):

    # img의 윤곽선 검출 RETR_EXTERNAL는 바깥쪽 윤곽선, CHAIN_APPROX_NONE은 모든 윤곽선의 좌표
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        # cnt의 면적을 게산 후 area에 넣음
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")

        # 윤곽선 면적이 areaMin 보다 크면 윤곽선을 그림
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)

            # 윤곽선 둘레의 길이
            peri = cv2.arcLength(cnt, True)


            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            # print(len(approx))

            #  x, y : 사각형의 왼쪽 상단 모서리 좌표, w, h: 사각형의 너비와 높이
            x , y , w, h = cv2.boundingRect(approx)

            # 직사각형 그리기
            cv2.rectangle(imgContour, (x , y ), (x + w , y + h ), (0, 255, 0), 5)

            # 윤곽선의 꼭짓점 개수, 면적, 그리고 직사각형의 좌표를 텍스트로 표시
            cv2.putText(imgContour, "Points: " + str(len(approx)),
                        (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)

            cv2.putText(imgContour, "Area: " + str(int(area)),
                        (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)

            cv2.putText(imgContour, " " + str(int(x))+ " "+str(int(y)),
                        (x - 20, y- 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)


            # 사각형의 중심 계산
            cx = int(x + (w / 2))
            cy = int(y + (h / 2))



            if (cx <int(frameWidth/2)-deadZone):
                # 가로 / 2 - 데드존 위치에 검출됬을 경우 GO LEFT 글을 표기하고 30 왼쪽으로
                drone.move_left(30)
                cv2.putText(imgContour, " GO LEFT " , (20, 50), cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 255), 3)
                cv2.rectangle(imgContour,(0,int(frameHeight/2-deadZone)),
                              (int(frameWidth/2)-deadZone,int(frameHeight/2)+deadZone),
                              (0,0,255),cv2.FILLED)
                continue

            # 가로 / 2 + 데드존 위치에 검출됬을 경우 GO RIGHT 글을 표기하고 30 오른쪽으로
            elif (cx > int(frameWidth / 2) + deadZone):

                drone.move_right(30)
                cv2.putText(imgContour, " GO RIGHT ", (20, 50), cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 255), 3)
                cv2.rectangle(imgContour,(int(frameWidth/2+deadZone),int(frameHeight/2-deadZone))
                              ,(frameWidth,int(frameHeight/2)+deadZone),(0,0,255),cv2.FILLED)
                continue

            # 높이 / 2 - 데드존 위치에 검출됬을 경우 GO UP 글을 표기하고 30 상승
            elif (cy < int(frameHeight / 2) - deadZone):

                drone.move_up(30)
                cv2.putText(imgContour, " GO UP ", (20, 50),
                            cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 255), 3)
                cv2.rectangle(imgContour,(int(frameWidth/2-deadZone),0)
                              ,(int(frameWidth/2+deadZone),int(frameHeight/2)-deadZone),(0,0,255),cv2.FILLED)
                continue

            # 높이 / 2 + 데드존 위치에 검출됬을 경우 GO DOWN 글을 표기하고 30 하강
            elif (cy > int(frameHeight / 2) + deadZone):

                drone.move_down(30)
                cv2.putText(imgContour, " GO DOWN ", (20, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 1,(0, 0, 255), 3)
                cv2.rectangle(imgContour,(int(frameWidth/2-deadZone),int(frameHeight/2)+deadZone)
                              ,(int(frameWidth/2+deadZone),frameHeight),(0,0,255),cv2.FILLED)
                continue

            # 중심과 에지 객체의 중앙을 빨강선으로 연결
            cv2.line(imgContour, (int(frameWidth/2),int(frameHeight/2))
                     ,(cx,cy), (0, 0, 255), 3)



# 화면에 중앙점과 하늘색 선을 추가해주는 코드
def display(img):

    # 가로로 하늘색 선 생성
    cv2.line(img,(int(frameWidth/2)-deadZone,0)
             ,(int(frameWidth/2)-deadZone,frameHeight)
             ,(255,255,0),3)

    cv2.line(img,(int(frameWidth/2)+deadZone,0)
             ,(int(frameWidth/2)+deadZone,frameHeight)
             ,(255,255,0),3)

    # 중앙에 빨간 원 생성
    cv2.circle(img,(int(frameWidth/2),int(frameHeight/2)),5,(0,0,255),5)

    # 세로로 하늘색 선 생성
    cv2.line(img, (0,int(frameHeight / 2) - deadZone)
             ,(frameWidth,int(frameHeight / 2) - deadZone), (255, 255, 0), 3)
    cv2.line(img, (0, int(frameHeight / 2) + deadZone)
             ,(frameWidth, int(frameHeight / 2) + deadZone), (255, 255, 0), 3)



# 드론의 비디오, 영상처리를 위한 함수
def startvideo():
    # 이륙
    drone.takeoff()
    while True:
        # 드론 카메라 불러오기
        frame = drone.get_frame_read().frame

        # 원본 이미지를 용도에 맞게 색상 변환
        img = frame.copy()
        img  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        # 슬라이스로 바뀐 값 변수지정
        h_min = cv2.getTrackbarPos("HUE Min","HSV")
        h_max = cv2.getTrackbarPos("HUE Max", "HSV")
        s_min = cv2.getTrackbarPos("SAT Min", "HSV")
        s_max = cv2.getTrackbarPos("SAT Max", "HSV")
        v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
        v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

        # 영상 처리를 위한 가우시안과 지정한 최대, 최소의 hsv값 색상 cvt
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])

        mask = cv2.inRange(imgHsv,lower,upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        imgBlur = cv2.GaussianBlur(result, (7, 7), 1)
        imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)


        # 설정한 임계치 값
        threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
        threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

        # gray 스케일
        imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

        # 1로 이루어진 5*5 사각형 커널 생성
        kernel = np.ones((5, 5))

        # 이미지 팽창 실시
        imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

        getContours(imgDil, img)

        # 원본에 중앙 원과 각 지점 표시
        display(img)

        # 원본, 색 검출, 에지, 데드존 이미지를 한번에 표시해주는 코드
        stack = stackImages(0.7, ([img, result], [imgDil, img]))

        # 화면에 이미지창 생성
        cv2.imshow('Drone Video Stream', stack)

        # esc 키를 누르면 닫음
        if cv2.waitKey(1) & 0xFF == 27:
            drone.land()
            break

    # 드론 카메라 기능 정지
    drone.streamoff()


# 인터프리터에서 직접 실행했을 경우에만 실행하라는 코드
if __name__ == '__main__':
    startvideo()