import tkinter as tk
import random

def change_color():
  colors = ["red", "green", "blue", "yellow", "purple", "orange"]
  panel.config(bg=random.choice(colors))

root = tk.Tk()
root.geometry("400x300")
root.title("Цветная панель")

panel = tk.Frame(root, width=350, height=200, bg="white")
panel.pack(pady=20, padx=20)

button = tk.Button(root, text="Изменить цвет", command=change_color)
button.pack()

root.mainloop()