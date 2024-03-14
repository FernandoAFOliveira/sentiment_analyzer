#src.gui.MainGUI

import tkinter as tk
from src.gui.file_selector import FileSelector
from src.gui.plot_display import PlotDisplay

class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title('Sentiment Analysis Tool')

        # File selector module
        self.file_selector = FileSelector(master, self.update_plot)

        # Plot display module
        self.plot_display = PlotDisplay(master)
        self.plot_display.initialize_default_plot()

    def update_plot(self, df):
        # Update plot based on the new dataframe
        self.plot_display.update_plot(df)

def run_gui():
    root = tk.Tk()
    gui = MainGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
