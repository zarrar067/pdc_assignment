Name : Zarrar Ahmad       Roll No : 20B-067-CS

PDC Assignment: Parallel and Serial Programming
This project showcases both serial and parallel programming techniques for efficiently processing and analyzing student fee data.

Overview
The project demonstrates:

Serial Programming:

A simple, step-by-step method to process data one at a time.
Calculates the most consistent payment day for each student based on their fee records.
Parallel Programming:

Uses Python's multiprocessing library to improve performance.
Splits the data into smaller chunks and processes them simultaneously, speeding up the calculation of consistent payment days.
Files
serial_programming.py:

Implements the serial approach for analyzing student fee payment consistency.
parallel_programming.py:

Implements the parallel approach using multiprocessing to handle larger datasets more efficiently.
students.csv:

Contains student details, such as IDs and other related information.
student_fees.csv:

Contains records of students' fee payments, including payment dates.
Technologies Used
Python
Pandas library
Multiprocessing library
Key Features
Calculates the most consistent payment day for each student efficiently.
Highlights the difference between serial and parallel processing approaches.
Usage
Make sure the required files (students.csv and student_fees.csv) are in the project directory.
Run either serial_programming.py or parallel_programming.py to analyze the data.
