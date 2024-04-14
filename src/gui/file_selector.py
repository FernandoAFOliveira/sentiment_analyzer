# src/gui/main_gui.py
import tkinter as tk
from tkinter import filedialog
from src.gui.file_selector import FileSelector
from src.analysis import sentiment_analysis_functions as saf
from src.utils import utils

class ResultDisplay(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.text = tk.Text(self)
        self.text.pack(fill=tk.BOTH, expand=True)

    def update_text(self, content):
        self.text.insert(tk.END, content + "\n")
        self.text.see(tk.END)

class ControlPanel(tk.Frame):
    def __init__(self, parent, clear_callback):
        super().__init__(parent)
        self.pack()
        self.clear_button = tk.Button(self, text="Clear Results", command=clear_callback)
        self.clear_button.pack(side=tk.RIGHT)

class StatusBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.X)
        self.label = tk.Label(self, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)

class MainGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)

        self.file_selector = FileSelector(self, self.update_results)
        self.file_selector.pack(fill=tk.X)

        self.result_display = ResultDisplay(self)
        self.control_panel = ControlPanel(self, self.clear_results)
        self.status_bar = StatusBar(self.master)

    def update_results(self, df):
        self.result_display.update_text(str(df))
        self.status_bar.set_status("Analysis Complete")

    def clear_results(self):
        self.result_display.text.delete(1.0, tk.END)
        self.status_bar.set_status("Ready")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sentiment Analysis Tool")
    root.geometry("800x600")
    app = MainGUI(root)
    root.mainloop()
