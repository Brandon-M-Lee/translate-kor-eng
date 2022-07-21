import tkinter as tk
from tkinter import messagebox
from backend import *

window = tk.Tk()

window.title('한영키를 잘못 설정했다면 사용하시오')
window.geometry('800x400')
window.resizable(0, 0)

def trans(event):
    s = entry.get()
    if s.upper() != s or s.lower() != s:
        text = eng_to_kor(s)
        label.config(text = text)
        copy_to_clipboard(text)
        messagebox.showinfo('복사 완료', '클립보드에 복사되었습니다')
    else:
        text = kor_to_eng(s)
        label.config(text = text)
        copy_to_clipboard(text)
        messagebox.showinfo('복사 완료', '클립보드에 복사되었습니다')

entry=tk.Entry(window, width=50)
entry.bind("<Return>", trans)
entry.pack(pady=50)

label = tk.Label(window)
label.pack()

window.mainloop()