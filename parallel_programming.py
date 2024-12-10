import pandas as pd
import multiprocessing as mp
import time


def compute_payment_days(chunk):
    grouped_data = chunk.groupby('Student ID')['Day']
    return grouped_data.apply(lambda days: days.mode()[0]).reset_index()

def main():
    
    students_file_path = "students.csv"
    fees_file_path = "student_fees.csv"

    
    students_data = pd.read_csv(students_file_path)
    fees_data = pd.read_csv(fees_file_path)

    
    fees_data['Day'] = fees_data['Payment Date'].str.extract(r'(\d+)$').astype(int)

    
    start_time = time.time()

    # Divide the fees dataset into smaller chunks
    num_chunks = mp.cpu_count()  # Use the number of CPU cores for parallelism
    chunk_size = len(fees_data) // num_chunks
    data_chunks = [fees_data.iloc[i:i + chunk_size] for i in range(0, len(fees_data), chunk_size)]

    # Parallel processing using a multiprocessing pool
    with mp.Pool(num_chunks) as pool:
        processed_results = pool.map(compute_payment_days, data_chunks)

    # Combine all results and remove duplicate entries
    consistent_days = pd.concat(processed_results).drop_duplicates(subset='Student ID')

    # Merge the consistent payment days data with student details
    final_result = students_data.merge(consistent_days, on='Student ID', how='inner')

    
    execution_time = time.time() - start_time

    
    print(f"Execution Time: {execution_time:.4f} seconds")
    print(final_result)

if __name__ == "__main__":
    main()
