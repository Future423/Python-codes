import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.configure(bg="white")
window.title("Mind Reading Program")
window.minsize(280,145)
window.maxsize(280,145)
global custom_font
custom_font = ("Arial", 12)
global fnt
fnt=("Aparajita",20)
label = tk.Label(window, text="Mind Reading Program",bg="white", font=fnt)
label.pack(pady=20)
def start_button_click():
    label.pack_forget()
    start_button.pack_forget()
    global updated_label
    updated_label = tk.Label(window, text="Enter a number",bg="white", font=fnt)
    updated_label.pack(pady=20)
    global entry
    entry = tk.Entry(window)
    entry.pack()
    #entry.configure(bg='azure1')
    def enter_button_click():
        global X
        X = entry.get()
        show_splash_window()
    global enter_button
    enter_button = tk.Button(window, text="Enter",font = ("Arial", 12), command=enter_button_click)
    enter_button.pack(pady=10)
start_button = tk.Button(window, text="  Start  ",font = ("Arial", 12), command=start_button_click)
start_button.pack(pady=10)
def show_splash_window():
    splash_window = tk.Toplevel(window)
    splash_window.title("Splash Window")
    splash_window.geometry("300x110")
    loading_label = tk.Label(splash_window, text="Loading",font=custom_font)
    loading_label.pack(pady=10)
    progress_bar = ttk.Progressbar(splash_window, mode="indeterminate", length=200, value=0, maximum=100,style="green.Horizontal.TProgressbar")
    progress_bar.pack(pady=10)
    style = ttk.Style()
    style.theme_use("default")
    style.configure("green.Horizontal.TProgressbar", background="green", troughcolor="white")
    splash_window.after(6000, lambda: show_main_window(splash_window))
    def update_loading_text():
        loading_label.config(text="Analysing Memory")
        splash_window.after(1500, lambda: loading_label.config(text="Reading Mind",font=custom_font))
        splash_window.after(3000, lambda: loading_label.config(text="Almost Complete",font=custom_font))
        splash_window.after(4500, lambda: loading_label.config(text="Come back here",font=custom_font))
    splash_window.after(1500, update_loading_text)
    progress_bar.start(5)
def show_main_window(splash_window):
    splash_window.destroy()
    updated_label.pack_forget()
    entry.pack_forget()
    enter_button.pack_forget()
    updated1_label = tk.Label(window, text="You are thinking of number " + X,bg="white", font=fnt)
    updated1_label.pack(pady=20)
    close_button = tk.Button(window, text="Close",font = ("Arial", 12), command=window.destroy)
    close_button.pack(pady=10)
window.mainloop()
