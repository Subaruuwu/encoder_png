import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


def make_window(title):
    window = tk.Tk()
    window.title(title)

    style = Style(theme="darkly")
    style.configure('.', font=('Roboto', 12))
    style.configure('Tlabel', font=('Roboto', 12))
    return window


