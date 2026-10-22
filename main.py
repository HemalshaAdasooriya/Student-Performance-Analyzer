import csv

# with open("StudentPerformanceFactors.csv", "r", newline="") as file:
#     reader = csv.reader(file)
#     header = next(reader)  # Read the header row
#     print(header)  # Print the header row
    
#     # total_students = 0
#     # for row in reader:
#     #     total_students += 1  # Count each data row
#     # print(f"Total number of students: {total_students}")

#     print("Dataset columns:")
#     for column in header:
#             print(column)

#     print() #start new line  

#     hours_studied_index = header.index("Hours_Studied")
#     print(f"Index of Hours_Studied: {hours_studied_index}") 

#     print("Study hours of first 5 students:")
#     for i in range(5):
#         row = next(reader)
#         hours_studied = int(row[hours_studied_index])
#         hours_studied_type = type(hours_studied)
#         print(hours_studied, hours_studied_type)  # Print the Hours_Studied value for each of the first 5 students

with open("StudentPerformanceFactors.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    hours_studied_index = header.index("Hours_Studied")
    
    total_hours_studied = 0
    total_students = 0

    #finding Average of hours studied
    for row in reader:
         hours_studied = int(row[hours_studied_index])
         max_hours_studied = max(hours_studied, total_hours_studied)
         total_hours_studied += hours_studied
         total_students += 1
    print(f"Total students: {total_students}")
    print(f"Total hours studied: {total_hours_studied}")
    if total_students > 0:
        average_hours_studied = total_hours_studied / total_students
    print(f"Average hours studied: {average_hours_studied}")


#finding highest and lowest Hours_Studied values.
with open("StudentPerformanceFactors.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    hours_studied_index = header.index("Hours_Studied")
    hours_list = []

    for row in reader:
        hours_studied = int(row[hours_studied_index])
        hours_list.append(hours_studied)

    if len(hours_list) == 0:
        print("No data available to calculate highest and lowest hours studied.")
    else:
        highest_hours_studied = max(hours_list)
        lowest_hours_studied = min(hours_list)
        print(f"Highest hours studied: {highest_hours_studied}")
        print(f"Lowest hours studied: {lowest_hours_studied}")
        
    
#Number of students who scored 80 or above.
with open("StudentPerformanceFactors.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    score_index = header.index("Exam_Score")
    
    students_scored_80_or_above = 0

    for row in reader:
        score = int(row[score_index])
        if score >= 80:
            students_scored_80_or_above += 1

    print(f"Number of students who scored 80 or above: {students_scored_80_or_above}")