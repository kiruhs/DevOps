import tkinter as tk
from tkinter import ttk

# def update_font_size(value):
#     try:
#         new_font_size = int(float(value))
#         label.config(font=("Arial", new_font_size))
#     except ValueError:
#         pass
#
# parent = tk.Tk()
# parent.title("Font size Control")
# font_size_scale = ttk.Scale(parent, from_=10, to=36, orient="horizontal", length=200, command=update_font_size)
# initial_font_size = 36
# font_size_scale.set(initial_font_size)
# label = ttk.Label(parent, text="Font Size", font=("Arial",initial_font_size))
# label.pack(pady=10)
# font_size_scale.pack(padx=20, pady=20)
# parent.mainloop()

# from tkcalendar import DateEntry
#
# def get_selected_date():
#     selected_date = cal.get_date()
#     selected_date_label.config(text=f"Selected date: {selected_date}")
# parent = tk.Tk()
# parent.title("Date entry example")
# parent.config(bg="lightgreen")
# parent.resizable(False,False)
# cal = DateEntry(parent, width=32, background="darkblue", foreground="white", borderwidth=2)
# get_date_button = tk.Button(parent,text="Get Selected Date", command=get_selected_date)
# get_date_button.pack(pady=10)
# selected_date_label = tk.Label(parent, text="", bg="lightgreen", font=("Helvetica", 12))
# selected_date_label.pack()
# cal.pack(padx=10, pady=10)
# parent.mainloop()


# import webview
#
# def open_site(url):
#     webview.create_window("Facebook", url=url)
#     webview.start()
#
# win = tk.Tk()
# but_f = tk.Button(win, text="Facebook", command=lambda url="https://www.facebook.com" : open_site(url))
# but_i = tk.Button(win, text="Instagram", command=lambda url="https://www.instagram.com" : open_site(url))
# but_c = tk.Button(win, text="CNN", command=lambda url="https://www.cnn.com" : open_site(url))
#
#
# win.grid_rowconfigure(2)
# win.grid_columnconfigure(0, weight=1)
# but_f.grid(row=0, column=0, sticky="nsew")
# but_i.grid(row=1, column=0, sticky="nsew")
# but_c.grid(row=2, column=0, sticky="nsew")
#
# win.mainloop()

# root = tk.Tk()
#
# class RedButton:
#     def __init__(self):
#         self.b = tk.Button(text="Red", width= 15, height=5)
#         self.b.bind("<Button-1>", self.change)
#         self.b.pack()
#         self.flag = 1
#     def change(self, event):
#         if self.flag%2 == 1:
#             self.b['fg'] = 'red'
#             self.b['activeforeground'] = 'red'
#         else:
#             self.b['fg'] = 'green'
#             self.b['activeforeground'] = 'green'
#         self.flag +=1
#
# RedButton()
# root.mainloop()

# def do_popup(event):
#     try:
#         m.tk_popup(event.x_root, event.y_root)
#     except:
#         pass
#     finally:
#         m.grab_release()
#
# root = tk.Tk()
# l = tk.Label(root, text="Right-click display menu", width=40, height=20)
# l.pack()
# m = tk.Menu(root, tearoff=0)
# m.add_command(label="Cut", command=lambda : print("Cut"))
# m.add_command(label="Copy")
# m.add_command(label="Paste")
# m.add_command(label="Reload")
# m.add_separator()
# m.add_command(label="Rename")

#
# l.bind("<Button-3>", do_popup)
#
# root.mainloop()

