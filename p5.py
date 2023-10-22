import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [28, 34, 42, 30, 25],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing']
}

employee_data = pd.DataFrame(data)

older_than_30 = employee_data[employee_data['Age'] > 30]
print(older_than_30)
#done