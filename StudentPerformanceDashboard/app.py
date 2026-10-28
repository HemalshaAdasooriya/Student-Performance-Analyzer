import matplotlib.pyplot as plt
import streamlit as st
import csv

st.title("Student Performance Analyzer")
st.write("My first Python dashboard!")

col1, col2 = st.columns(2)

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
    with col1:
        st.metric("Total students:", total_students)
        st.metric("Total hours studied:", total_hours_studied)
    if total_students > 0:
        average_hours_studied = total_hours_studied / total_students
    with col1:
        st.metric("Average hours studied:", f"{average_hours_studied:.4f}")

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
        with col1:
            st.metric("No data available to calculate highest and lowest hours studied.", "")
    else:
        highest_hours_studied = max(hours_list)
        lowest_hours_studied = min(hours_list)
        with col1:
            st.metric("Highest hours studied:", highest_hours_studied)
            st.metric("Lowest hours studied:", lowest_hours_studied)


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

    with col2:
        st.metric("Number of students who scored 80 or above:", students_scored_80_or_above)
    #percentage of students who scored 80 or above
    percentage_scored_80_or_above = (students_scored_80_or_above / total_students) * 100
    with col2:
        st.metric("Percentage of students who scored 80 or above:", f"{percentage_scored_80_or_above:.2f}%")

#average exam score
with open("StudentPerformanceFactors.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    score_index = header.index("Exam_Score")
    
    total_students = 0
    total_student_score = 0

    for row in reader:
        score = int(row[score_index])
        total_student_score += score
        total_students += 1
    average_score = total_student_score / total_students
    with col2:
        st.metric("Average exam score:", f"{average_score:.4f}")


#finding highest and lowest exam score values.
with open("StudentPerformanceFactors.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    score_index = header.index("Exam_Score")
    score_list = []

    for row in reader:
        score = int(row[score_index])
        score_list.append(score)

    if len(score_list) == 0:
        with col2:
            st.metric("No data available to calculate highest and lowest exam scores.", "")
    else:
        highest_exam_score = max(score_list)
        lowest_exam_score = min(score_list)
        with col2:
            st.metric("Highest exam score:", highest_exam_score)
            st.metric("Lowest exam score:", lowest_exam_score)

#bar chart for Students by Study Hours
with open("StudentPerformanceFactors.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    hours_studied_index = header.index("Hours_Studied")
    total_hours_studied = 0
    hours_count = {}

    for row in reader:
        hours_studied = int(row[hours_studied_index])

        if hours_studied in hours_count:
            hours_count[hours_studied] += 1
        else:
            hours_count[hours_studied] = 1

        total_hours_studied += hours_studied
        total_students += 1
st.subheader("Students by Hours Studied")
fig, ax = plt.subplots()
ax.bar(hours_count.keys(), hours_count.values())

ax.set_xlabel("Hours Studied")
ax.set_ylabel("Number of Students")
ax.set_title("Student by Hours Studied")

st.pyplot(fig)
plt.close(fig)