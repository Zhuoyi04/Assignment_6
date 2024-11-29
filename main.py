from module_A import get_subjects
import sys
sys.stdout.reconfigure(encoding='utf-8')


file_path = '20231231.csv'

subjects = get_subjects(file_path)
print("Available subjects:")
for i, subject in enumerate(subjects):
    print(f"{i + 1}. {subject}")

choice = int(input("Select a subject by number: ")) - 1
if choice < 0 or choice >= len(subjects):
    print("Invalid choice!")
