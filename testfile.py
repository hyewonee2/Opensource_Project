import sys
import cv2
import numpy as np
import pytesseract as pt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image

# Tesseract OCR 실행 파일 경로 설정
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'--oem 1 --psm 3'

class ImageOCRWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("이미지 OCR")
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
            # 이미지 OCR 수행
            self.perform_ocr(file_path)

    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaled(400, 400)
        self.image_label.setPixmap(pixmap)

    def perform_ocr(self, file_path):
        try:
            image = Image.open(file_path)
            print("이미지를 성공적으로 열었습니다.")

            # 이미지 전처리
            processed_image = self.preprocess_image(image)

            # 전처리된 이미지로 OCR 수행
            text = pt.image_to_string(processed_image, lang='kor', config=custom_config)
            if text.strip():  # 텍스트가 비어 있지 않은지 확인
                print("OCR 결과:")
                print(text)
            else:
                print("OCR 결과가 비어 있습니다.")

        except FileNotFoundError:
            print("이미지 파일을 찾을 수 없습니다. 경로를 확인하세요.")
        except Exception as e:
            print("OCR 수행 중 오류 발생:", e)

    def preprocess_image(self, image):
        # 이미지를 numpy 배열로 변환
        img = np.array(image)

        # 그레이스케일 변환
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 가우시안 블러 적용
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 이미지 이진화 (Otsu's Binarization 사용)
        _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # 대비 조정 (CLAHE: Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        contrast = clahe.apply(binary)

        # PIL 이미지로 다시 변환
        processed_image = Image.fromarray(contrast)
        return processed_image

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageOCRWindow()
    window.show()
    sys.exit(app.exec_())
