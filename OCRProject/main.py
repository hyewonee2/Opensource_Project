import tkinter as tk
from tkinter import messagebox

# 글로벌 변수로 checked_list 선언
checked_list = []


#첫페이지 class
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

    # 확인 버튼 클릭 시 체크박스 상태를 확인하고 함수를 호출하는 함수
    def show_checked(self):
        global checked_list
        # checked_list 초기화
        checked_list.clear()

        if self.hindu_checked.get():
            checked_list.append('cow')

        if self.muslim_checked.get():
            checked_list.append('pig')

        if self.allergies_checked.get():
            checked_list.append('allergies')

    # 알러지 리스트 반환
    def get_checked_list(self):
        return checked_list

def main():
    app = App()
    app.mainloop()

    selected_list = app.get_checked_list()

    if not selected_list:
        root = tk.Tk()
        root.withdraw()  # 메인 윈도우 숨김
        messagebox.showinfo("알고먹자", "You can eat it.")
        root.destroy()

if __name__ == "__main__":
    main()
