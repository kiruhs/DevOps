import tkinter as tk
from tkinter import ttk
from time import sleep
from tkinter.constants import DISABLED, RIGHT, LEFT, BOTTOM, TOP

# window = tk.Tk()
# window.title('My App')
# window.geometry("300x300")
# window.minsize(100,70)
# window.maxsize(350, 250)
# window.attributes('-fullscreen', True)
# window.resizable(False, False)
# window.attributes('-alpha', 0.5)
# window.attributes('-toolwindow', True)



# frame_add_form = tk.Frame(window, bg='green')
# frame_statistic = tk.Frame(window, width=150, height=150, bg='yellow')
# frame_list = tk.Frame(window, width=300, height=150, bg='blue')
#
# frame_add_form.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)
# frame_statistic.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)
# frame_statistic.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# frame_list.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# label = tk.Label(text="Hello DevOps!")
# label.pack()
# clicks = 0
# def click_button():
#     global clicks
#     clicks += 1
#     btn['text'] = f"Clicks: {clicks}"
#     if clicks >= 10:
#         label.destroy()
#     if clicks >=15:
#         window.quit()

# btn1 = tk.Button(text="Right", command=click_button) # , state=DISABLED) disables ['disables']
# btn2 = tk.Button(text="Left", command=click_button) # , state=DISABLED) disables ['disables']
# btn3 = tk.Button(text="Top", command=click_button) # , state=DISABLED) disables ['disables']
# btn4 = tk.Button(text="Bottom", command=click_button) # , state=DISABLED) disables ['disables']
# btn1.pack(side=RIGHT)
# btn2.pack(side=LEFT)
# btn3.pack(side=TOP)
# btn4.pack(side=BOTTOM)
# btn = tk.Button(text="Right", command=click_button)  # , state=DISABLED) disables ['disables']
#
# btn.place(relx=0.5, rely=0.5, anchor='c', width=50, height=30, relwidth=0.33, relheight=0.25)

# for r in range(3):
#     for c in range(3):
#         btn = tk.Button(text=f"({r+1},{c+1})")
#         btn.grid(row=r, column=c)
#
# btn = tk.Button(text='Spanned')
# btn.grid(row=3, column=0, columnspan=3, ipadx=15, ipady=5, sticky="WE")

# parent = tk.Tk()
# parent.title("Parent button")
# # my_button = tk.Button(parent, text="Quit", height=1, width=50, command=child.destroy)
# # my_button.pack()
# child = tk.Toplevel(parent)
# child.title("Child button")
# child.geometry("+300+250")
#
# def add_label():
#     my_label = tk.Label(parent, text='I am result of child button click')
#     my_label.pack()
#     my_entry = tk.Entry(parent)
#     my_entry.pack()
#     def add_entered_text():
#         my_txt = my_entry.get()
#         entered_text = tk.Label(child, text=my_txt)
#         entered_text.pack()
#     entry_button = tk.Button(parent, text='Enter', height=1, width=50, command=add_entered_text)
#     entry_button.pack()
#
# my_button2 = tk.Button(child, text="Add label", height=1, width=50, command=add_label, bg='yellow')
# my_button = tk.Button(parent, text="Quit", height=1, width=50, command=child.destroy)
# my_button.pack()
# my_button2.pack()
# parent.mainloop()
# child.mainloop()

# combobox

root = tk.Tk()
root.geometry("200x100")
my_str_var = tk.StringVar()
my_combobox = ttk.Combobox(root, textvariable=my_str_var, values=["JavaScript", "Linux", "Python"])
my_combobox.pack()

def selected(event):
    # получаем выделенный элемент
    selection = my_combobox.get()
    # print(selection)
    label["text"] = f"вы выбрали: {selection}"

label = tk.Label()
label.pack()
my_combobox.bind("<<ComboboxSelected>>",selected)
root.mainloop()