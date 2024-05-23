student_names = []
marks = []
has_passed = []

#Adding student names and marks
for _ in range(1): # Assuming 1 student names and marks
    name = input("enter student's name:")
    student_names.append(name)
    mark = int(input("enter student's marks:"))
    marks.append(mark)
    has_passed.append(mark >=40) # Checking if the student has passed
    
#Creating results list:
results = []
for i in range(len(student_names)):
    results.append([student_names[i], marks[i], has_passed[i]])
    
print("final results:", results)
