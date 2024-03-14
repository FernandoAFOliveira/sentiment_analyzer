#src.gui.PlotDisplay

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class PlotDisplay:
    def __init__(self, master):
        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack()

    def initialize_default_plot(self):
        # Create and display default plot
        pass

    def update_plot(self, df):
        # Update plot based on new data
        pass
