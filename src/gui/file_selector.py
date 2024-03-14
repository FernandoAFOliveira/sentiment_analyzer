import tkinter as tk
from tkinter import filedialog, simpledialog
from src.utils import utils
from src.analysis import sentiment_analysis_functions as saf

class FileSelector:
    def __init__(self, master, update_plot_callback):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.choose_btn = tk.Button(self.frame, text="Choose File", command=self.choose_file)
        self.choose_btn.pack(side=tk.LEFT)

        self.update_plot_callback = update_plot_callback

    def choose_file(self):
        # Logic for choosing file and column
        # Call self.update_plot_callback with the processed dataframe
        pass
