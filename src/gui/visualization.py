#gui.visualization.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from src.utils import utils


class Visualization:
    def plot_comparison_bar_graph(self, df1, df2, title):
        fig, ax = plt.subplots()

        # Prepare data for df1
        df1_counts = df1['label'].value_counts().reindex([-1, 0, 1], fill_value=0)
        df1_percentages = (df1_counts / df1_counts.sum()) * 100

        if df2 is not None:
            # Prepare data for df2 if it exists
            df2_counts = df2['label'].value_counts().reindex([-1, 0, 1], fill_value=0)
            df2_percentages = (df2_counts / df2_counts.sum()) * 100
            bar_width = 0.35
            index = np.arange(3)  # For the three categories: -1, 0, 1

            # Plot bars for both dataframes
            plt.bar(index - bar_width/2, df1_percentages, bar_width, alpha=0.8, color='r', label='No Context')
            plt.bar(index + bar_width/2, df2_percentages, bar_width, alpha=0.8, color='b', label='With Context')
        else:
            # Plot bars for df1 only
            plt.bar(df1_percentages.index, df1_percentages, alpha=0.8, color='r', label='No Context')

        # Add labels and title
        ax.set_xlabel('Sentiment')
        ax.set_ylabel('Percentage')
        ax.set_title(title)
        ax.set_xticks(range(-1, 2))  # For -1, 0, 1 labels
        ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
        plt.legend()
        plt.tight_layout()
        return fig
