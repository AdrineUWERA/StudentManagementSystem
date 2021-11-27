from student import *


class EntrepreneurshipStudent(Student):
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number,
                 date_of_enrollment, year):
        super().__init__(student_email, student_name, gender, date_of_birth, address, phone_number,
                         date_of_enrollment, year)
        self.major = "Entrepreneurship"
        self.venture = []
        self.expected_graduation_date = self.date_of_enrollment + datetime.timedelta(weeks=104)
        print("Entrepreneurship student registered successfully!")

    @staticmethod
    def view_degree_program_outline():
        ent_program_outline = open("ent_degree_program_outline", "r")
        print(ent_program_outline.read())
        ent_program_outline.close()
        return True

    def promote_student(self):
        if self.year == 2:
            return "The student was in his/her final year."
        else:
            return super().promote_student()

    def change_student_status(self):
        if datetime.datetime.now() >= self.expected_graduation_date:
            self.status = "Alumni"
            return "The student is done with the degree program!"
        else:
            return f"Student will graduate {self.expected_graduation_date}"

    def print_student_information(self):
        return super().print_student_information() + f"\nVenture:{self.venture}\nExpected graduation date:" \
                                                     f"{self.expected_graduation_date}"

    def add_venture_details(self):
        venture_details = {"Venture name": input("Enter the venture name: "),
                           "Venture details": input("Enter the student's venture details: ")}
        self.venture.append(venture_details)
        return "Venture added successfully!"