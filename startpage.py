
import sys
import os
import tkinter as tk
from PIL import Image, ImageTk
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

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

        self.hindu_checked = tk.BooleanVar()
        self.muslim_checked = tk.BooleanVar()
        self.allergies_checked = tk.BooleanVar()

        image_hindu_path = "ImageFile/hindu.png"
        image_muslim_path = "ImageFile/muslim.png"

        self.image_hindu = tk.PhotoImage(file=image_hindu_path)
        self.image_muslim = tk.PhotoImage(file=image_muslim_path)

        tk.Checkbutton(self, text="Hindu", image=self.image_hindu, variable=self.hindu_checked, compound=tk.RIGHT).pack(anchor=tk.W)
        tk.Checkbutton(self, text="Muslim", image=self.image_muslim, variable=self.muslim_checked, compound=tk.RIGHT).pack(anchor=tk.W)
        tk.Checkbutton(self, text="Allergies", variable=self.allergies_checked).pack(anchor=tk.W)

        button = tk.Button(self, text="확인", command=self.show_checked)
        button.pack(pady=10)

    def show_checked(self):
        if self.hindu_checked.get() or self.muslim_checked.get():
            print("Hindu")
            self.destroy()
            self.show_image_window()
            print("Hindu")
        if self.allergies_checked.get():
            self.destroy()
            self.show_allergies_window()

    def show_image_window(self):
        app = QApplication(sys.argv)
        window = ImageWindow()
        window.show()
        sys.exit(app.exec_())

    def show_allergies_window(self):
        self.allergies_root = tk.Tk()
        self.allergies_root.title("알고먹자")
    
        check_vars = [tk.IntVar() for _ in range(3)]
        check_names = ["달걀(Egg)", "우유(Milk)", "밀(Wheat)"]

        base_dir = os.path.dirname(__file__)  # 현재 파일의 디렉토리
        image_files = [os.path.join(base_dir, "ImageFile", image) for image in ["egg.png", "milk.png", "wheat.png"]]

        images = []
        for image_file in image_files:
            img = Image.open(image_file)
            img = img.resize((64, 64), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            images.append(img)

        check_buttons = [
            tk.Checkbutton(self.allergies_root, text=check_names[i], variable=check_vars[i], image=images[i], compound='left', padx=2)
            for i in range(3)
        ]

        for i in range(3):
            check_buttons[i].grid(row=0, column=i, sticky='w')

        button = tk.Button(self.allergies_root, text="확인", command=self.show_image_window_from_allergies)
        button.grid(row=1, column=0, columnspan=3)

        self.allergies_root.mainloop()

    def show_image_window_from_allergies(self):
        self.allergies_root.destroy()
        self.show_image_window()


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

if __name__ == "__main__":
    app = App()
    app.mainloop()
