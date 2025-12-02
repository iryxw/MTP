import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x500")
root.title("Блокнот с вкладками")

notebook = ttk.Notebook(root)

tab1 = tk.Frame(notebook)
label1 = tk.Label(tab1, text="Заметки", font=("Arial", 14))
label1.pack(pady=10)
text1 = tk.Text(tab1, height=20, width=60)
text1.pack(pady=10)

tab2 = tk.Frame(notebook)
label2 = tk.Label(tab2, text="Список задач", font=("Arial", 14))
label2.pack(pady=10)
text2 = tk.Text(tab2, height=20, width=60)
text2.pack(pady=10)

tab3 = tk.Frame(notebook)
label3 = tk.Label(tab3, text="Идеи", font=("Arial", 14))
label3.pack(pady=10)
text3 = tk.Text(tab3, height=20, width=60)
text3.pack(pady=10)

notebook.add(tab1, text="Заметки")
notebook.add(tab2, text="Задачи")
notebook.add(tab3, text="Идеи")

notebook.pack(expand=True, fill="both")

root.mainloop()