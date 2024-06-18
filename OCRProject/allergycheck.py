import tkinter as tk
from PIL import Image, ImageTk

# 창 생성
root = tk.Tk()
root.title("알고먹자")

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
    img = img.resize((64, 64), Image.ANTIALIAS)
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

# 함수 리스트
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
button = tk.Button(root, text="확인", command=show_checked)
button.grid(row=4, column=0, columnspan=5)

# GUI 루프 시작
root.mainloop()
