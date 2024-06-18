import sys
import os
import tkinter as tk
from PIL import Image, ImageTk
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import pytesseract as pt


# Tesseract OCR 실행 파일 경로 설정
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'--oem 1 --psm 3'
example = ["설탕", "닭", "포도당", "비타민"]

class OCRResultWindow(QWidget):
    def __init__(self, ocr_result):
        super().__init__()
        self.setWindowTitle("OCR 결과")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # OCR 결과를 출력할 QLabel 추가
        for i in example:
            label = QLabel()
            if i in ocr_result:
                label.setText(i)
            else:
                label.setText("OCR 결과에 '%s'이 포함되어 있지 않습니다." % i)
            layout.addWidget(label)

class ImageOCRWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("이미지 OCR")
        self.setGeometry(100, 100, 800, 800)  # 창의 위치와 크기 설정

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
                self.show_ocr_result_window(ocr_result)

    def perform_ocr(self, file_path):
        try:
            image = Image.open(file_path)
            print("이미지를 성공적으로 열었습니다.")

            # 전처리된 이미지로 OCR 수행
            text = pt.image_to_string(image, lang='kor', config=custom_config)
            if text.strip():  # 텍스트가 비어 있지 않은지 확인
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

    def show_ocr_result_window(self, result):
        self.ocr_result_window = OCRResultWindow(result)  # 인스턴스를 클래스 속성으로 저장
        self.ocr_result_window.show()

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

    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaled(400, 400)
        self.image_label.setPixmap(pixmap)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("알고먹자")
        self.geometry("400x500+100+100")

        # 체크되면 TRUE를 가짐
        self.hindu_checked = tk.BooleanVar()
        self.muslim_checked = tk.BooleanVar()
        self.allergies_checked = tk.BooleanVar()

        # 이미지 로드
        image_hindu_path = "ImageFile/hindu.png"
        image_muslim_path = "ImageFile/muslim.png"

        self.image_hindu = tk.PhotoImage(file=image_hindu_path)
        self.image_muslim = tk.PhotoImage(file=image_muslim_path)

        # 체크박스 생성 및 이미지 삽입
        tk.Checkbutton(self, text="Hindu", image=self.image_hindu, variable=self.hindu_checked, compound=tk.RIGHT).pack(anchor=tk.W)
        tk.Checkbutton(self, text="Muslim", image=self.image_muslim, variable=self.muslim_checked, compound=tk.RIGHT).pack(anchor=tk.W)
        tk.Checkbutton(self, text="Allergies", variable=self.allergies_checked).pack(anchor=tk.W)

        # 확인 버튼 생성
        button = tk.Button(self, text="확인", command=self.show_checked)
        button.pack(pady=10)

    def show_checked(self):
        if self.hindu_checked.get():
            self.destroy()
            self.show_image_window()
            print("Hindu 체크됨")
        if self.muslim_checked.get():
            self.destroy()
            self.show_image_window()
            print("Muslim 체크됨")
        if self.allergies_checked.get():
            self.destroy()
            self.show_allergies_window()
            print("Allergies 체크됨")

    def show_image_window(self):
        app = QApplication(sys.argv)
        window = ImageWindow()
        window.show()
        sys.exit(app.exec_())

    def show_allergies_window(self):
        # 창 생성   
        self.allergies_root = tk.Tk()
        self.allergies_root.title("알고먹자")

        
        # 체크박스 상태를 저장할 변수 생성
        check_vars = [tk.IntVar() for _ in range(20)]
        # 체크박스 이름 리스트 (20개, 한국어와 영어 병기)
        check_names = ["달걀(Egg)", "우유(Milk)", "밀(Wheat)", "콩(Soy)", "땅콩(Peanut)", "옥수수(Corn)", "메밀(Buckwheat)", "버섯(Mushroom)", "생선(Fish)", "조개(Shellfish)", "바나나(Banana)", "오징어(Squid)", "두유(Soy Milk)", "딸기(Strawberry)", "고추(Pepper)", "키위(Kiwi)", "게(Crab)", "치즈(Cheese)", "토마토(Tomato)", "새우(Shrimp)"]

        # 이미지 파일 경로 리스트 (20개)
        image_files = ["ImageFile/egg.png", "ImageFile/milk.png", "ImageFile/wheat.png", "ImageFile/soy.png", "ImageFile/peanut.png", "ImageFile/corn.png", "ImageFile/buckwheat.png", "ImageFile/mushroom.png", "ImageFile/fish.png", "ImageFile/shellfish.png", "ImageFile/banana.png", "ImageFile/squid.png", "ImageFile/soy_milk.png", "ImageFile/strawberry.png", "ImageFile/pepper.png", "ImageFile/kiwi.png", "ImageFile/crab.png", "ImageFile/cheese.png", "ImageFile/tomato.png", "ImageFile/shrimp.png"]

        # 크기를 조정한 이미지 객체 리스트
        images = []

        # 이미지를 로드하고 크기를 조정
        for image_file in image_files:
            img = Image.open(image_file)
            img = img.resize((64, 64), Image.LANCZOS)  # Image.LANCZOS로 수정
            img = ImageTk.PhotoImage(img)
            images.append(img)

        # 체크박스 생성
        check_buttons = [
            tk.Checkbutton(root, text=check_names[i], variable=check_vars[i], image=images[i], compound='left', padx=2)
            for i in range(20)
        ]

        # 체크박스 배치
        for i in range(4):
            for j in range(5):
                check_buttons[i * 5 + j].grid(row=i, column=j, sticky='w')

        # 각 체크박스에 대한 함수를 정의
        def function_A():
            print("옵션 A가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_B():
            print("옵션 B가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_C():
            print("옵션 C가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_D():
            print("옵션 D가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_E():
            print("옵션 E가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_F():
            print("옵션 F가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_G():
            print("옵션 G가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_H():
            print("옵션 H가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_I():
            print("옵션 I가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_J():
            print("옵션 J가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_K():
            print("옵션 K가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_L():
            print("옵션 L가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_M():
            print("옵션 M가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_N():
            print("옵션 N가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_O():
            print("옵션 O가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_P():
            print("옵션 P가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_Q():
            print("옵션 Q가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_R():
            print("옵션 R가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_S():
            print("옵션 S가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        def function_T():
            print("옵션 T가 선택되었습니다.")
            # 추가 동작을 여기에 정의

        functions = [function_A, function_B, function_C, function_D, function_E, function_F, function_G, function_H, function_I, function_J, function_K, function_L, function_M, function_N, function_O, function_P, function_Q, function_R, function_S, function_T]

        # 확인 버튼 클릭 시 체크박스 상태를 확인하고 함수를 호출하는 함수
        def show_checked():
            checked_any = False
            for i, var in enumerate(check_vars):
                if var.get():  # 체크된 경우
                    functions[i]()
                    checked_any = True

                    if not checked_any:
                        print("bye")

        # 확인 버튼 생성    
        button = tk.Button(self.allergies_root, text="확인", command=self.show_image_window_from_allergies)
        button.grid(row=4, column=0, columnspan=5)

        self.allergies_root.mainloop()

    def show_image_window_from_allergies(self):
        self.allergies_root.destroy()
        self.show_image_window()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    