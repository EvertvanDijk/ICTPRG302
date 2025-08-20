"""
(c) 2025 Evert van Dijk
This code creates directories for each student listed in C3Students.txt
and subdirectories for their respective courses.
It uses the current working directory to create the student folders.
It uses nested loops to create subdirectories for each course.

The directories are structured as follows:
- Current Working Directory
    - Student Name (Eg John Smith as Smith, John)
        - Course Subdirectory 1 (eg ICTPRG302)
    
The purpose is so I can easily manage student files and 
their submissions for future audits.        
the data is stored in courses.txt and Students.txt files.
Alternatively these can be stored in .cvs files.
"""
import os

# Read course IDs from the text file where *file* is the object that holds "/path/to/courses.txt"
with open("courses.txt", "r", encoding="utf-8") as file:
    subdirs = [line.strip() for line in file if line.strip()] # reads each line and adds to the array students[]

# Read students from the text file where *file* is the object that holds "/path/to/Students.txt"
with open("Students.txt", "r", encoding="utf-8") as file:
    students = [line.strip() for line in file if line.strip()]

# Create directories using nested loops.
# First Loop: for each student
for student in students: #student is the variable in this loop, students is the array created on line 22 
    student_path = os.path.join(os.getcwd(), student)
    os.makedirs(student_path, exist_ok=True)
    
    # Second Loop: for each course subdirectory
    for subdir in subdirs:
        subdir_path = os.path.join(student_path, subdir)
        os.makedirs(subdir_path, exist_ok=True)

print("All directories created successfully!")      # Confirmation message, this will run whether it is successful or not.
input("Press Enter to continue...")                 # superflous but useful for debugging.
