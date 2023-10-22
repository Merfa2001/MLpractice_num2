import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [95, 84, 72, 60, 88]
}

student_data = pd.DataFrame(data)

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'D'

student_data['Grade'] = student_data['Score'].apply(assign_grade)

print(student_data)
#done