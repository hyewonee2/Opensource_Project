import tkinter as tk
from tkinter import messagebox
from app import App
from allergy_check import Allergy_Check

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
