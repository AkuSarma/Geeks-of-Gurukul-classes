num_students = int(input("Enter the number of students: "))

students = []

for i in range(num_students):
    name, marks = input("Enter student's name and marks: ").split()
    students.append((name, int(marks)))

for i in range(num_students - 1):
    for j in range(num_students - i - 1):
        if students[j][1] < students[j + 1][1]:
            students[j], students[j + 1] = students[j + 1], students[j]

ranked_students = []
rank = 1
for i, (name, marks) in enumerate(students):
    if i > 0 and marks == students[i - 1][1]:
        ranked_students.append((rank, name))
    else:
        rank = i + 1
        ranked_students.append((rank, name))

for r, name in ranked_students:
    print(f"{r}. {name}")
