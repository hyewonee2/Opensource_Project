import tkinter as tk
from PIL import Image, ImageTk

class AllergyChecker:
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
