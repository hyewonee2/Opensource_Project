import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QIcon
import cv2
import pytesseract as pt
from PIL import Image
from PyQt5.QtCore import Qt
import numpy as np
from PyQt5.QtGui import QPixmap

# Tesseract OCR 실행 파일 경로 설정
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'--oem 1 --psm 3'

class OCRResultWindow(QWidget):
    def __init__(self, ocr_result, checked_list, image_path):
        super().__init__()
        self.setWindowTitle("OCR 결과")
        self.setGeometry(100, 100, 800, 800)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # OCR 처리한 이미지 표시
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        # OCR 결과 텍스트 레이블
        for i in checked_list:
            label = QLabel()
            if i in ocr_result:
                label.setText("OCR 결과에 '%s'이 포함되어 있습니다." % i)
            else:
                label.setText("OCR 결과에 '%s'이 포함되어 있지 않습니다." % i)
            layout.addWidget(label)
        print(checked_list)



class ImageOCRWindow(QWidget):
    def __init__(self, checked_list):
        super().__init__()

        self.checked_list = checked_list

        self.setWindowTitle("이미지 OCR")
        self.setGeometry(100, 100, 800, 800)  # 창의 위치와 크기 설정
        self.setWindowIcon(QIcon("ImageFile/gal.png"))

        layout = QVBoxLayout(self)

        # 첫 번째 레이블
        label1 = QLabel("사진을 첨부해주세요.")
        label1.setStyleSheet("font-size: 40px; font-weight: bold; color: #333;")
        layout.addWidget(label1, alignment=Qt.AlignCenter)

        # 두 번째 레이블
        label2 = QLabel("Please attach a picture")
        label2.setStyleSheet("font-size: 40px; font-weight: bold; color: #333;")
        layout.addWidget(label2, alignment=Qt.AlignCenter)

        # 이미지 버튼
        self.button = QPushButton(self)
        self.button.setGeometry(300, 300, 200, 200)
        self.button.clicked.connect(self.open_file)
        icon = QIcon("ImageFile/gal.png")  # 여기에 이미지 파일 경로를 입력
        self.button.setIcon(icon)
        self.button.setIconSize(self.button.size() * 0.8)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 2px solid #cccccc;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        layout.addWidget(self.button)

        # 이미지를 표시할 레이블
        self.image_label = QLabel()
        layout.addWidget(self.image_label)

        self.ocr_result_window = None  # OCR 결과 창에 대한 참조를 유지하기 위한 변수

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "이미지 파일 열기", "", "이미지 파일 (*.png *.jpg *.jpeg *.bmp *.gif);;모든 파일 (*.*)", options=options)
        if file_path:
            # 이미지 OCR 수행
            ocr_result = self.perform_ocr(file_path)
            if ocr_result:
                self.show_ocr_result_window(ocr_result, file_path)

    def perform_ocr(self, file_path):
        try:
            image = Image.open(file_path)
            print("이미지를 성공적으로 열었습니다.")

            # 이미지 전처리
            processed_image = self.preprocess_image(image)

            # 전처리된 이미지로 OCR 수행
            text = pt.image_to_string(processed_image, lang='kor', config=custom_config)
            if text.strip():  # 텍스트가 비어 있지 않은지 확인
                print(text)
                return text
            else:
                print("OCR 결과가 비어 있습니다.")
                return None

        except FileNotFoundError:
            print("이미지 파일을 찾을 수 없습니다. 경로를 확인하세요.")
            return None
        except Exception as e:
            print("OCR 수행 중 오류 발생:", e)
            return None

    def preprocess_image(self, image):
        # 이미지를 numpy 배열로 변환
        img = np.array(image)

        # 그레이스케일 변환
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 이미지 이진화 (Otsu's Binarization 사용)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # PIL 이미지로 다시 변환
        processed_image = Image.fromarray(binary)
        return processed_image
        
    def show_ocr_result_window(self, result, file_path):
        self.ocr_result_window = OCRResultWindow(result, self.checked_list, file_path)  # 인스턴스를 클래스 속성으로 저장
        self.ocr_result_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 체크 리스트 예시
    checked_list = ["원재료1", "원재료2", "원재료3"]
    
    main_window = ImageOCRWindow(checked_list)
    main_window.show()
    
    sys.exit(app.exec_())
