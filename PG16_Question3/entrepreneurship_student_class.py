from student import *  # Importing everything in file students including class student and csv, sys and datetime
# libraries


# creating class EntrepreneurshipStudent which inherits from class student
class EntrepreneurshipStudent(Student):
    # Init method will access init method of the parent class and initialize additional instance variables specific to
    # the Entrepreneurship degree program
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number,
                 date_of_enrollment, year):
        # Accessing parent class init method
        super().__init__(student_email, student_name, gender, date_of_birth, address, phone_number,
                         date_of_enrollment, year)
        self.major = "Entrepreneurship"  # student's major is Entrepreneurship by default
        self.venture = []   # All Entrepreneurship students have a venture
        self.expected_graduation_date = self.date_of_enrollment + datetime.timedelta(weeks=104)  # expected graduation
        # date is calculated by adding 2 years to the date of enrollment which is the duration of this degree program
        try:
            # Opens the file in which all students records are kept in read mode as file object student_records
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)  # Read all lines in the file and assign them to variable
                # read_student as a list
                for student in read_student:  # Looping through all lines(students) in the file
                    if self.student_email in student:
                        break  # If student email is already recorded in file the loop will break and they will not be
                        # recorded again as each time a student wants to do an operation a new instance is created so
                        # they would be recorded on file multiple times

                else:  # If the student's email is not recorded on file they will be recorded

                    # Opens the same file with student records in append mode, and add a newline parameter to specify
                    # that no blank line should be left between two lines when writing on the file
                    with open("student_records.csv", 'a', newline='') as add_record:
                        # Field names for each field of the line, they can also be considered as column names
                        fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                                      'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                                      'expected_graduation_date', 'internship']
                        record_student = csv.DictWriter(add_record, fieldnames=fieldnames)  # Creating a writing object
                # and using DictWriter method to record student information as values of the fieldnames keys

                        # Recording student information on a single line(row), only key values will be recorded
                        record_student.writerow(
                            {"student_email": self.student_email, "student_name": self.student_name, "gender": self.gender,
                             "date_of_birth": self.date_of_birth,
                             "address": self.address, "phone_number": self.phone_number, "major": self.major,
                             "date_of_enrollment": self.date_of_enrollment,
                             "year": self.year, "status": self.status,
                             "github_username/venture/mission": self.venture,
                             "expected_graduation_date": self.expected_graduation_date, "internship": self.internship})
                    print("Entrepreneurship student registered successfully!")
        except OSError as e:
            print("File not found", e)  # printed if a file can not be accessed, e represents
            # exception-type object and it will give more clarity on the OSError which occurred
            sys.exit()  # Ends the program with exit function

    # a method for displaying degree program outline to the user
    # made a static method because the degree program outline does not vary from student to student although it varies
    # between degree programs hence it can be called without an object
    @staticmethod
    def view_degree_program_outline():
        try:
            # opens the file containing the outline of the degree program in reading mode
            with open("ent_degree_program_outline", "r") as ent_program_outline:
                print(ent_program_outline.read())  # reads the file and displays the information in the file
                return True  # returns true to indicate that the file was opened and read
        except OSError as e:
            print("File not found", e)  # printed if a file can not be accessed
            sys.exit()   # Ends the program with exit function

    # Method to promote students to  another year
    def promote_student(self):
        if self.year == 2:  # checks of the Entrepreneurship student is in his/her final year hence can't be promoted
            return "The student was in his/her final year."

        else:  # promotes the student if he/she hasn't reached the final year
            self.year += 1  # increments student year of study by 1
            try:
                # Opens the file in which all students records are kept in read mode as file object student_records
                with open("student_records.csv", 'r') as student_records:
                    read_student = csv.reader(student_records)  # Read all lines in the file and assign them to variable
                # read_student as a list
                    updated_student_records = []  # will contain all lines of the file after being updated
                    for student in read_student:  # Looping through all lines(students) in the file
                        # since each line is a list itself, and the student email is the first item the condition is
                        # checking for each line if the element at index [0] is equal to the email of the calling
                        # instance as we want to know on which line is the information about the calling instance kept
                        if self.student_email == student[0]:
                            student[8] = self.year  # 8th index on list which holds the year is updated with new year
                        updated_student_records.append(student)  # Each line under iteration is appended on the list
                        # whether updated or not
            except OSError as e:
                print("File not found", e)  # This will be printed if a file can not be accessed
                sys.exit()  # Ends the program with exit function

            # Opens the same file with student records in write mode, and add a newline parameter to specify that no
            # blank line should be left between two lines when writing on the file
            with open("student_records.csv", 'w', newline="") as student_records:
                # Field names for each field of the line, they can also be considered as column names
                fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                              'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                              'expected_graduation_date', 'internship']
                write_student = csv.DictWriter(student_records, fieldnames=fieldnames)  # Creating a writing object
                # and using DictWriter method to record student information as values of the fieldnames keys
                for student in updated_student_records:  # Looping through lines (student records) stored in the list
                    # Writing each line on the list again as a separate row (line) and using indexes to access
                    # where information is stored on the list(line stored as a list) as it is uniform in all lines.
                    write_student.writerow(
                        {"student_email": student[0], "student_name": student[1], "gender": student[2],
                         "date_of_birth": student[3],
                         "address": student[4], "phone_number": student[5], "major": student[6],
                         "date_of_enrollment": student[7],
                         "year": student[8], "status": student[9], "github_username/venture/mission": student[10],
                         "expected_graduation_date": student[11], "internship": student[12]})
            return f"Student is now in year {self.year}"  # returns message with new year

    # a method for changing student status
    def change_student_status(self):
        if datetime.date.today() >= self.expected_graduation_date:  # checks if student is done with the studies
            try:
                # Opens the file in which all students records are kept in read mode as file object student_records
                with open("student_records.csv", 'r') as student_records:
                    read_student = csv.reader(student_records)  # Read all lines in the file and assign them to variable
                # read_student as a list
                    updated_student_records = []  # will contain all lines of the file after being updated
                    for student in read_student: # Looping through all lines(students) in the file
                        # checking for each line if the element at index [0] is equal to the email of the calling
                        # instance
                        if self.student_email == student[0]:
                            self.status = "Alumni"  # updates student status to Alumni in variable instance
                            student[9] = self.status  # updates student status to Alumni in the file
                        updated_student_records.append(student)  # Each line under iteration is appended on the list
                        # whether updated or not
            except OSError as e:
                print("File not found", e)  # This will be printed if a file can not be accessed
                sys.exit()  # Ends the program with exit function

            # Opens the same file with student records in write mode, and add a newline parameter to specify that no
            # blank line should be left between two lines when writing on the file
            with open("student_records.csv", 'w', newline="") as student_records:
                # Field names for each field of the line, they can also be considered as column names
                fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                              'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                              'expected_graduation_date', "internship"]
                write_student = csv.DictWriter(student_records, fieldnames=fieldnames)  # Creating a writing object
                # and using DictWriter method to record student information as values of the fieldnames keys
                for student in updated_student_records:  # Looping through lines (student records) stored in the list
                    # Writing each line on the list again as a separate row (line) and using indexes to access
                    # where information is stored on the list(line stored as a list) as it is uniform in all lines.
                    write_student.writerow(
                        {"student_email": student[0], "student_name": student[1], "gender": student[2],
                         "date_of_birth": student[3],
                         "address": student[4], "phone_number": student[5], "major": student[6],
                         "date_of_enrollment": student[7],
                         "year": student[8], "status": student[9], "github_username/venture/mission": student[10],
                         "expected_graduation_date": student[11], "internship": student[12]})
            return "Student done is done with the degree program"  # return value when the student's graduation date has
            # reached

        else:
            # return value when the student's graduation date hasn't reached yet
            return f"Student will graduate on {self.expected_graduation_date}"

    #  a method to display computer science student information
    def print_student_information(self):
        try:
            # Opens the file in which all students records are kept in read mode as file object student_records
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)  # Read all lines in the file and assign them to variable
                # read_student as a list
                for student in read_student:  # Looping through all lines(students) in the file
                    # checking for each line if the element at index [0] is equal to the email of the calling
                    # instance
                    if self.student_email == student[0]:
                        # returns student information by reading from file using the index on which the info is located
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
                               f"Venture: {student[10]}\n" \
                               f"Expected graduation date: {student[11]}\n" \
                               f"Internships:{student[12]}\n"
        except OSError as e:
            print("File not found", e)  # This will be printed if a file can not be accessed
            sys.exit()  # Ends the program with exit function

    # Method to add student venture
    def add_venture_details(self):
        try:
            # Opens the file in which all students records are kept in read mode as file object student_records
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)  # Read all lines in the file and assign them to variable
                # read_student as a list
                updated_student_records = []  # will contain all lines of the file after being updated
                for student in read_student:  # Looping through all lines(students) in the file
                    # since each line is a list itself, and the student email is the first item the condition is checking
                    # for each line if the element at index [0] is equal to the email of the calling instance as we want
                    # to know on which line is the information about the calling instance kept
                    if self.student_email == student[0]:
                        # The user enters venture details and they are kept in a dictionary
                        venture_details = {"Venture name": input("Enter the venture name: "),
                                           "Venture details": input("Enter the student's venture details: ")}

                        if student[10] != '[]':  # checks if the students  has had a venture before. This '[]' would be
                            # the value stored on index[10] if the student had zero ventures as the default value for
                            # self.venture is an empty list
                            self.venture.append(student[10])  # Append ventures the student had before on file to the instance variable.
                            # The instance variable is initially empty as a student object is created once again, regardless
                            # that they are recorded on the file and the variable is initialized to empty list in the init method
                            self.venture.append(venture_details)  # Append new venture to the instance variable.
                            student[10] = ''  # The index which holds student venture information is emptied because it
                            # will be replaced by the information in self.venture, and there would be a repetition as
                            # what the index holds was also appended to the instance variable
                            for venture in self.venture:  # Loops through all ventures held in the instance variable
                                student[10] += str(venture)  # Appends the venture under iteration to the ventures
                                # recorded in the previous iterations

                        else:  # This would be implemented if the student has never had a venture before
                            student[10] = ""  # "[]" is removed from the index on which ventures are recorded
                            self.venture.append(venture_details)  # Append new venture to the instance variable.
                            for venture in self.venture:  # Loops through all ventures held in the instance variable
                                student[10] += str(venture)  # Appends the venture under iteration to the ventures
                                # recorded in the previous iterations
                    updated_student_records.append(student)  # Each line under iteration is appended on the list
                    # whether updated or not
        except OSError as e:
            print("File not found", e)  # This will be printed if a file can not be accessed
            sys.exit()  # Ends the program with exit function

        # Opens the same file with student records in write mode, and add a newline parameter to specify that no
        # blank line should be left between two lines when writing on the file
        with open("student_records.csv", 'w', newline="") as student_records:
            # Field names for each field of the line, they can also be considered as column names
            fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address', 'phone_number',
                          'major', 'date_of_enrollment', 'year', 'status', 'github_username/venture/mission',
                          'expected_graduation_date', "internship"]
            write_student = csv.DictWriter(student_records, fieldnames=fieldnames)  # Creating a writing object
            # and using DictWriter method to record student information as values of the fieldnames keys
            for student in updated_student_records:  # Looping through lines (student records) stored in the list
                # Writing each line on the list again and using indexes to access where information is stored on
                # the list(line stored as a list) as it is uniform in all lines.
                write_student.writerow(
                    {"student_email": student[0], "student_name": student[1], "gender": student[2],
                     "date_of_birth": student[3],
                     "address": student[4], "phone_number": student[5], "major": student[6],
                     "date_of_enrollment": student[7],
                     "year": student[8], "status": student[9], "github_username/venture/mission": student[10],
                     "expected_graduation_date": student[11], "internship": student[12]})

        return "Venture added successfully!"  # Method return value
