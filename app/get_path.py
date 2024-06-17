import os
import tkinter as tk
from tkinter import filedialog


def get_directory_path(file_paths):
    first_file_path = file_paths[0]
    for i in range(len(first_file_path) - 1, 0, -1):
        if first_file_path[i] == '/':
            directory_path = first_file_path[:i]
            break
    return directory_path


def select_input_files(run_button, text_label, file_patch):
    '''
        Диалоговое окно выбора исходных файлов
    '''
    # todo: add lambda function to reduce: global output_path, selected_files
    selected_files = filedialog.askopenfilenames(title="Выберите медиафайл", multiple=True)
    if selected_files:
        text_label.config(state='normal')
        text_label.delete(1.0, 'end')
        for file in selected_files:
            text_label.insert('end', 'Выбран путь:\n' + file + '\n')
            output_path = os.path.dirname(file)
        text_label.insert('end', '\n')
        text_label.insert('end', '\n' + 'Сохранить в: ' + '\n' + output_path + '\n')
        text_label.config(state='disabled')
        run_button.config(state='normal')

        file_patch.input_patch = selected_files[0]
        file_patch.output_patch = output_path

        # output_path = get_directory_path(selected_files)
        # text_label.config(state='normal')

        # text_label.config(state='disabled')