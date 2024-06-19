import sys
import cv2
import numpy as np
import pytesseract
import imutils
from imutils.perspective import four_point_transform
from imutils.contours import sort_contours
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

def plt_imshow(title='image', img=None, figsize=(8, 5)):
    plt.figure(figsize=figsize)
    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []
            for i in range(len(img)):
                titles.append(title)
        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()

def preprocess_image(image):
    # 그레이스케일 변환
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 노이즈 제거 (가우시안 블러 사용)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # 이미지 이진화 (Otsu's Binarization 사용)
    _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return gray_image, blurred_image, binary_image

def main(image_path):
    # 로컬 파일 시스템에서 이미지 읽기
    org_image = cv2.imread(image_path)

    # 원본 이미지 시각화
    plt_imshow("Original Image", org_image)

    # 이미지 전처리
    gray_image, blurred_image, binary_image = preprocess_image(org_image)
    plt_imshow(["Gray Image", "Blurred Image", "Binary Image"], [gray_image, blurred_image, binary_image])

    # 이미지 리사이즈 및 에지 검출
    image = imutils.resize(binary_image, width=500)
    ratio = org_image.shape[1] / float(image.shape[1])
    edged = cv2.Canny(blurred_image, 75, 200)
    plt_imshow("Edged Image", edged)

    # 컨투어 찾기 및 정렬
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    # 4개의 꼭지점을 갖는 도형 검출
    exampleCnt = None
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            exampleCnt = approx
            break

    if exampleCnt is None:
        raise Exception("Could not find receipt outline.")
    
    # 윤곽 그리기 및 시각화
    output = image.copy()
    cv2.drawContours(output, [exampleCnt], -1, (0, 255, 0), 2)
    plt_imshow("Example Image Outline", output)

    # 원본 이미지에 윤곽 기반으로 이미지 보정
    example = four_point_transform(org_image, exampleCnt.reshape(4, 2) * ratio)
    plt_imshow("Example Image Transform", example)

    # OCR 적용
    ocr_result = pytesseract.image_to_string(example)
    print("OCR Result:\n", ocr_result)

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("이미지 선택기")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button = QPushButton("이미지 열기")
        self.button.clicked.connect(self.open_file)
        self.layout.addWidget(self.button)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "이미지 파일 열기", "", "이미지 파일 (*.png *.jpg *.jpeg *.bmp *.gif);;모든 파일 (*.*)", options=options)
        if file_path:
            self.load_image(file_path)
            main(file_path)  # 이미지 경로를 main 함수로 전달하여 처리

    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaled(400, 400)
        self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageWindow()
    window.show()
    sys.exit(app.exec_())
