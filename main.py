from module_A import get_subjects, get_scores
from module_B import draw_distribution_graph
import sys
sys.stdout.reconfigure(encoding='utf-8')


year_files = {
    "2020": '20201231.csv',
    "2021": '20211231.csv',
    "2022": '20221231.csv',
    "2023": '20231231.csv'
}

# Prompt user to select a year
year_choice = input(f"연도 선택({', '.join(year_files.keys())}) : ")
if year_choice not in year_files:
    print("잘못된 연도를 선택했습니다!")
    sys.exit()

file_path = year_files[year_choice]

subjects = get_subjects(file_path)
print("연도 선택:")
for i, subject in enumerate(subjects):
    print(f"{i + 1}. {subject}")

choice = int(input("과목 번호를 선택하세요 : ")) - 1
if choice < 0 or choice >= len(subjects):
    print("잘못된 과목을 선택했습니다!")
else:
    selected_subject = subjects[choice]
    scores, male_count, female_count = get_scores(file_path, selected_subject)
    draw_distribution_graph(scores, male_count, female_count, selected_subject)
