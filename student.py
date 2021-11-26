import datetime

student_records = []


class Student:
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number, degree, year):
        self.student_email = student_email
        self.student_name = student_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.degree = degree
        self.year = year
        self.student_status = "Current"
        self.date_of_enrollment = datetime.datetime.now()
        self.year = year
        self.status = "Current"
        self.internship = []
        student_records.append(self)
        print("Student registered successfully!")

    def print_student_information(self):
        print(f"Student information: \n"
              f"Student email: {self.student_email}\n"
              f"Student name: {self.student_name}\n"
              f"Gender:{self.gender}\n"
              f"Date of birth: {self.date_of_birth}\n"
              f"Address: {self.address}\n"
              f"Phone number: {self.phone_number}\n"
              f"Degree: {self.degree}\n"
              f"Date of enrollment: {self.date_of_enrollment}\n"
              f"Year:{self.year}\n"
              f"Status:{self.status}\n"
              f"Internships:{self.internship}")

    def promote_student(self):
        self.year += 1
        print(f"Student is now in year {self.year}")

    def update_student_information(self):
        print("Choose: \n1.Update phone number\n2.Update address\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_phone_number = input("Enter student's new phone number: ")
            self.phone_number = new_phone_number
            print(f"Phone number updated successfully to {self.phone_number}")
        elif choice == 2:
            new_address = input("Enter student's new address: ")
            self.address = new_address
            print(f"Address updated successfully to {self.address}")
        else:
            print("Invalid input!")

    def add_student_internship(self):
        internship_details = {"Company name": input("Enter the name of the company the student interned at: "),
                              "Start date": input("Enter the start date of the internship: "),
                              "End date": input("Enter the end date of the internship: "),
                              "Position": input("Enter the position the student had in the internship: ")}

        self.internship.append(internship_details)


# st1 = Student("a", "b", "c","d","e","f","g","2021 2 11","i")
# st1.print_student_information()