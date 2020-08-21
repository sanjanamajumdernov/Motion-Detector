import cv2, time, pandas
from datetime import datetime

first_frame= None
status_list= [None,None]
times=[]
df= pandas.DataFrame(columns=["Start","End"])
video= cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_delta = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)

    cnts, _ = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        time.append(datetime.now())

        # Appending End time of motion
    if status_list[-1] == 0 and status_list[-2] == 1:
        time.append(datetime.now())

        # Displaying image in gray_scale
    cv2.imshow("Gray Frame", gray)

    print(status_list)
    print(times)

for i in range (0,len(times),2):
    df = df.append({"start":times[1],"End":times[i+1]},ignore_index = True)

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()