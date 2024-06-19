import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# 글로벌 변수로 checked_list 선언
checked_list = []

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

# Allergy_Check 클래스 정의
class Allergy_Check:
    def __init__(self, root):
        self.root = root
        self.root.title("알고먹자")

        # 체크박스 상태를 저장할 변수 생성
        self.check_vars = [tk.IntVar() for _ in range(20)]

        # 체크박스 이름 리스트 (20개, 한국어와 영어 병기)
        self.check_names = ["달걀(Egg)", "우유(Milk)", "밀(Wheat)", "콩(Soy)", "땅콩(Peanut)", "옥수수(Corn)", "메밀(Buckwheat)", "버섯(Mushroom)", "생선(Fish)", "조개(Shellfish)", "바나나(Banana)", "오징어(Squid)", "두유(Soy Milk)", "딸기(Strawberry)", "고추(Pepper)", "키위(Kiwi)", "게(Crab)", "치즈(Cheese)", "토마토(Tomato)", "새우(Shrimp)"]

        # 이미지 파일 경로 리스트 (20개)
        self.image_files = ["ImageFile/egg.png", "ImageFile/milk.png", "ImageFile/wheat.png", "ImageFile/soy.png", "ImageFile/peanut.png", "ImageFile/corn.png", "ImageFile/buckwheat.png", "ImageFile/mushroom.png", "ImageFile/fish.png", "ImageFile/shellfish.png", "ImageFile/banana.png", "ImageFile/squid.png", "ImageFile/soy_milk.png", "ImageFile/strawberry.png", "ImageFile/pepper.png", "ImageFile/kiwi.png", "ImageFile/crab.png", "ImageFile/cheese.png", "ImageFile/tomato.png", "ImageFile/shrimp.png"]

        # 크기를 조정한 이미지 객체 리스트
        self.images = []

        # 이미지를 로드하고 크기를 조정
        for image_file in self.image_files:
            img = Image.open(image_file)
            img = img.resize((64, 64), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.images.append(img)

        # 체크박스 생성
        self.check_buttons = [
            tk.Checkbutton(self.root, text=self.check_names[i], variable=self.check_vars[i], image=self.images[i], compound='left', padx=2)
            for i in range(20)
        ]

        # 체크박스 배치
        for i in range(4):
            for j in range(5):
                self.check_buttons[i * 5 + j].grid(row=i, column=j, sticky='w')

        # 확인 버튼 생성
        self.button = tk.Button(self.root, text="확인", command=self.show_checked)
        self.button.grid(row=4, column=0, columnspan=5)

        # checked_allergy 리스트
        self.checked_allergy = []

    # 체크박스 상태를 업데이트하는 함수
    def update_checked_allergy(self):
        self.checked_allergy = [self.check_names[i].split("(")[0] for i, var in enumerate(self.check_vars) if var.get()]

    # 확인 버튼 클릭 시 체크박스 상태를 확인하는 함수
    def show_checked(self):
        self.update_checked_allergy()
        if not self.checked_allergy:
            print("bye")
        else:
            print("Checked allergies: ", self.checked_allergy)

    # 알러지 리스트 반환
    def get_checked_allergy(self):
        return self.checked_allergy

def main():
    app = App()
    app.mainloop()

    selected_list = app.get_checked_list()

    if not selected_list:
        root = tk.Tk()
        root.withdraw()  # 메인 윈도우 숨김
        messagebox.showinfo("알고먹자", "You can eat it.")
        root.destroy()
        
    elif selected_list == ['allergies']:
        root = tk.Tk()
        app = Allergy_Check(root)
        root.mainloop()

if __name__ == "__main__":
    main()
