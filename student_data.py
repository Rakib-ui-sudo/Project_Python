class StudentDatabase :
    __student_list = []

    @classmethod
    def add_student(self,student_obj):
        self.__student_list.append(student_obj)

    @classmethod
    def get_student_list(self):#///
        return self.__student_list    


class Student:
    def __init__(self,student_id,name,department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = True

        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
             print("Error: Student is already enrolled!")

        else:
            self.__is_enrolled = True
            print("Student enrolled sucssfully!")

    def drop_student(self):
        if not self.__is_enrolled:
            print("Error: Student is not enrolled!")
        else:
            self.__is_enrolled = False
            print(f"Student {self.__student_id} has been dropped!") 

    def get_student_id(self):#\\\
        return self.__student_id         

    def view_student_info(self):
        # print("\n----- Student Information -----")
        print(f"Student Id: {self.__student_id}, Name: {self.__name}, Department:{self.__department}, Enrolled : {self.__is_enrolled}")                   


# =======================Main=========================
student1 = Student(101, "Rakib", "CSE")
student2 = Student(102, "Rahim", "EEE")
student3 = Student(103, "Karim", "BBA")

while True:
    print("\n===== Student Database Management =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ").strip()

    if choice == '1':
        students = StudentDatabase.get_student_list()

        if not students:
            print("No students found!")
        else:
            for student in students:
                student.view_student_info()

    elif choice == '4':
        print("Exit...")
        break

    elif choice == '2' or choice == '3':

        student_id = int(input("Enter student ID: "))

        selected_student = None

        for student in StudentDatabase.get_student_list():
            if student.get_student_id() == student_id:
               selected_student = student
               break

        if selected_student is None:
           print("Student not found!")

        elif choice == '2':
             selected_student.enroll_student()

        else:
            selected_student.drop_student()
    
    else:
        print("Invalid choice!")






