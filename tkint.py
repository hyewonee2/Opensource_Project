import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")]
    )
    if file_path:
        load_image(file_path)

def load_image(file_path):
    image = Image.open(file_path)
    image.thumbnail((400, 400))  # 이미지 크기 조정
    photo = ImageTk.PhotoImage(image)

    # 이미지를 보여줄 레이블 설정
    image_label.config(image=photo)
    image_label.image = photo  # 이미지 객체를 전역 변수로 유지
    root.update()  # GUI 업데이트

# 메인 윈도우 생성
root = tk.Tk()
root.title("이미지 선택기")

# 프레임 생성
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# 버튼 생성 및 배치
button = tk.Button(frame, text="이미지 열기", command=open_file)
button.pack()

# 이미지 표시할 레이블 생성 및 배치
image_label = tk.Label(frame)
image_label.pack(pady=10)

# GUI 실행
root.mainloop()

