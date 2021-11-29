import datetime

student_records = []


class Student:
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number,
                 date_of_enrollment, year):
        self.student_email = student_email
        self.student_name = student_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.major = ""
        self.year = year
        date_of_enrollment = list(map(int, date_of_enrollment.strip().split("-")))
        self.date_of_enrollment = datetime.datetime(date_of_enrollment[0], date_of_enrollment[1], date_of_enrollment[2])
        self.year = year
        self.status = "Current"
        self.internship = []
        student_records.append(self)

    def print_student_information(self):
        return f"Student information: \n"\
               f"Student email: {self.student_email}\n"\
               f"Student name: {self.student_name}\n"\
               f"Gender: {self.gender}\n"\
               f"Date of birth: {self.date_of_birth}\n"\
               f"Address: {self.address}\n"\
               f"Phone number: {self.phone_number}\n"\
               f"Major: {self.major}\n"\
               f"Date of enrollment: {self.date_of_enrollment}\n"\
               f"Year:{ self.year}\n"\
               f"Status: {self.status}\n"\
               f"Internships:{ self.internship}"

    def promote_student(self):
        self.year += 1
        return f"Student is now in year {self.year}"

    def update_student_information(self):
        print("Choose: \n1.Update phone number\n2.Update address\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_phone_number = input("Enter student's new phone number: ")
            self.phone_number = new_phone_number
            return f"Phone number updated successfully to {self.phone_number}"
        elif choice == 2:
            new_address = input("Enter student's new address: ")
            self.address = new_address
            return f"Address updated successfully to {self.address}"
        else:
            return "Invalid input!"

    def add_student_internship(self):
        internship_details = {"Company name": input("Enter the name of the company the student interned at: "),
                              "Start date": input("Enter the start date of the internship: "),
                              "End date": input("Enter the end date of the internship: "),
                              "Position": input("Enter the position the student had in the internship: ")}

        self.internship.append(internship_details)
        return "internship added successfully!"


# st1 = Student("a", "b", "c","d","e","f","g")
# print(st1.print_student_information())
