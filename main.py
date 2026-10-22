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
         total_hours_studied += hours_studied
         total_students += 1
    print(f"Total students: {total_students}")
    print(f"Total hours studied: {total_hours_studied}")
    if total_students > 0:
        average_hours_studied = total_hours_studied / total_students
    print(f"Average hours studied: {average_hours_studied}")

    #finding highest and lowest Hours_Studied values.
