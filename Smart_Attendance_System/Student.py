from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")

        #-----------Variables-------------------
        self.var_student_id=StringVar()
        self.var_student_name=StringVar()
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_section=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mobl_no=StringVar()
        self.var_teacher=StringVar()
        self.var_photo_sample=StringVar()
        self.var_address=StringVar()

    # This part is for setting images labels
        # first header image  
        img=Image.open(r"D:\Smart_Attendance_System\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # this sets image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

         # backgorund image 
        bg1=Image.open(r"D:\Smart_Attendance_System\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # sets image as lable and placing it on background image
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        # setting title of student pannel
        title_lb1 = Label(bg_img,text="Welcome to the Student Pannel",font=("Aptos (Body)",30,"bold"),bg="white",fg="darkblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Creating main Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Aptos (Body)",12,"bold"),fg="darkblue")
        left_frame.place(x=10,y=10,width=665,height=480)

        # Current Course 
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("Aptos (Body)",12,"bold"),fg="darkblue")
        current_course_frame.place(x=10,y=5,width=635,height=150)

        #label Department
        dep_label=Label(current_course_frame,text="Department",font=("Aptos (Body)",12,"bold"),bg="white",fg="darkblue")
        dep_label.grid(row=0,column=0,padx=5,pady=15)

        #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_department,width=15,font=("Aptos (Body)",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","BS-CS","BS-EE","BS-Mechenical","BS-SE","BS-Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W) # positioning the label on window using the grid layout
                                                               #sticky=w means align combo box to west (left)side of grid 
        # -----------------------------------------------------

        #label Course
        cou_label=Label(current_course_frame,text="Course",font=("Aptos (Body)",12,"bold"),bg="white",fg="darkblue")
        cou_label.grid(row=0,column=2,padx=5,pady=15)

        #combo box 
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=15,font=("Aptos (Body)",12,"bold"),state="readonly")
        cou_combo["values"]=("Select Course","DIP","Operating System","Statistics","Database System","Professional paractices")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)

        #-------------------------------------------------------------

        #label Year
        year_label=Label(current_course_frame,text="Year",font=("Aptos (Body)",12,"bold"),bg="white",fg="darkblue")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=("Aptos (Body)",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2018-22","2019-23","2020-24","2021-25","2022-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        #-----------------------------------------------------------------

        #label Semester 
        year_label=Label(current_course_frame,text="Semester",font=("Aptos (Body)",12,"bold"),bg="white",fg="darkblue")
        year_label.grid(row=1,column=2,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("Aptos (Body)",12,"bold"),state="readonly")
        year_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=5,pady=15,sticky=W)

        # Student Information frame labels
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("Aptos (Body)",12,"bold"),fg="darkblue")
        class_Student_frame.place(x=10,y=160,width=650,height=230)

        #Student id label
        studentId_label = Label(class_Student_frame,text="Student-ID:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_student_id,width=15,font=("Aptos (Body)",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student name
        student_name_label = Label(class_Student_frame,text="Student-Name:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_student_name,width=15,font=("Aptos (Body)",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #section
        student_div_label = Label(class_Student_frame,text="Section:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        student_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_section,width=13,font=("Aptos (Body)",12,"bold"),state="readonly")
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #roll No
        student_roll_no_label = Label(class_Student_frame,text="Roll-No:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        student_roll_no_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll_no,width=15,font=("Aptos (Body)",12,"bold"))
        student_roll_no_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        student_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("Aptos (Body)",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date of Birth
        student_dob_label = Label(class_Student_frame,text="DOB:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("Aptos (Body)",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Email
        student_email_label = Label(class_Student_frame,text="Email:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("Aptos (Body)",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Phone Number
        student_mob_label = Label(class_Student_frame,text="Mobl_No:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mobl_no,width=15,font=("Aptos (Body)",12,"bold"))
        student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        student_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("Aptos (Body)",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #Teacher Name
        student_tutor_label = Label(class_Student_frame,text="Teacher Name:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        student_tutor_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("Aptos (Body)",12,"bold"))
        student_tutor_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take Photo Sample",variable=self.var_photo_sample,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        radiobtn1=ttk.Radiobutton(class_Student_frame,text="No Photo Sample",variable=self.var_photo_sample,value="No")
        radiobtn1.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("Aptos (Body)",12,"bold"),fg="white",bg="darkblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("Aptos (Body)",12,"bold"),fg="white",bg="darkblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("Aptos (Body)",12,"bold"),fg="white",bg="darkblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("Aptos (Body)",12,"bold"),fg="white",bg="darkblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo",width=9,font=("Aptos (Body)",12,"bold"),fg="white",bg="darkblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        #update photo button
        update_photo_btn=Button(btn_frame,text="Update Photo",width=11,font=("Aptos (Body)",12,"bold"),fg="white",bg="darkblue")
        update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)





        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Aptos (Body)",12,"bold"),fg="darkblue")
        right_frame.place(x=680,y=10,width=660,height=480)

        #Search System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Aptos (Body)",12,"bold"),fg="darkblue")
        search_frame.place(x=10,y=5,width=635,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("Aptos (Body)",12,"bold"),fg="darkblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("Aptos (Body)",12,"bold"),state="readonly")
        search_combo["values"]=("Select","roll_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("Aptos (Body)",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("Aptos (Body)",12,"bold"),fg="white",bg="darkblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("Aptos (Body)",12,"bold"),fg="white",bg="darkblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("stID","stName","Dept","Course","Year","Sem","Sec","Gender","DOB","Mob-No","roll_no","Email","Teacher","Photo_sample","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("stID",text="student_id")
        self.student_table.heading("stName",text="student_name")
        self.student_table.heading("Dept",text="department")
        self.student_table.heading("Course",text="course")
        self.student_table.heading("Year",text="year")
        self.student_table.heading("Sem",text="semester")
        self.student_table.heading("Sec",text="section")
        self.student_table.heading("Gender",text="gender")
        self.student_table.heading("DOB",text="dob")
        self.student_table.heading("Mob-No",text="mobl_no")
        self.student_table.heading("roll_no",text="roll_No")
        self.student_table.heading("Email",text="email")
        self.student_table.heading("Teacher",text="teacher")
        self.student_table.heading("Photo_sample",text="photo_sample")
        self.student_table.heading("Address",text="address")
        self.student_table["show"]="headings"


        # Set Width of Colums 
        self.student_table.column("stID",width=110)
        self.student_table.column("stName",width=110)
        self.student_table.column("Dept",width=110)
        self.student_table.column("Course",width=110)
        self.student_table.column("Year",width=110)
        self.student_table.column("Sem",width=110)
        self.student_table.column("Sec",width=110)
        self.student_table.column("Gender",width=110)
        self.student_table.column("DOB",width=110)
        self.student_table.column("Mob-No",width=110)
        self.student_table.column("roll_no",width=110)
        self.student_table.column("Email",width=110)
        self.student_table.column("Teacher",width=110)
        self.student_table.column("Photo_sample",width=110)
        self.student_table.column("Address",width=110)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ===============================Function Decleration==============================
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_student_id.get()=="" or self.var_student_name.get()=="" or self.var_section.get()=="" or self.var_roll_no.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mobl_no.get()=="" or self.var_teacher.get()==""or self.var_photo_sample.get()=="" or self.var_address.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='3502511',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_student_id.get(),
                self.var_student_name.get(),
                self.var_department.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_section.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_mobl_no.get(),
                self.var_roll_no.get(),
                self.var_email.get(),
                self.var_teacher.get(),
                self.var_photo_sample.get(),
                self.var_address.get()
                ))

                conn.commit()
                self.fetch_data() # function call hai jo updated data ko display karega.
                conn.close()
                messagebox.showinfo("Success","All Records Saved, Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='3502511',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall() 

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit() # Database ke changes save karta hai (data insert hone ke baad).
        conn.close()

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_student_id.set(data[0]),
        self.var_student_name.set(data[1]),
        self.var_department.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_section.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mobl_no.set(data[9]),
        self.var_roll_no.set(data[10]),
        self.var_email.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_photo_sample.set(data[13]),
        self.var_address.set(data[14])
    # ========================================Update Function==========================
    def update_data(self):
        if  self.var_student_id.get()=="" or self.var_student_name.get()=="" or self.var_course.get()=="Select Course" or self.var_department.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or  self.var_section.get()=="" or self.var_roll_no.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mobl_no.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='3502511',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set student_name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,section=%s,Gender=%s,DOB=%s,mobl_no=%s,roll_no=%s,Email=%s,Teacher=%s,Photo_Sample=%s,Address=%s where Student_ID=%s",( 
                    self.var_student_name.get(),
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_section.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mobl_no.get(),
                    self.var_roll_no.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_photo_sample.get(),
                    self.var_address.get(),
                    self.var_student_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_student_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='3502511',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_student_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_student_id.set(""),
        self.var_student_name.set(""),
        self.var_department.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_section.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_mobl_no.set(""),
        self.var_roll_no.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_photo_sample.set(""),
        self.var_address.set("")
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='3502511',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT student_id,student_name,department,course,year,semester,section,Gender,DOB,mobl_no,roll_no,email,teacher,photo_sample,address FROM student where roll_no='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_student_id.get()=="" or self.var_student_name.get()=="" or self.var_department.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_section.get()=="" or self.var_roll_no.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mobl_no.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='root', password='3502511',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set student_name=%s,department=%s,course=%s,year=%s,semester=%s,section=%s,gender=%s,dob=%s,mobl_no=%s,roll_no=%s,email=%s,teacher=%s,photo_sample=%s,address=%s where student_id=%s",( 
                    self.var_student_name.get(),
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_section.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mobl_no.get(),
                    self.var_roll_no.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_photo_sample.get(),
                    self.var_address.get(),
                    self.var_student_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_croped(img):
                    # convert iamges from brg to gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum neigbhor 5
                    for (x,y,w,h) in faces: #for generating rectangle thats why we take x,y,width,height
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)  #for openning camera
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(300,300))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path='data_img/student.'+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13  or int(img_id)==100: #13 is for if I press enter it will stop #talking image samples
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
