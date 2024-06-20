import tkinter as tk
import os
import sys
import cv2
import pytesseract as pt
from tkinter import messagebox
from allergychecker import AllergyChecker
from OCRresult import ImageOCRWindow, OCRResultWindow
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# 글로벌 변수로 checked_list 선언
checked_list = []

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("알고먹자")
        self.geometry("700x700+100+100")

        # 체크되면 TRUE를 가짐
        self.hindu_checked = tk.BooleanVar()
        self.muslim_checked = tk.BooleanVar()
        self.allergies_checked = tk.BooleanVar()

        # 이미지 로드
        image_hindu_path = "ImageFile/hindu.png"
        image_muslim_path = "ImageFile/muslim.png"
        image_allergies_path = "ImageFile/allergies.png"

        self.image_hindu = tk.PhotoImage(file=image_hindu_path).subsample(3, 3)
        self.image_muslim = tk.PhotoImage(file=image_muslim_path).subsample(3, 3)
        self.image_allergies = tk.PhotoImage(file=image_allergies_path).subsample(3, 3)


        self.image_hindu = tk.PhotoImage(file=image_hindu_path)
        self.image_muslim = tk.PhotoImage(file=image_muslim_path)
        self.image_allergies = tk.PhotoImage(file=image_allergies_path)

        # 체크박스 생성 및 이미지 삽입
        tk.Checkbutton(self, text="힌두교(Hindu)", variable=self.hindu_checked, compound=tk.BOTTOM).grid(row=0, column=0, padx=20, pady=10)
        tk.Label(self, image=self.image_hindu).grid(row=1, column=0, padx=20, pady=10)
        
        tk.Checkbutton(self, text="이슬람교(Muslim)", variable=self.muslim_checked, compound=tk.BOTTOM).grid(row=0, column=1, padx=20, pady=10)
        tk.Label(self, image=self.image_muslim).grid(row=1, column=1, padx=20, pady=10)
        
        tk.Checkbutton(self, text="알러지(Allergies)", variable=self.allergies_checked, compound=tk.BOTTOM).grid(row=0, column=2, padx=20, pady=10)
        tk.Label(self, image=self.image_allergies).grid(row=1, column=2, padx=20, pady=10)

        # 확인 버튼 생성
        button = tk.Button(self, text="확인", command=self.show_checked)
        button.grid(row=2, columnspan=3, pady=20)

    # 확인 버튼 클릭 시 체크박스 상태를 확인하고 함수를 호출하는 함수
    def show_checked(self):
        global checked_list
        # checked_list 초기화
        checked_list.clear()
        checked_cow = ['cow']
        checked_pig = ['pig']

        if self.hindu_checked.get():
            checked_list.append('소고기')
            checked_list.append('쇠고기')
            self.destroy()
            app2 = QApplication(sys.argv)
            window = ImageOCRWindow(checked_list, checked_cow)
            window.show()
            sys.exit(app2.exec_())

        if self.muslim_checked.get():
            checked_list.append('돼지')
            self.destroy()
            app2 = QApplication(sys.argv)
            window = ImageOCRWindow(checked_list, checked_pig)
            window.show()
            sys.exit(app2.exec_())

        if self.allergies_checked.get():
            checked_list.append('allergies')
            self.destroy()
            root = tk.Tk()
            app3 = AllergyChecker(root)
            root.mainloop()
            
    # 알러지 리스트 반환
    def get_checked_list(self):
        return checked_list

if __name__ == "__main__":
    app = App()
    app.mainloop()
