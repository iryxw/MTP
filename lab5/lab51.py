import tkinter as tk
from tkinter import messagebox

def on_button_click(value):
  current = entry.get()
  entry.delete(0, tk.END)
  entry.insert(tk.END, current + str(value))

def on_clear():
  entry.delete(0, tk.END)

def on_equal():
  try:
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
  except:
    messagebox.showerror("Ошибка", "Некорректный ввод")

root = tk.Tk()
root.geometry("300x400")
root.title("Калькулятор")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill=tk.X, padx=10, pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
  '7', '8', '9', '/',
  '4', '5', '6', '*',
  '1', '2', '3', '-',
  '0', '.', '=', '+'
]

row, col = 0, 0
for button in buttons:
  if button == '=':
    tk.Button(buttons_frame, text=button, width=5, height=2, command=on_equal).grid(row=row, column=col)
  else:
    tk.Button(buttons_frame, text=button, width=5, height=2, command=lambda v=button: on_button_click(v)).grid(row=row, column=col)
  col += 1
  if col > 3:
    col = 0
    row += 1

tk.Button(buttons_frame, text="C", width=5, height=2, command=on_clear).grid(row=4, column=0, columnspan=4, sticky="we")

root.mainloop()