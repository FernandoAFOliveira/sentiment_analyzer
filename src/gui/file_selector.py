# src.gui.file_selector.py

import tkinter as tk
from tkinter import filedialog, simpledialog
from src.utils import utils
from src.analysis import sentiment_analysis_functions as saf

class FileSelector(tk.Frame):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback
        # Add button to choose file
        self.choose_btn = tk.Button(self, text="Choose File", command=self.choose_file)
        self.choose_btn.pack()

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.create_column_selection_options(file_path)

    def create_column_selection_options(self, file_path):
        columns = utils.list_columns_in_csv(file_path)
        self.selection_frame = tk.Frame(self)
        self.selection_frame.pack()

        label = tk.Label(self.selection_frame, text="Choose a column:")
        label.pack()

        for i, col in enumerate(columns, start=1):
            button = tk.Button(self.selection_frame, text=f"{col}", 
                               command=lambda c=col: self.process_file_selection(file_path, c))
            button.pack()

    def process_file_selection(self, file_path, column_name):
        self.selection_frame.destroy()  # Remove the selection frame
        df = saf.process_file(file_path, column_name)
        self.callback(df)  # Use callback to update the plot
