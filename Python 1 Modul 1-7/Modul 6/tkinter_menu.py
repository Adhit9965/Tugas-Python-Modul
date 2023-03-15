import tkinter as tk

root = tk.Tk()
root.geometry('400x200+500+200')

menubar = tk.Menu(root)

file = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file)

file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="save")
file.add_command(label="close")

file.add_separator()
file.add_command(label="Exit", command=root.quit)

edit = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut")
edit.add_command(label="copy")
edit.add_command(label="Paste")

root.config(menu=menubar)
root.mainloop()