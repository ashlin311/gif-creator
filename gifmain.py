from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
import cv2
import imageio

t=Tk()
t.title("Gif Creator")
t.geometry("850x250")

def capture():
    cam=cv2.VideoCapture(0)
    if not cam.isOpened():
        tkinter.messagebox.showinfo("","Cannot Open Camera")
    captures=[]

    while True:
        ret,frame=cam.read()
        cv2.imshow("frame",frame)
        key=cv2.waitKey(0)
        if key==ord("c"):
            captures.append(frame)
        elif key==ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()
    filename=simpledialog.askstring(title="Gif Name",prompt="Enter Gif name\t\t")
    gif = filename + ".gif"
    

    with imageio.get_writer(gif,mode="I") as writer:
        for i,frame in enumerate(captures):
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            writer.append_data(rgb_frame)

l1=Label(text="GIF Maker",width=58,height=5,font=("Gothic 20 italic bold"),background="#CFE964")
l1.grid(row=3,column=2,rowspan=3,columnspan=3)
l2=Label(text="Make a GIF using:",width=50,height=1,font=("Courier 15"),background="#CFE964")
l2.grid(row=5,column=2,rowspan=1,columnspan=2)

options=Frame(t)
options.grid(row=7,column=2,columnspan=2)
b1=Button(options,text="Web Cam",height=2,width=10,font=("Times"),command=capture)
b1.grid(row=0,column=0,padx=150)
b2=Button(options,text="Existing pictures",height=2,width=15,font=("Times"))
b2.grid(row=0,column=3,padx=100)

mainloop()