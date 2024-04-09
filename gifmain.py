import cv2
import imageio

cam=cv2.VideoCapture(0)
 
if not cam.isOpened():
    print("Cannot open camera")
captures=[]

while True:
    ret,frame=cam.read()

    cv2.imshow("frame",frame)
    key=cv2.waitKey(0)
    if key==ord("c"):
        captures.append(frame)
    elif key==ord("q"):
        break


filename = input("Enter name of gif (without extension): ")
gif = filename + ".gif"
print(gif)

with imageio.get_writer(gif,mode="I") as writer:
    for i,frame in enumerate(captures):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        writer.append_data(rgb_frame)
        