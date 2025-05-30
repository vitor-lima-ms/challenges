N_STUDENTS_RECORD = int(input())
students_record = dict()

for i in range(N_STUDENTS_RECORD):
    student_data = input()
    student_data_list = student_data.split(' ')
    student_notes = list()
    for i in range(1, 4):
        student_notes.append(float(student_data_list[i]))
    students_record[student_data_list[0]] = student_notes

student = input()

notes_list = list()
for key, value in students_record.items():
    if key == student:
        for note in value:
            notes_list.append(note)

notes_sum = 0
for note in notes_list:
    notes_sum += note

student_mean = notes_sum / len(notes_list)

print(f'{student_mean:.2f}')