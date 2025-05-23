import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

def start_project(mode):
    try:
        subprocess.run([sys.executable, "main.py", mode])
    except Exception as e:
        messagebox.showerror("Ошибка запуска", str(e))

root = tk.Tk()
root.title("Cube3D v3.2.6 Launcher")
root.geometry("400x300")
tk.Label(root, text="Выберите тип проекта:", font=("Arial", 14)).pack(pady=10)

for mode in ["3D", "2D"]:
    tk.Button(root, text=f"Запустить {mode}", font=("Arial", 12),
              command=lambda m=mode: start_project(m)).pack(pady=5)

tk.Button(root, text="Выход", command=root.quit).pack(side="bottom", pady=20)
root.mainloop()
