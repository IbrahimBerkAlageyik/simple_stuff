class Student:

    student_number = 0

    # initilizes the Student class object. student_number attr is automatically incremented with each object created.
    def __init__(self, first_name, last_name, date_of_birth, sex, country_of_birth):
        Student.student_number += 1
        self._id = Student.student_number
        self.first_name = first_name
        self._last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.country_of_birth = country_of_birth
    
    # getter or student number since its a private attr
    def get_student_number(self):
        return self._id
    #setter for stu num
    def set_student_number(self, student_number):
        self._id = student_number
    # getter for last name
    def get_last_name(self):
        return self._last_name
    # setter for last name
    def set_last_name(self, newlast_name):
        self._last_name = newlast_name

# class for an array that wil contain objects of the student class
class StudentContainer:

    # create the list
    def __init__(self):
        self.students = []

    # adds student to the list attr of this class' object and checks if it has less than 100
         # limiting the number to 100
    def add_student(self, student):
        if len(self.students) < 100:
            self.students.append(student)
            print(f"Student {student.first_name} {student.get_last_name()} added successfully.")
        else:
            print("Cannot add more students. Container is full.")

    # finds a student by its stu num inside the list
    def find_student_by_number(self, student_number):
        for student in self.students:
            if str(student.get_student_number()) == student_number:
                return student
        return None
        
    # gets the stu num finds the student prints out the info of the student
    def print_student_info(self, student_number):
        student = self.find_student_by_number(student_number)
        if student:
            print(f"Student Information for Student Number {student_number}:")
            print(f"First Name: {student.first_name}")
            print(f"Last Name: {student.get_last_name()}")
            print(f"Date of Birth: {student.date_of_birth}")
            print(f"Sex: {student.sex}")
            print(f"Country of Birth: {student.country_of_birth}")
        else:
            print(f"Student with Student Number {student_number} not found in the database.")

    # prints out all the info about every student inside the list
    def print_all_students_info(self):
        if not self.students:
            print("No students in the database.")
        else:
            print("Student Information for all Students in the Database:")
            for student in self.students:
                print(f"Student Number: {student.get_student_number()}")
                print(f"First Name: {student.first_name}")
                print(f"Last Name: {student.get_last_name()}")
                print(f"Date of Birth: {student.date_of_birth}")
                print(f"Sex: {student.sex}")
                print(f"Country of Birth: {student.country_of_birth}")
                print("---")

    # prints all the student with the specified birthday
    def print_students_by_birth_year(self, birth_year):
        found_students = False
        print(f"Student Information for Students Born in {birth_year}:")
        for student in self.students:
            if student.date_of_birth.startswith(birth_year):
                found_students = True
                print(f"Student Number: {student.get_student_number()}")
                print(f"First Name: {student.first_name}")
                print(f"Last Name: {student.get_last_name()}")
                print(f"Date of Birth: {student.date_of_birth}")
                print(f"Sex: {student.sex}")
                print(f"Country of Birth: {student.country_of_birth}")
                print("---")

        if not found_students:
            print(f"No students found in the database born in {birth_year}.")
    
    # finds student by its num and deletes it from the list
    def delete_student_by_number(self, student_number):
        student = self.find_student_by_number(student_number)
        if student:
            self.students.remove(student)
            print(f"Student with Student Number {student_number} deleted from the database.")
        else:
            print(f"Student with Student Number {student_number} not found in the database.")

    # clear out the list deleting all the info
    def clear_all(self):
        self.students.clear()

    # finds the student by its num and modifies a specific attr of the student
    def modify_student_record(self, student_number):
        student = self.find_student_by_number(student_number)
        if student:
            print(f"Modifying information for Student Number {student_number}:")
            print("1. First Name")
            print("2. Last Name")
            print("3. Date of Birth")
            print("4. Sex")
            print("5. Country of Birth")

            field_choice = input("Enter the number of the field to modify (1-5): ")
            
            if field_choice in {'1', '2', '3', '4', '5'}:
                field_index = int(field_choice) - 1
                fancy_field_names = ["First Name", "Last Name", "Date of Birth", "Sex", "Country of Birth"]
                field_names = ['first_name', 'get_last_name' 'date_of_birth', 'sex', 'country_of_birth']
                field_name = field_names[field_index]
                new_value = input(f"Enter the new value for {fancy_field_names[field_index]}: ")
                
                if field_choice == 2:
                    student.set_last_name(new_value)
                else:
                    setattr(student, field_name, new_value)

                print(f"Record updated successfully for {fancy_field_names[field_index]}.")
            else:
                print("Invalid field choice. No modifications made.")
        else:
            print(f"Student with Student Number {student_number} not found in the database.")



# opens text file and writes the student info of the list onto the file
def write_students_to_file(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            line = f"{str(student.get_student_number()).ljust(5)}\t{str(student.first_name).ljust(15)}\t{str(student.get_last_name()).ljust(15)}\t{str(student.date_of_birth).ljust(15)}\t{str(student.sex).ljust(15)}\t{str(student.country_of_birth).ljust(15)}\n"
            file.write(line)


# clears out the list sets the Class attr for student num to 0. reads info from file and adds it to the list
def read_students_from_file(filename, database):
    database.clear_all()
    Student.student_number = 0

    with open(filename, 'r') as file:
        
        for line in file:
                
            data = line.strip().split()
            num, first_name, last_name, date_of_birth, sex, country_of_birth = map(str, data)

            # Create a new Student object and add it to the database
            student = Student(first_name, last_name, date_of_birth, sex, country_of_birth)
            database.add_student(student)
            

students = StudentContainer()
print("enter choice (1-9):\n1 => Save to file\n2 => Read from file and save to array\n3 => Add a new student\n4 => Find student by student number and get all data\n5 => Show all Students\n6 => Show all students born in a given year\n7 => Modify a student record: input the student number, ask the field to modify, and get the new value from the user. Modify the record accordingly.\n8 => Delete a student with a specific student number\n9 => See Menu\n0 => Exit\n")
while True:
    choice = int(input())

    match choice:
        case 1:
            write_students_to_file(students.students, "students.txt")
            print("Success! Saved to file.")
        case 2:
            read_students_from_file("students.txt", students)
        case 3:
            first_name = input("Enter Fist name: ")
            last_name = input("Enter last_name: ")
            date_of_birth = input("Enter date_of_birth: ")
            sex = input("Enter sex: ")
            country_of_birth = input("Enter country_of_birth: ")
            student = Student(first_name, last_name, date_of_birth, sex, country_of_birth)
            students.add_student(student)
        case 4:
            student_number_to_find = input("Enter Student Number: ")
            students.print_student_info(student_number_to_find)
        case 5:
            students.print_all_students_info()
        case 6:
            year = input("Enter year of birth: ")
            students.print_students_by_birth_year(year)
        case 7:
            num = input("Enter student number: ")
            students.modify_student_record(student_number = num)
        case 8:
            num = input("Enter student number: ")
            students.delete_student_by_number(num)
        case 9:
            print("enter choice (1-9):\n1 => Save to file\n2 => Read from file and save to array\n3 => Add a new student\n4 => Find student by student number and get all data\n5 => Show all Students\n6 => Show all students born in a given year\n7 => Modify a student record: input the student number, ask the field to modify, and get the new value from the user. Modify the record accordingly.\n8 => Delete a student with a specific student number\n9 => See Menu\n0 => Exit\n")
        case 0:
            break

            