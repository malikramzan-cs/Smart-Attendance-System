from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recognition_System")

        # First header image (left side)
        img1 = Image.open(r"D:\Smart_Attendance_System\Images_GUI\logo.jfif")
        img1 = img1.resize((455, 130), Image.LANCZOS)  # One-third the width of the window
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=0, y=0, width=455, height=130)

        # Second header image (center)
        img2 = Image.open(r"D:\Smart_Attendance_System\Images_GUI\uni1.jfif")
        img2 = img2.resize((455, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb2 = Label(self.root, image=self.photoimg2)
        f_lb2.place(x=455, y=0, width=455, height=130)

        # Third header image (right side)
        img3 = Image.open(r"D:\Smart_Attendance_System\Images_GUI\uni3.jfif")  
        img3 = img3.resize((455, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb3 = Label(self.root, image=self.photoimg3)
        f_lb3.place(x=910, y=0, width=455, height=130)

        # Background image
        bg1 = Image.open(r"D:\Smart_Attendance_System\Images_GUI\bg1.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title of the pannel
        title_lb1 = Label(bg_img, text="Developer Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Labels with header images
        label1 = Label(bg_img, text="Developed By:", font=("tahoma", 15, "bold"), bg="white", fg="black")
        label1.place(x=50, y=170, width=220, height=40)  # Below the first header image
        
        #label 2 for develpoed by
        label1 = Label(bg_img, text="Muhammad Ramzan", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        label1.place(x=50, y=240, width=220, height=40)

        

        label3 = Label(bg_img, text="FA22-BCS-145", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        label3.place(x=50, y=300, width=220, height=40)
        
        # Buttons section
        # ---------------------------------------------------------------------------------------------------------------
        # Developer button 1
        dev_img_btn1 = Image.open(r"D:\Smart_Attendance_System\Images_GUI\ramzan1.jfif")
        dev_img_btn1 = dev_img_btn1.resize((250, 250), Image.LANCZOS)
        self.dev_img1 = ImageTk.PhotoImage(dev_img_btn1)

        dev_b1 = Button(bg_img, image=self.dev_img1, cursor="hand2")
        dev_b1.place(x=300, y=150, width=250, height=250)

        

        
        # for 2nd image
        label2 = Label(bg_img, text="M.Usman Younas ", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        label2.place(x=750, y=180, width=230, height=40)  

        label4= Label(bg_img, text="FA22-BCS-137", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        label4.place(x=750, y=250, width=230, height=40)
        
        # Button 2
        dev_img_btn2 = Image.open(r"D:\Smart_Attendance_System\Images_GUI\usman.jpeg")
        dev_img_btn2 = dev_img_btn2.resize((250, 250), Image.LANCZOS)
        self.dev_img2 = ImageTk.PhotoImage(dev_img_btn2)

        dev_b2 = Button(bg_img, image=self.dev_img2, cursor="hand2")
        dev_b2.place(x=1000, y=150, width=250, height=250)

        


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
