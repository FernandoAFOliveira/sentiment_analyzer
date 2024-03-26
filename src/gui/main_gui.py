#src.gui.MainGUI

import tkinter as tk
from src.gui.file_selector import FileSelector
from src.gui.plot_display import PlotDisplay

class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title('Sentiment Analysis Tool')

        # Set initial size of the window
        master.geometry("800x600")  # Width x Height

        # File selector module
        self.file_selector = FileSelector(master, self.update_plot)
        self.file_selector.grid(row=0, column=0, sticky="nsew")

        # Plot display module
        self.plot_display = PlotDisplay(master)
        self.plot_display.grid(row=1, column=0, sticky="nsew")

        # Set grid weights for responsiveness
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=3)  # Adjust the weight to allocate more space to the plot

    def update_plot(self, df):
        # Update plot based on the new dataframe
        self.plot_display.update_plot(df)

def run_gui():
    root = tk.Tk()
    gui = MainGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
