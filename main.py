class Student:
    namelist = []
    all_grades = {}
    courses = []
    counter = 0
  
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses.append(self.finished_courses)
        self.courses_in_progress = []
        self.courses.append(self.courses_in_progress)
        self.grades = {}
        self.namelist.append(self.name)
        Student.counter += 1
  
    def __str__(self):
      total = 0
      for key in self.grades:
       total += sum(self.grades[key])/len(self.grades[key])/len(self.grades)
      return 'Student:\nName:' + str(self.name) + '\nNachname:' + str(self.surname) + '\nDurchschnittsnote HA:' + str(total) + '\nLaufende Kurse:' + str(self.courses_in_progress) + '\nAbgeschlossene Kurse:' + str(self.finished_courses) + '\n'
# студенты оценивают лекторов

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                if course in Lecturer.all_grades:
                  Lecturer.all_grades[course] += [grade]
                else:
                  Lecturer.all_grades[course] = [grade]
            else:
                lecturer.grades[course] = [grade]
                if course in Lecturer.all_grades:
                  Lecturer.all_grades[course] += [grade]
                else:
                  Lecturer.all_grades[course] = [grade]
        else:
            'Ошибка'
          
    def compare(self, other):
        if isinstance(other, Student): 
          totalself = 0
          for key in self.grades:
            totalself += sum(self.grades[key])/len(self.grades[key])/len(self.grades)
          totalother = 0
          for key in other.grades:
            totalother += sum(other.grades[key])/len(other.grades[key])/len(other.grades)
          if totalself < totalother:
            return str(other.name) + ' '+ str(other.surname) + ' ist besser mit ' + str(totalother)
          if totalself > totalother:
            return str(self.name) + ' '+ str(self.surname) + ' ist besser mit ' + str(totalself)

    def compare_all(course):
      totalall = {}
      totalall = sum(Student.all_grades[course])/len(Student.all_grades[course])
      return 'Durschnittsnote für ' + course + ': ' + str(totalall)
              
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    all_grades = {}
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
      total = 0
      for key in self.grades:
       total += sum(self.grades[key])/len(self.grades[key])/len(self.grades)
      return 'Lecturer:\nName:' + str(self.name) + '\nNachname:' + str(self.surname) + '\nDurchschnittsnote Lesung:' + str(total) + '\n'

    def compare(self, other):
        if isinstance(other, Lecturer): 
          totalself = 0
          for key in self.grades:
            totalself += sum(self.grades[key])/len(self.grades[key])/len(self.grades)
          totalother = 0
          for key in other.grades:
            totalother += sum(other.grades[key])/len(other.grades[key])/len(other.grades)
          if totalself < totalother:
            return str(other.name) + ' '+ str(other.surname) + ' ist besser mit ' + str(totalother)
          if totalself > totalother:
            return str(self.name) + ' '+ str(self.surname) + ' ist besser mit ' + str(totalself)
            
    def compare_all(course):
      totalall = {}
      totalall = sum(Lecturer.all_grades[course])/len(Lecturer.all_grades[course])
      return 'Durschnittsnote für ' + course + ': ' + str(totalall)

# преподы оценивают студентов
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                if course in Student.all_grades:
                  Student.all_grades[course] += [grade]
                else:
                  Student.all_grades[course] = [grade]
            else:
                student.grades[course] = [grade]
                if course in Student.all_grades:
                  Student.all_grades[course] += [grade]
                else:
                  Student.all_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Reviewer:\nName:' + str(self.name) + '\nNachname:' + str(self.surname) + '\n'


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

great_student = Student('Santa', 'Claus', 'male')
great_student.courses_in_progress += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

some_mentor = Reviewer('Ralph', 'Hardy')
some_mentor.courses_attached += ['Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
some_mentor.rate_hw(great_student, 'Git', 8)
some_mentor.rate_hw(best_student, 'Git', 5)

best_lecturer = Lecturer('Alfred', 'Lasarus')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['C++']

dude_lecturer = Lecturer('Ronald', 'Weasley')
dude_lecturer.courses_attached += ['C++']

student_reviewer = Student('Mark', 'Muffin', 'male')
student_reviewer.courses_in_progress += ['Python']
student_reviewer.courses_in_progress += ['C++']
student_reviewer.rate(best_lecturer, 'Python', 10)
student_reviewer.rate(best_lecturer, 'C++', 8)

buddy_student = Student('Ralph', 'Holmes', 'male')
buddy_student.courses_in_progress += ['C++']
buddy_student.rate(dude_lecturer, 'C++', 10)

print(cool_mentor)
print(best_lecturer)
print(best_student)

print(best_student.compare(great_student))
print(best_lecturer.compare(dude_lecturer))

print(Student.compare_all('Python'))
print(Lecturer.compare_all('C++'))


