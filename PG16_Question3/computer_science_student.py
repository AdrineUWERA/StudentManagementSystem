from student import *


class ComputerScienceStudent(Student):
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number,
                 date_of_enrollment, year, github_username):
        super().__init__(student_email, student_name, gender, date_of_birth, address, phone_number,
                         date_of_enrollment, year)
        self.major = "Computer Science"
        self.github_username = github_username
        self.expected_graduation_date = self.date_of_enrollment + datetime.timedelta(weeks=208)
        try:
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)
                for student in read_student:
                    if self.student_email in student:
                        break
                else:
                    with open("student_records.csv", 'a', newline='') as add_record:
                        fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                                      'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                                      'expected_graduation_date', 'internship']
                        record_student = csv.DictWriter(add_record, fieldnames=fieldnames)
                        record_student.writerow(
                            {"student_email": self.student_email, "student_name": self.student_name, "gender": self.gender,
                             "date_of_birth": self.date_of_birth,
                             "address": self.address, "phone_number": self.phone_number, "major": self.major,
                             "date_of_enrollment": self.date_of_enrollment,
                             "year": self.year, "status": self.status,
                             "github_username/venture/mission": self.github_username,
                             "expected_graduation_date": self.expected_graduation_date, "internship": self.internship})
                    print("Computer science student registered successfully!")
        except OSError as e:
            print("File not found", e)
            sys.exit()

    @staticmethod
    def view_degree_program_outline():
        try:
            with open("CS_degree_program_outline.tx", "r") as cs_program_outline:
                print(cs_program_outline.read())
                return True
        except OSError as e:
            print("File not found", e)
            sys.exit()

    def promote_student(self):
        if self.year == 4:
            return "The student is in his/her final year"

        else:
            self.year += 1
            try:
                with open("student_records.csv", 'r') as student_records:
                    read_student = csv.reader(student_records)
                    updated_student_records = []
                    for student in read_student:
                        if self.student_email == student[0]:
                            student[8] = self.year
                        updated_student_records.append(student)
            except OSError as e:
                print("File not found", e)
                sys.exit()

            with open("student_records.csv", 'w', newline="") as student_records:
                fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                              'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                              'expected_graduation_date', 'internship']
                write_student = csv.DictWriter(student_records, fieldnames=fieldnames)
                for student in updated_student_records:
                    write_student.writerow(
                        {"student_email": student[0], "student_name": student[1], "gender": student[2],
                         "date_of_birth": student[3],
                         "address": student[4], "phone_number": student[5], "major": student[6],
                         "date_of_enrollment": student[7],
                         "year": student[8], "status": student[9], "github_username/venture/mission": student[10],
                         "expected_graduation_date": student[11],  "internship": student[12]})
            return f"Student is now in year {self.year}"

    def change_student_status(self):
        if datetime.date.today() >= self.expected_graduation_date:
            try:
                with open("student_records.csv", 'r') as student_records:
                    read_student = csv.reader(student_records)
                    updated_student_records = []
                    for student in read_student:
                        if self.student_email == student[0]:
                            self.status = "Alumni"
                            student[9] = self.status
                        updated_student_records.append(student)

            except OSError as e:
                print("File not found", e)
                sys.exit()

            with open("student_records.csv", 'w', newline="") as student_records:
                fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                              'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                              'expected_graduation_date', "internship"]
                write_student = csv.DictWriter(student_records, fieldnames=fieldnames)
                for student in updated_student_records:
                    write_student.writerow(
                        {"student_email": student[0], "student_name": student[1], "gender": student[2],
                         "date_of_birth": student[3],
                         "address": student[4], "phone_number": student[5], "major": student[6],
                         "date_of_enrollment": student[7],
                         "year": student[8], "status": student[9], "github_username/venture/mission": student[10],
                         "expected_graduation_date": student[11], "internship": student[12]})

            return "Student done is done with the degree program"

        else:
            return f"Student will graduate on {self.expected_graduation_date}"

    def print_student_information(self):
        try:
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)
                for student in read_student:
                    if self.student_email == student[0]:
                        return f"Student information: \n" \
                               f"Student email: {student[0]}\n" \
                               f"Student name: {student[1]}\n" \
                               f"Gender: {student[2]}\n" \
                               f"Date of birth: {student[3]}\n" \
                               f"Address: {student[4]}\n" \
                               f"Phone number: {student[5]}\n" \
                               f"Major: {student[6]}\n" \
                               f"Date of enrollment: {student[7]}\n" \
                               f"Year:{student[8]}\n" \
                               f"Status: {student[9]}\n" \
                               f"Github username: {student[10]}\n" \
                               f"Expected graduation date: {student[11]}\n" \
                               f"Internships:{student[12]}\n"
        except OSError as e:
            print("File not found", e)
            sys.exit()
