from student import Student     # imports Student class from student file
import datetime     # imports datetime modules


class ComputerScienceStudent(Student):      # class named ComputerScienceStudent that inherits Student class
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number,year,
                 github_username):        # initialize ComputerScienceStudent properties
        super().__init__(student_email, student_name, gender, date_of_birth, address, phone_number, year)      # Access init method of student class (parent class)
        self.major = "Computer Science"
        self.github_username = github_username
        self.expected_graduation_date = self.date_of_enrollment + datetime.timedelta(weeks=208)
        # 208 weeks equals to 4 years
        print("Computer science student registered successfully!")

    @staticmethod
    def view_degree_program_outline():
        cs_program_outline = open("CS_degree_program_outline.tx", "r")
        print(cs_program_outline.read())

    def promote_student(self):
        if self.year == 4:
            print("The student is in his/her final year")

        else:
            self.year += 1
            print(f"Student is now in year {self.year}")

    def change_student_status(self):
        if datetime.datetime.now() >= self.expected_graduation_date:
            self.student_status = "Alumni"

        else:
            print(f"Student will graduate on {self.expected_graduation_date}")

    def print_student_information(self):
        super().print_student_information()
        print(f"Github username: {self.github_username}\n"
              f"Expected graduation date: {self.expected_graduation_date}")


# st1 = ComputerScienceStudent("a", "b", "c","d","e","f","g","h","i","k")
# st1.view_degree_program_outline()
