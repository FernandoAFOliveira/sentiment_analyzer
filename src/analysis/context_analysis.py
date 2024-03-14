#analysis.context_analysis.py

import csv
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

def creates_dataframe_with_context(file, column_name, question):
    lst = []
    sia = SIA()
    
    with open(file, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for element in reader:
            lst.append(element[column_name])

    results = []
    for text in lst:
        text_with_question = question + ' ' + text
        pol_score = sia.polarity_scores(text_with_question)
        pol_score['text'] = text_with_question
        results.append(pol_score)
    
    df = pd.DataFrame.from_records(results)
    df['label'] = 0
    df.loc[df['compound'] > 0.2, 'label'] = 1
    df.loc[df['compound'] < -0.2, 'label'] = -1
    return df
