import tkinter as tk

# 창 생성
root = tk.Tk()
root.title("알고먹자")

# 체크박스 상태를 저장할 변수 생성
check_vars = [tk.IntVar() for _ in range(6)]

# 체크박스 이름 리스트
check_names = ["랩틸리언", "유당불내증", "고혈압", "땅콩알러지", "힌두교", "몰몬교"]

# 체크박스 생성
check_buttons = [
    tk.Checkbutton(root, text=check_names[i], variable=check_vars[i])
    for i in range(6)
]

# 체크박스 배치
for i in range(3):
    for j in range(2):
        check_buttons[i * 2 + j].grid(row=i, column=j, sticky='w')

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

# 함수 리스트
functions = [function_A, function_B, function_C, function_D, function_E, function_F]

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
button.grid(row=3, column=0, columnspan=2)

# GUI 루프 시작
root.mainloop()
