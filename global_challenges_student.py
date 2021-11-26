from student import Student
import datetime


class GlobalChallengesStudent(Student):
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number, degree,
                 year, mission):
        super().__init__(student_email, student_name, gender, date_of_birth, address, phone_number, degree, year)
        self.mission = mission
        self.expected_graduation_date = self.date_of_enrollment + datetime.timedelta(weeks=156)
        # 156 weeks equals to 3 years
        print("Global challenges student registered successfully!")

    @staticmethod
    def view_degree_program_outline(self):
        cs_program_outline = open("GC_degree_program_outline.tx", "r")
        print(cs_program_outline.read())

    def promote_student(self):
        if self.year == 3:
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
        print(f"Mission: {self.mission}\n"
              f"Expected graduation date: {self.expected_graduation_date}")

