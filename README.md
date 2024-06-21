## Opensource Project: 알고 먹자

## Images 프로젝트 이미지
![image](https://github.com/hyewonee2/Opensource_Project/assets/165885976/efdcfb1b-b269-455d-ad63-53e3e195026e)
![image](https://github.com/hyewonee2/Opensource_Project/assets/165885976/d2114204-55b8-49ad-b96d-a2abba365e0a)
![image](https://github.com/hyewonee2/Opensource_Project/assets/165885976/f74bf9bf-b2ac-4d02-809c-561e7dd424ed)
![image](https://github.com/hyewonee2/Opensource_Project/assets/165885976/ea08257c-2a52-4cc7-be5b-fe5e3ad4d972)




 ## Technologies Used

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

## Installation

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

## Features
  By using the program, foreign workers in Korea can check whether pork, beef, or their allergies are included in the food. You can see the selection window and the results window consisting of pictograms.
  
## Project Structure

```  
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
├──testimage/
│   ├── imgtest.jpg
│   ├── imgtest2.jpg
│   ├── imgtest3.jpg
│   ├── imgtest4.jpg
│   └── imgtest5.jpg
└── ImageFile/
    ├── ok.png
    └── various food image.png ...```
