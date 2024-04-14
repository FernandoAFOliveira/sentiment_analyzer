import sys
import os
import tkinter as tk
from tkinter import filedialog
from src.gui.file_selector import FileSelector
from src.gui.plot_display import PlotDisplay

# Adjust the path so imports work correctly
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, root_directory)

class ResultDisplay(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.text = tk.Text(self, height=10, width=50)
        self.text.pack(fill=tk.BOTH, expand=True)

    def update_text(self, content):
        self.text.insert(tk.END, content + "\n")

class ControlPanel(tk.Frame):
    def __init__(self, parent, analyze_callback, clear_callback):
        super().__init__(parent)
        self.analyze_button = tk.Button(self, text="Analyze", command=analyze_callback)
        self.analyze_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.clear_button = tk.Button(self, text="Clear", command=clear_callback)
        self.clear_button.pack(side=tk.LEFT)

class StatusBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)

    def set_status(self, message):
        self.label.config(text=message)

class MainGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title('Sentiment Analysis Tool')
        self.master.geometry("800x600")

        self.file_frame = tk.Frame(master)
        self.plot_frame = tk.Frame(master)
        self.result_frame = tk.Frame(master)
        self.control_frame = tk.Frame(master)
        self.status_frame = tk.Frame(master)

        self.file_frame.grid(row=0, column=0, sticky="nsew")
        self.plot_frame.grid(row=1, column=0, sticky="nsew")
        self.result_frame.grid(row=2, column=0, sticky="nsew")
        self.control_frame.grid(row=3, column=0, sticky="nsew")
        self.status_frame.grid(row=4, column=0, sticky="nsew")

        self.file_selector = FileSelector(self.file_frame, self.update_plot)
        self.plot_display = PlotDisplay(self.plot_frame)
        self.result_display = ResultDisplay(self.result_frame)
        self.control_panel = ControlPanel(self.control_frame, self.start_analysis, self.clear_results)
        self.status_bar = StatusBar(self.status_frame)

    def update_plot(self, df):
        self.plot_display.update_plot(df)
        self.result_display.update_text(str(df))
        self.status_bar.set_status("Plot Updated")

    def start_analysis(self):
        # Logic for starting the analysis
        pass

    def clear_results(self):
        self.result_display.text.delete(1.0, tk.END)
        self.status_bar.set_status("Ready")

def run_gui():
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()