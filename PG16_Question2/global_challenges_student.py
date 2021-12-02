from student import *


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
        try:
            with open("GC_degree_program_outline.tx", "r") as gc_program_outline: 
                print(gc_program_outline.read())
                return True
        except OSError as e:
            print("File not found", e)

    def promote_student(self):
        if self.year == 3:
            return "The student is in his/her final year"

        else:
            return super().promote_student()

    def change_student_status(self):
        if datetime.datetime.now() >= self.expected_graduation_date:
            self.status = "Alumni"
            return "Student done is done with the degree program"

        else:
            return f"Student will graduate on {self.expected_graduation_date}"

    def print_student_information(self):

        return super().print_student_information() + f"\nMission: {self.mission}\n" \
              f"Expected graduation date: {self.expected_graduation_date}"
