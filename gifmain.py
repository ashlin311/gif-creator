import cv2
import imageio
from tkinter import *

top=Tk()
top.title("Gif Creator")
top.geometry("780x500")

print("HI HELLO Welcome to my gif creator")
while True:

    print("""1)Create a gif with your webcam
    2)Create a gif with existing pictures
    3) Exit""")
    ch=int(input())
    if ch==1:
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
        cv2.destroyAllWindows()

        filename = input("Enter name of gif (without extension): ")
        gif = filename + ".gif"
        print(gif)

        with imageio.get_writer(gif,mode="I") as writer:
            for i,frame in enumerate(captures):
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                writer.append_data(rgb_frame)
    elif ch==3:
        print("Thank you")
        break
                