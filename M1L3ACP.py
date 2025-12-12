#Assignment: Exam Eligibility

total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter number of classes attended: "))

# Calculating attendance percentage
attendance_percentage = (attended_classes / total_classes) * 100

print(f"\nAttendance Percentage: {attendance_percentage:.2f}%")

# Checking eligibility
if attendance_percentage >= 75:
    print("You are eligible to write the exam.")
else:
    print("You are NOT eligible to write the exam.")
