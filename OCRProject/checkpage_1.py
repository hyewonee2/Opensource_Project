import tkinter as tk
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("알고먹자")
        self.geometry("400x400+100+100")

        # 체크되면 TRUE를 가짐
        self.hindu_checked = tk.BooleanVar()
        self.muslim_checked = tk.BooleanVar()
        self.allergies_checked = tk.BooleanVar()

        # 이미지 로드
        script_dir = os.path.dirname(__file__)  # 스크립트의 디렉토리 경로
        image_hindu_path = os.path.join(script_dir, "ImageFile", "hindu.png")
        image_muslim_path = os.path.join(script_dir, "ImageFile", "muslim.png")

        self.image_hindu = tk.PhotoImage(file=image_hindu_path)
        self.image_hindu = self.image_hindu.subsample(4)

        self.image_muslim = tk.PhotoImage(file=image_muslim_path)

        # 체크박스 생성 및 이미지 삽입
        tk.Checkbutton(self, text="Hindu", image=self.image_hindu, variable=self.hindu_checked, compound=tk.RIGHT).pack(anchor=tk.W)
        tk.Checkbutton(self, text="Muslim", image=self.image_muslim, variable=self.muslim_checked, compound=tk.RIGHT).pack(anchor=tk.W)
        tk.Checkbutton(self, text="Allergies", variable=self.allergies_checked).pack(anchor=tk.W)

        # 확인 버튼 생성
        button = tk.Button(self, text="확인", command=self.show_checked)
        button.pack(pady=10)

    # 확인 버튼 클릭 시 체크박스 상태를 확인하고 함수를 호출하는 함수
    def show_checked(self):
        if self.hindu_checked.get():
            #연결지점
            #이미지 삽입 페이지로 이동
            print("Hindu 체크됨")
        if self.muslim_checked.get():
            #연결지점
            #이미지 삽입 페이지로 이동
            print("Muslim 체크됨")
        if self.allergies_checked.get():
            #연결지점
            #알러지 세부 체크 페이지로 이동
            print("Allergies 체크됨")

if __name__ == "__main__":
    app = App()
    app.mainloop()
