#analysis.sentiment_analysis.py

import csv
import nltk
import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from datetime import datetime
from src.gui.visualization import Visualization


class SentimentAnalysis:
    def __init__(self):
        """Initializes the SentimentIntensityAnalyzer and any other necessary components."""
        self.sia = SIA()

    def copy_csv_to_local(self, file_path, subdirectory='data_copies'):
        """
        Copies the specified CSV file to a local subdirectory.

        Args:
            file_path (str): The path to the original CSV file.
            subdirectory (str): The subdirectory to store the copied file.

        Returns:
         str: The path to the copied file.
        """
        if not os.path.exists(subdirectory):
         os.makedirs(subdirectory)

        # Extract the file name from the path
        file_name = os.path.basename(file_path)
        local_copy_path = os.path.join(subdirectory, file_name)

        # Copy the file if source and destination are different
        if file_path != local_copy_path:
            shutil.copy(file_path, local_copy_path)

        return local_copy_path

    
    def creates_dataframe(self, file, column_name):
        """
        First copies the CSV file to a local directory, then creates a dataframe...
        Creates a dataframe from a specified column in a CSV file and performs sentiment analysis on the textual data.
        Args:
            file (str): The path to the CSV file.
            column_name (str): The name of the column to analyze.
        Returns:
            DataFrame: A pandas DataFrame containing the original text and its sentiment scores.
        """
        # Copy the CSV file to the local subdirectory
        local_file_path = self.copy_csv_to_local(file)        
        lst = []
        with open(file, encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile)
            for element in reader:
                lst.append(element[column_name])

        results = []
        for x in lst:
            pol_score = self.sia.polarity_scores(x)
            pol_score['text'] = x
            results.append(pol_score)

        df = pd.DataFrame.from_records(results)
        df['label'] = 0
        df.loc[df['compound'] > 0.2, 'label'] = 1
        df.loc[df['compound'] < -0.2, 'label'] = -1
        return df

    def bar_graph(self, df, title):
        """
        Creates a bar graph showing the distribution of sentiments (positive, negative, neutral) in the data.
        Additionally, displays the value on top of each bar and includes a legend with total counts.
    
        Args:
        df (DataFrame): The pandas DataFrame containing sentiment labels.
            title (str): The title of the graph.
    
        Returns:
            None: Displays the bar graph.
        """
        fig, ax = plt.subplots(figsize=(8, 8))

        # Calculate counts and percentages
        counts = df.label.value_counts()
        percentages = df.label.value_counts(normalize=True) * 100

        bars = sns.barplot(x=percentages.index, y=percentages, ax=ax, color='red').set(title=title)
        sns.set_style('whitegrid')

        # Add labels to each bar
        for bar in ax.patches:
            ax.annotate(f"{format(bar.get_height(), '.2f')}%",  
                   (bar.get_x() + bar.get_width() / 2, 
                    bar.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 8),
                   textcoords='offset points')

        ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
        ax.set_ylabel("Percentage")

        # Create a legend for the total counts
        total_counts = [f"Negative: {counts[-1]}", f"Neutral: {counts[0]}", f"Positive: {counts[1]}"]
        plt.legend(total_counts, loc='upper left')

        plt.show()


    def counts(self, df, column):
        """
        Counts the occurrences of each sentiment label in a DataFrame.
        Args:
            df (DataFrame): The pandas DataFrame to analyze.
            column (str): The column name containing sentiment labels.
        Returns:
            Series: A pandas Series with the counts of each label.
        """
        return df[column].value_counts()

    def percentage(self, df, column):
        """
        Calculates the percentage of each sentiment label in a DataFrame.
        Args:
            df (DataFrame): The pandas DataFrame to analyze.
            column (str): The column name containing sentiment labels.
        Returns:
            Series: A pandas Series with the percentage of each label.
        """
        return df[column].value_counts(normalize=True) * 100

    def print_top_comments(self, df, column, conotation, number):
        """
        Prints the top comments for a given sentiment label.
        Args:
            df (DataFrame): The pandas DataFrame containing the comments and their labels.
            column (str): The column name containing sentiment labels.
            conotation (int): The sentiment label to filter by (-1, 0, 1).
            number (int): The number of top comments to print.
        Returns:
            None: Prints the top comments.
        """
        filtered_df = df[df[column] == conotation].head(number)
        for comment in filtered_df['text']:
            print('-' + comment)

    def save_top_comments_to_file(self, df, column, conotation, number, default_dir='saved_comments'):
        """
        Saves the top comments for a given sentiment label to a file.
        The file is saved in a default directory with a timestamp in its name.
        Args:
            df (DataFrame): The pandas DataFrame containing the comments and their labels.
            column (str): The column name containing sentiment labels.
            conotation (int): The sentiment label to filter by (-1, 0, 1).
            number (int): The number of top comments to save.
            default_dir (str): The default directory to save the file.
        """
        # Create the default directory if it doesn't exist
        if not os.path.exists(default_dir):
            os.makedirs(default_dir)

        # Generate a unique filename with a timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f"top_comments_{conotation}_{timestamp}.txt"
        file_path = os.path.join(default_dir, file_name)

        with open(file_path, 'a') as file:
            filtered_df = df[df[column] == conotation].head(number)
            for comment in filtered_df['text']:
                file.write('-' + comment + '\n')

        print(f"Top comments saved to {file_path}")


    def download_nltk_data(self, data_directory='nltk_data'):
        """
        Downloads required NLTK data if not already present.

        Args:
        data_directory (str): The directory to store NLTK data.

        Returns:
        None: Downloads data and prints status.
        """
        # Create the directory if it doesn't exist
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)

        # Set NLTK data path
        nltk.data.path.append(data_directory)

        # Download the VADER lexicon
        nltk.download('vader_lexicon', download_dir=data_directory)
        print("NLTK data downloaded in '{}'".format(data_directory))
        
    def process_file(file_path, column_name, include_context=False, context_question=""):
        from context_analysis import creates_dataframe_with_context
        sa = SentimentAnalysis()
        if include_context:
            return creates_dataframe_with_context(file_path, column_name, context_question)
        else:
            return sa.creates_dataframe(file_path, column_name)

    def generate_plot(df1, df2=None, title="Sentiment Analysis"):
        visualization = Visualization()
        if df2 is not None:
            return visualization.plot_comparison_bar_graph(df1, df2, title)
        else:
            return visualization.bar_graph(df1, title)