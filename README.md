# Smart-Attendance-System
A desktop-based Smart Attendance System built with Python, Tkinter, OpenCV, and MySQL. It uses Haar Cascades for real-time face detection and the LBPH algorithm for face recognition to automatically mark student attendance and manage records.

This system automates the process of attendance marking by using **Haar Cascade Classifiers** for real-time face detection and the **Local Binary Patterns Histograms (LBPH)** algorithm for high-accuracy face recognition.

---

## 🚀 Key Features

*   **Student Panel (CRUD Operations)**: Register new students, edit details, search student information, and delete records.
*   **Automatic Dataset Generator**: Capture up to 100 face samples per student using your webcam, which are automatically pre-processed and stored in grayscale.
*   **Face Recognizer**: Launch a live webcam feed to recognize registered students in real-time and mark their attendance.
*   **Data Training Engine**: Train the face classifier model (`clf.xml`) with a single click inside the application.
*   **Attendance Panel**: View, search, and export attendance records saved dynamically in CSV format.
*   **Interactive Desktop GUI**: Sleek background graphics, customized icons, and banners for user-friendly navigation.

---

## 🛠️ Tech Stack & Libraries

*   **Programming Language**: Python 3.x
*   **GUI Framework**: Tkinter (Python standard library)
*   **Computer Vision**: OpenCV (OpenCV-contrib-python for LBPH face recognizer)
*   **Image Processing**: Pillow (PIL)
*   **Database**: MySQL
*   **Database Connector**: `mysql-connector-python`

---


    ```

### 💡 Step-by-Step Usage Guide:
1.  **Register a Student**:
    *   Open the **Student Panel**.
    *   Fill in all the required details (Name, ID, Roll No, Department, etc.).
    *   Click **Take Photo Sample** to open your webcam and capture face samples.
    *   Click **Save** to insert student details into the database.
2.  **Train the Dataset**:
    *   Go back to the home panel and open **Train Data**.
    *   Click the **Train Dataset** button. This reads the photos from the `data_img` directory and saves the trained classifier as `clf.xml`.
3.  **Real-Time Attendance Marking**:
    *   Open the **Face Detector** panel.
    *   Click the **Face Detector** button to open the live webcam stream.
    *   When the system recognizes a registered face, it will display the student's name and write the entry to the attendance log.
4.  **Manage Attendance**:
    *   Open the **Attendance** panel to view attendance lists, import/export CSV logs, or edit records.

---


## 📄 License
This project is open-source. Feel free to modify and adapt it for your own educational and development projects!
