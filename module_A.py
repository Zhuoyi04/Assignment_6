import pandas as pd

def get_subjects(file_path):
    data = pd.read_csv(file_path,encoding='euc-kr')
    subjects = data['유형'].unique().tolist()  # Extract unique subject names
    return subjects

def get_scores(file_path, selected_subject):
    data = pd.read_csv(file_path, encoding='euc-kr')
    filtered_data = data[data["유형"] == selected_subject]

    scores = filtered_data['표준점수'].dropna().tolist()
    male_count = filtered_data['남자'].dropna().tolist()  # Exclude NaN values
    female_count = filtered_data['여자'].dropna().tolist()  # Exclude NaN values
    return scores, male_count, female_count
