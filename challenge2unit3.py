def sort_students(student_list):
  sorted_students= sorted(student_list,key=lambda student:student[2],reverse=True)
  return sorted_students
students = [("sandy","A123",'7.8'), ("san","A124", '8.9'), ("virat", "A125",'9.9'),("desr", "A127", "8.9")]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name : {},Rollnumber : {},cgpa : {}".format(student[0],student[1],student[2]))