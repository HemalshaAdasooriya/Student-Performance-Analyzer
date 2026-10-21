import csv

with open("StudentPerformanceFactors.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    print(header)  # Print the header row
    total_students = 0

    for row in reader:
        total_students += 1  # Count each data row

print(f"Total number of students: {total_students}")