# Grades are computed using a weighted average. Suppose that the written test counts 70%,  lab exams 20% and assignments 10%.
# Program should accept the scores for written test, lab exams and assignments
# Output the grade of a student (using weighted average)

written_test=float(input("Enter Written test marks: "))
lab_exams=float(input("Enter Lab exams marks: "))
assignments=float(input("Enter Assignments marks: "))

grade=(written_test*70)/100 + (lab_exams*20)/100 + (assignments*10)/100
print("overall grade: ",grade)