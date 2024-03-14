#gui.sentiment_gui.py

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.utils import utils



class SentimentAnalysisGUI:
    def __init__(self, master):
        self.master = master
        master.title('Sentiment Analysis Tool')

        # Choose Existing File button
        self.choose_existing_btn = tk.Button(master, text="Choose Existing File", command=self.choose_existing_file)
        self.choose_existing_btn.pack()

        # Upload New File button
        self.upload_new_btn = tk.Button(master, text="Upload New File", command=self.upload_new_file)
        self.upload_new_btn.pack()

        # Canvas for plot
        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack()

        # Display area for DataFrame
        self.text_area = tk.Text(master, height=10, width=50)
        self.text_area.pack()


    def choose_existing_file(self):
        # Update the path to the 'data_copies' directory
        data_copies_dir = os.path.join('data', 'data_copies')
        csv_files = self.list_csv_files(data_copies_dir)

        if csv_files:
            file_options = "\n".join([f"{i+1}. {file}" for i, file in enumerate(csv_files)])
            file_index = simpledialog.askinteger("Select File",
                                                 f"Select the file to analyze:\n{file_options}",
                                                 minvalue=1, maxvalue=len(csv_files))
            if file_index is not None:
                file_name = csv_files[file_index - 1]
                file_path = os.path.join(data_copies_dir, file_name)
                self.process_file(file_path)
        else:
            messagebox.showinfo("No Files Found", "No CSV files found in the 'data_copies' directory.")


    def upload_new_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.process_file(file_path)

    def list_csv_files(self, directory):
        return [f for f in os.listdir(directory) if f.endswith('.csv') and os.path.isfile(os.path.join(directory, f))]

    def process_file(self, file_path):
        # Implement the code to process the file
        from src.analysis import sentiment_analysis_functions as saf
        columns = utils.list_columns_in_csv(file_path)
        column_options = "\n".join([f"{i+1}. {col}" for i, col in enumerate(columns)])
        column_index = simpledialog.askinteger("Select Column",
                                               f"Select the column to analyze:\n{column_options}",
                                               minvalue=1, maxvalue=len(columns))
        if column_index is not None:
            column_name = columns[column_index - 1]
            df = saf.process_file(file_path, column_name)
            self.display_plot(df)

    def display_plot(self, df):
        from src.analysis import sentiment_analysis_functions as saf
        fig = saf.generate_plot(df)
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        canvas.draw()  # Refresh the canvas with the new plot

def run_gui():
    root = tk.Tk()
    gui = SentimentAnalysisGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
