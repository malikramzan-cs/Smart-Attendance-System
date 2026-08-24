from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class ProjectDesc:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Description")
        self.root.geometry("1200x700")
        self.root.config(bg="white")

        # Top Image Section
        header_image = Image.open(r"D:\Smart_Attendance_System\Images_GUI\f_bg.jpg")
        header_image = header_image.resize((1200, 150), Image.LANCZOS)
        self.photo_header = ImageTk.PhotoImage(header_image)

        header_label = Label(self.root, image=self.photo_header, bg="white")
        header_label.place(x=0, y=0, width=1200, height=150)

        # Frame for Project Details
        desc_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        desc_frame.place(x=20, y=150, width=1100, height=500)

        # Project Description Title
        desc_title = Label(
            desc_frame,
            text="Smart Attendance Management System using Facial Recognition",
            font=("tahoma", 18, "bold"),
            bg="white",
            fg="navyblue",
            pady=10,
        )
        desc_title.pack(anchor="center", pady=10)

        # Scrollable Text Area for Details
        text_scroll = Scrollbar(desc_frame, orient=VERTICAL)
        self.project_text = Text(
            desc_frame,
            wrap=WORD,
            font=("tahoma", 14),
            bg="lightgrey",
            fg="black",
            yscrollcommand=text_scroll.set,
        )
        text_scroll.pack(side=RIGHT, fill=Y)
        self.project_text.pack(fill=BOTH, expand=True, padx=10, pady=10)
        text_scroll.config(command=self.project_text.yview)

        # Add content to the text area
        self.add_project_details()

    def add_project_details(self):
        details = """\
The Smart Attendance Management System is designed to modernize traditional attendance tracking using facial recognition technology.

**Focus of the Project:**
This project leverages artificial intelligence and computer vision to identify individuals and mark their attendance automatically. The focus is on increasing accuracy, saving time, and reducing manual effort in attendance management.

**How it Works:**
1. Faces of individuals (students, employees, etc.) are captured through a camera.
2. The system processes these faces, compares them with a pre-trained dataset, and identifies them using facial recognition techniques.
3. Once identified, the system marks attendance and stores it in a centralized database.
4. Attendance reports can be generated for analysis or record-keeping.

**Benefits of the Project:**
- **Efficiency:** Eliminates the need for manual attendance tracking.
- **Accuracy:** Reduces human errors in maintaining attendance logs.
- **Time-Saving:** Attendance is recorded within seconds.
- **Security:** Ensures that only authorized individuals are marked as present.
- **Data Insights:** Allows easy generation of attendance records and analytics.

This project is ideal for schools, universities, and workplaces aiming to adopt smart technologies for daily operations."""

        self.project_text.insert(END, details)
        self.project_text.config(state=DISABLED)  # Make the text read-only


if __name__ == "__main__":
    root = Tk()
    app = ProjectDesc(root)
    root.mainloop()
