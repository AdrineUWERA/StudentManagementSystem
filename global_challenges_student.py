from student import Student
import datetime


class GlobalChallengesStudent(Student):
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number,
                 date_of_enrollment, year, mission):
        super().__init__(student_email, student_name, gender, date_of_birth, address, phone_number,
                         date_of_enrollment, year)
        self.major = "Global Challenges"
        self.mission = mission
        self.expected_graduation_date = self.date_of_enrollment + datetime.timedelta(weeks=156)
        # 156 weeks equals to 3 years
        print("Global challenges student registered successfully!")

    @staticmethod
    def view_degree_program_outline():
        gc_program_outline = open("GC_degree_program_outline.tx", "r")
        print(gc_program_outline.read())
        gc_program_outline.close()
        return True

    def promote_student(self):
        if self.year == 3:
            return "The student is in his/her final year"

        else:
            return super().promote_student()

    def change_student_status(self):
        if datetime.datetime.now() >= self.expected_graduation_date:
            self.student_status = "Alumni"
            return "Student done is done with the degree program"

        else:
            return f"Student will graduate on {self.expected_graduation_date}"

    def print_student_information(self):

        return super().print_student_information() + f"Mission: {self.mission}\n" \
              f"Expected graduation date: {self.expected_graduation_date}"
