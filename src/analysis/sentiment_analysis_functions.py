#analysis.sentiment_analysis_functions.py
from src.gui.visualization import Visualization
from src.utils import utils
from src.analysis import context_analysis



def process_file(file_path, column_name, include_context=False, context_question=""):
    from src.analysis.sentiment_analysis import SentimentAnalysis
    if include_context:
        from context_analysis import creates_dataframe_with_context
        return creates_dataframe_with_context(file_path, column_name, context_question)
    else:
        sa = SentimentAnalysis()
        return sa.creates_dataframe(file_path, column_name)
    
def generate_plot(df, title="Sentiment Analysis"):
    from src.gui.visualization import Visualization
    visualization = Visualization()
    # If df2 is provided, modify here to handle the comparison case
    return visualization.plot_comparison_bar_graph(df, None, title)

