from data_science_template.common_functions import data_cleaning, statistical_analysis

def conduct_analysis():
    # Load data from example_data/raw_data.csv
    raw_data = ...
    cleaned_data = data_cleaning.clean_data(raw_data)
    analysis_results = statistical_analysis.perform_analysis(cleaned_data)
    # Conduct specific analysis based on user input
    # ...

if __name__ == '__main__':
    conduct_analysis()
