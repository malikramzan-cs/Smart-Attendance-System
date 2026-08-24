
from sys import path  # for accessing path 
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  # to handle images in the gui
import os             #for interacting with the file system
import mysql.connector     
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Face_Recognition:

    def __init__(self,root):   #self refers to class intance, a function can access objects and attributes of class
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Smart_Attendance_System\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\Smart_Attendance_System\Images_GUI\bg2.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)
    #=====================Attendance===================

    def mark_attendance(self,i,r,n):
        with open("ramzan_attnd.csv","r+",newline="\n") as f: #f reperesent file object, opens file for reading and writing
            myDatalist=f.readlines()
            name_list=[]   #list to store student ids that are already present in the file
            for line in myDatalist:
                entry=line.split((","))     #split each field with comma and create list entry
                name_list.append(entry[0])   #extract 0 index field, like (student_id) and ading it to name list

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")


    #================face recognition==================
    def face_recog(self):
        if hasattr(self, 'is_recognizing') and self.is_recognizing:
            return  # Prevent re-triggering
        self.is_recognizing = True  # Mark as recognizing

        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)  # scalefactor for the size of detected face,detect faces in the grayscale image

            coord = []  #initialize the list to store coordinates of the faces
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w]) # perdict is for confidence score of the prediction

                confidence = int((100 * (1 - predict / 300)))   #Converts the prediction score into a percentage to measure the confidence of recognition.

                conn = mysql.connector.connect(
                    username='root', password='3502511', host='localhost', database='face_recognition', port=3306)
                cursor = conn.cursor()

                cursor.execute("SELECT student_name FROM student WHERE student_id=%s", (id,))
                n = cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                cursor.execute("SELECT roll_no FROM student WHERE student_id=%s", (id,))
                r = cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                cursor.execute("SELECT student_id FROM student WHERE student_id=%s", (id,))
                i = cursor.fetchone()
                i = "+".join(i) if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Student_id:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2) #size of font, color,thickness
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll_no:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i, r, n)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):  #A function that calls draw_boundray to detect faces and draw rectangles around them, then returns the processed images
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)  #1.1 scale factor hai jo her baar 10% size reduce kr k detect kary ga face
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #Loads the Haar Cascade classifier for detecting faces
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        try:
            while True:
                ret, img = videoCap.read()
                if not ret:
                    print("Error accessing the camera. Exiting...")
                    break

                img = recognize(img, clf, faceCascade)
                cv2.imshow("Face Detector", img)  #Displays the processed image with face detection results

                key = cv2.waitKey(1)
                if key == 13 or key == 27:  # Enter or ESC to exit
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Release resources and close windows
            videoCap.release()
            cv2.destroyAllWindows()
            self.is_recognizing = False  # Reset the flag






if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()