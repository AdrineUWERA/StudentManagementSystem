from student import *


class InternationalBusinessAndTradeStudent(Student):
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number, degree, year):
        super().__init__(student_email, student_name, gender, date_of_birth, address, phone_number, degree, year)
        self.venture = []
        self.expected_graduation_date = self.date_of_enrollment + datetime.timedelta(weeks=156)
        print("IBT student registered successfully!")

    @staticmethod
    def view_degree_program_outline():
        ibt_program_outline = open("ibt_degree_program_outline", "r")
        print(ibt_program_outline.read())

    def promote_student(self):
        if self.year == 3:
            print("The student was in his/her final year.")
        else:
            super().promote_student()

    def change_student_status(self):
        if datetime.datetime.now() >= self.expected_graduation_date:
            self.status = "Alumni"
            print("The student is done with the degree program!")
        else:
            print(f"Student will graduate {self.expected_graduation_date}")

    def print_student_information(self):
        super().print_student_information()
        print(f"Venture:{self.venture}\n"
              f"Expected graduation date:{self.expected_graduation_date}")

    def add_venture_details(self):
        venture_details = {"Venture name": input("Enter the venture name: "),
                           "Venture details": input("Enter the student's venture details: ")}
        self.venture.append(venture_details)





