import pandas as pd
import time

students_file_path = "students.csv"
fees_file_path = "student_fees.csv"

start_time = time.time()

students_data = pd.read_csv(students_file_path)
fees_data = pd.read_csv(fees_file_path)

fees_data['Day'] = fees_data['Payment Date'].str.extract(r'(\d+)$').astype(int)

# Determine the most consistent payment day for each student
consistent_days = fees_data.groupby('Student ID')['Day'].apply(lambda days: days.mode()[0]).reset_index()
consistent_days.columns = ['Student ID', 'Most Consistent Payment Day']

# Combine student details with consistent payment day information
result_data = students_data.merge(consistent_days, on='Student ID', how='inner')

execution_time = time.time() - start_time

print(f"Execution Time: {execution_time:.4f} seconds")
print(result_data)
