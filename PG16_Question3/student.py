import datetime
import csv
import sys


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
        try:
            date_of_enrollment = list(map(int, date_of_enrollment.strip().split("-")))
            self.date_of_enrollment = datetime.date(date_of_enrollment[0], date_of_enrollment[1],
                                                    date_of_enrollment[2])
        except IndexError as e:
            print("Separate year, month, date with a hyphen(-). Use YYYY-MM-DD format.", e)
            sys.exit()
        except ValueError as e:
            print("Use digits only! And check if date is correct with YYYY-MM-DD format.", e)
            sys.exit()
        self.year = year
        self.status = "Current"
        self.internship = []

    def print_student_information(self):

        return f"Student information: \n" \
               f"Student email: {self.student_email}\n" \
               f"Student name: {self.student_name}\n" \
               f"Gender: {self.gender}\n" \
               f"Date of birth: {self.date_of_birth}\n" \
               f"Address: {self.address}\n" \
               f"Phone number: {self.phone_number}\n" \
               f"Major: {self.major}\n" \
               f"Date of enrollment: {self.date_of_enrollment}\n" \
               f"Year:{self.year}\n" \
               f"Status: {self.status}\n" \
               f"Internships:{self.internship}"

    def promote_student(self):
        self.year += 1
        return f"Student is now in year {self.year}"

    def update_student_information(self):
        print("Choose: \n1.Update phone number\n2.Update address\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)
                updated_student_records = []
                for student in read_student:
                    if self.student_email == student[0]:
                        new_phone_number = input("Enter student's new phone number: ")
                        self.phone_number = new_phone_number
                        student[5] = self.phone_number
                    updated_student_records.append(student)

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

            return f"Phone number updated successfully to {self.phone_number}"

        elif choice == '2':
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)
                updated_student_records = []
                for student in read_student:
                    if self.student_email == student[0]:
                        new_address = input("Enter student's new address: ")
                        self.address = new_address
                        student[4] = self.address
                    updated_student_records.append(student)

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

            return f"Address updated successfully to {self.address}"
        else:
            return "Invalid input!"

    def add_student_internship(self):
        with open("student_records.csv", 'r') as student_records:
            read_student = csv.reader(student_records)
            updated_student_records = []
            for student in read_student:
                if self.student_email == student[0]:
                    internship_details = {
                        "Company name": input("Enter the name of the company the student interned at: "),
                        "Start date": input("Enter the start date of the internship: "),
                        "End date": input("Enter the end date of the internship: "),
                        "Position": input("Enter the position the student had in the internship: ")}
                    if student[12] != '[]':
                        self.internship.append(student[12])
                        self.internship.append(internship_details)
                        student[12] = ''
                        for internship in self.internship:
                            student[12] += str(internship)
                    else:
                        student[12] = ""
                        self.internship.append(internship_details)
                        for internship in self.internship:
                            student[12] += str(internship)
                updated_student_records.append(student)

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

        return "internship added successfully!"
