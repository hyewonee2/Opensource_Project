<Project Name>  Opensource Project: 알고 먹자

<Images> 프로젝트 이미지
![image](https://github.com/hyewonee2/Opensource_Project/assets/165885976/efdcfb1b-b269-455d-ad63-53e3e195026e)
![image](https://github.com/hyewonee2/Opensource_Project/assets/165885976/d2114204-55b8-49ad-b96d-a2abba365e0a)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/ca2f03f3-2ead-48f1-b363-f731bc78aaf5/8684954d-69af-4e7b-9870-688720ff31a4/Untitled.png)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/ca2f03f3-2ead-48f1-b363-f731bc78aaf5/68874562-efc1-4194-9ec9-17016410aaa0/Untitled.png)![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/ca2f03f3-2ead-48f1-b363-f731bc78aaf5/bf2b9ffb-8b03-4f13-be4e-383fc71b5b1b/Untitled.png)

 <Technologies Used>

- **Programming Languages:**
  - Python

- **Frameworks and Libraries:**
  - Tkinter (for GUI development)
  - PyQt5 (for GUI development)
  - NumPy (for data processing)
  - OpenCV (cv2) (for image processing)
  - Pillow (PIL) (for image manipulation)

- **Tools:**
  - Tesseract OCR (pytesseract) (for optical character recognition)
  - Visual Studio Code (for development)

<Installation>

1. Clone the repository:
    ```bash
    git clone https://github.com/hyewonee2/Opensource_Project.git
    cd Opensource_Project
    ```

2. Create a virtual environment and activate it:

    **For Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```
5. Attach a image:
 you can download testimage file through our github or you can use your own image.

<Features>
  By using the program, foreign workers in Korea can check whether pork, beef, or their allergies are included in the food. You can see the selection window and the results window consisting of pictograms.
  
<Project Structure>
  
Opensource_Project/
│
├── README.md
├── requirements.txt
├──Main/ #Actual py files that you need to run this project.
│   ├── main.py
│   ├── app.py
│   ├── OCRResult.py
│   └── allergychecker.py
├──OCRProject/ #This is not neccesary files but you can see our development process.
│   ├── pyqt.py
│   ├── checkpage_1.py
│   ├── startwindow.py
│   ├── test.py
│   ├── testcolab.py
│   ├── testfile.py
│   └── allergychecker.py
└── ImageFile/
    ├── ok.png
    └── various food image.png ...
