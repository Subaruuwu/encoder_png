import tkinter as tk
from tkinter import ttk, Text
from ttkbootstrap import Style


def make_label(window, text, row, column, x, y):
    label = ttk.Label(window, text=text)
    label.grid(row=row, column=column, padx=x, pady=y)
    return label


def make_output_text(window, row, column, x, y, width=40, height=10, text=None):
    output_text = tk.Text(window, wrap=tk.WORD, width=width, height=height)
    output_text.grid(row=row, column=column, padx=x, pady=y)
    if text:
        output_text.config(text=text)
    return output_text


def make_text_label(width, row, column, height, state='normal'):
    txt = Text(width=width, background="#555", foreground="#ccc", height=height, state=state)
    txt.grid(row=row, column=column)
    # txt.place(y=150 + wqs, x=10)
    return txt


def config_text(text_label, new_text):
    text_label.config(text=new_text)
    text_label.update_idletasks()