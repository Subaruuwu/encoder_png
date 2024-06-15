import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


def make_button(window, text, command, row, column, x, y, state='normal'):
    button = ttk.Button(window, text=text, command=command, state=state)
    button.grid(row=row, column=column, padx=x, pady=y)
    return button


def make_combobox(dict_of_tasks: dict, window: tk, row: int, column: int, x: int, y: int):
    combobox = ttk.Combobox(window, values=[task for task in dict_of_tasks.values()])
    combobox.grid(row=row, column=column, padx=x, pady=y)
    combobox.bind("<<ComboboxSelected>>")  # , lambda event: on_combobox_select(event, combobox, description_label)
    return combobox


# def on_combobox_select(event):
#     selected_item = combobox.get()
#     description_label.config(text=f"Выбран вариант: {dict_of_description[selected_item]}")
#     #Добавить появление примера в поле для вывода с помощью словаря и атрибут input_data