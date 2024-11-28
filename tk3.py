import tkinter as tk
from tkinter import ttk

# def resize_font(event):
#     width = event.width
#     height = event.height
#     # font_size =int(min(width,height)/10)
#     font_size = int((width**2 + height**2)**0.5/15)
#     label.config(font=("Arial", font_size))
#
# root = tk.Tk()
# root.title("Dynamic font resize")
# root.geometry("300x150+100+60")
# label = tk.Label(root, text="Resize the window", font=("Arial", 20))
# label.pack(expand=True, fill=tk.BOTH)
# root.bind("<Configure>", resize_font)
# root.mainloop()

# ============================

# root = tk.Tk()
# root.title("Checkbox")
#
# button = tk.Button(root, text="Resize me", bg='lightblue')
# button.grid(row=0, column=0, sticky="nsew")
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.mainloop()

# my_boolean_var = tk.BooleanVar()
# my_checkbox = ttk.Checkbutton(text="Check if true", variable=my_boolean_var)
# my_checkbox.pack()

# def spinbox_change():
#     value = spinbox.get()
#     print("Value changed to ", value)
#
# root.geometry("300x200")
# spinbox = tk.Spinbox(root, from_=0, to=100, width=100, relief="sunken", repeatdelay=500, repeatinterval=100,
#                      font=('Arial',12), bg='lightgrey', fg='blue', command=spinbox_change)
#
# spinbox.config(justify="center", wrap=True, cursor="hand1", bd=3, fg='red', increment=10)
# spinbox.pack(padx=30, pady=30)
# root.mainloop()

#

# from tkinter.font import Font
# root = tk.Tk()
# root.geometry("300x200")
# text_var = tk.DoubleVar()
# text_var.set(45.45)
# spin_box = tk.Spinbox(root, from_=0.6, to=50.0, increment=0.01, textvariable=text_var, fg='blue',
#                       justify='right', wrap=True,
#                       font=Font(family='Helvetica', size=36, weight='bold'))
#
# spin_box.pack()
# root.mainloop()


# window = tk.Tk()
# mytext = tk.Text(window)
# mytext.insert('1.0', "-Python exercises, solutions -")
# mytext.insert('1.19', "Practice, ")
# mytext.delete('1.0','1.4')
# mytext.delete('end - 2 chars')
# mytext.delete("1.0", "end")
# mytext.pack()
# window.mainloop()


# window = tk.Tk()
# window.title("Radiobutton")
# window.geometry("350x200")
# #------------
# v = tk.StringVar(window, value='1') # and add to each radiobutton "variable=v"
# #------------
# radio1 = tk.Radiobutton(window, text="First", value=1, variable=v)
# radio2 = tk.Radiobutton(window, text="Second", value=2, variable=v)
# radio3 = tk.Radiobutton(window, text="Thirst", value=3, variable=v)
# radio1.grid(column=0, row=0)
# radio2.grid(column=1, row=0)
# radio3.grid(column=2, row=0)
#
# window.mainloop()


# import tkinter.scrolledtext as tks
#
# window = tk.Tk()
# window.title("Scrolled text")
# window.geometry("350x200")
# txt = tks.ScrolledText(window, width=40, height=10)
# txt.grid(column=0, row=0)
# window.mainloop()
#
# window = tk.Tk()
# window.geometry("350x200")
# label1 = tk.Label(window, text= "A list of favorite languages..." )
# listbox = tk.Listbox(window)
# listbox.insert(1, "Python")
# listbox.insert(2, "Java")
# listbox.insert(3, "C++")
# listbox.insert(4, "JavaScript")
# label1.pack()
# listbox.pack()
# window.mainloop()

# def create_tab(tab, txt):
#     label = tk.Label(tab, text=txt)
#     label.pack(padx=20, pady=20)


# parent = tk.Tk()
# parent.title("Tabbed notebook")
# notebook = ttk.Notebook(parent)
#
# tab1 = tk.Frame(notebook)
# tab2 = tk.Frame(notebook)
# tab3 = tk.Frame(notebook)
# # content of tab pages
# notebook.add(tab1, text="Java")
# notebook.add(tab2, text="Python")
# notebook.add(tab3, text="C++")
#
# create_tab(tab1, "Java Exercise")
# create_tab(tab2, "Python Exercise")
# create_tab(tab3, "C++ Exercise")
# notebook.pack(padx=10, pady=10, fill="both", expand=True)
# parent.mainloop()

# Treeview
# root = tk.Tk()
# root.title("Treeview")
# treeview = ttk.Treeview(root)
# item = treeview.insert("", tk.END, text="Item 1")
# subitem = treeview.insert(item, tk.END, text="Subitem level1")
# subsubitem = treeview.insert(subitem, tk.END, text="Subitem level2")
# item2 = treeview.insert("", tk.END, text="Item 2")
# treeview.pack()
# root.mainloop()


# root = tk.Tk()
# root.title("Pizza favorites")
# style = ttk.Style()
# style.theme_use('clam')
# style.configure("Treeview", background= "green", foreground="white")
# style.configure("Treeview.Heading", background= "grey", foreground="white")
# treeview = ttk.Treeview(root)
# treeview['columns'] = ("Name", "ID", "Pizza type")
# treeview.column("#0", width=120)
# treeview.column("Name", width=120)
# treeview.column("ID", width=120)
# treeview.column("Pizza type", width=120)
#
# treeview.heading("#0", text="Number")
# treeview.heading("Name", text="Name")
# treeview.heading("ID", text="ID")
# treeview.heading("Pizza type", text="Pizza type")
#
# treeview.insert("", 'end', values=("John", 12345, "Peperoni"))
#
# treeview.config(style="Treeview.Heading")
# treeview.pack(padx=10, pady=10)
# root.mainloop()

# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *
