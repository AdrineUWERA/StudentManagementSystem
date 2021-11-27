from computer_science_student import ComputerScienceStudent
from global_challenges_student import GlobalChallengesStudent
from international_business_and_trade_student_class import InternationalBusinessAndTradeStudent
from entrepreneurship_student_class import EntrepreneurshipStudent
from student import student_records
import sys

print("\nALU STUDENT MANAGEMENT SYSTEM")
print("-----------------------------")


def re_run():
    while True:
        operation2 = str(input("\nEnter 'Y' if you would like to do any other operation and 'N' if you do not want to: "))
        if operation2.upper() in ('Y', 'N'):
            break
        print("\nInvalid input. Choose 'Y' or 'N'.\n")
    if operation2.upper() == 'Y':
        main()
    else:
        sys.exit("Thank you!!")


def main():
    print("\nUser categories:\n"
          "1. Registrar Office\n"
          "2. Student\n")
    while True:
        user = input("Enter choice: ")
        if user in ('1', '2'):
            break
        print("\nInvalid input. Choose '1' or '2'.\n")
    if user == '1':
        print("\nChoose \n"
              "1. Register student\n"
              "2. View student information\n"
              "3. Promote student\n"
              "4. Change student status\n"
              "5. Update student information\n"
              "6. View degree program outline\n"
              "7. Add student internship\n"
              "8. Add student venture\n"
              "or other key to exit\n")
        action = input("Enter your choice: ")
        if action == '1':
            print("\nRegister student")
            print("----------------")
            print("Choose major the student will be taking:\n"
                  "1. Computer science\n"
                  "2. International Business and Trade\n"
                  "3. Global challenges\n"
                  "4. Entrepreneurship\n")
            student_major = input("Enter choice: ")
            if student_major == '1':
                student = ComputerScienceStudent(
                    student_email=input("Enter student's email: "),
                    student_name=input("Enter student's name: "),
                    gender=input("Enter student's gender: "),
                    date_of_birth=input("Enter student's date of birth (YYYY-MM-DD) and use digit: "),
                    address=input("Enter student's address: "),
                    phone_number=input("Enter student's phone number: "),
                    year=input("Enter student's year of study: "),
                    date_of_enrollment=input("Enter student's date of enrollment (YYYY MM DD) "
                                             "separated by space and use digit"),
                    github_username=input("Enter student's Github username: "))

            elif student_major == '2':
                student = InternationalBusinessAndTradeStudent(
                    student_email=input("Enter student's email: "),
                    student_name=input("Enter student's name: "),
                    gender=input("Enter student's gender: "),
                    date_of_birth=input("Enter student's date of birth (YYYY-MM-DD): "),
                    address=input("Enter student's address: "),
                    phone_number=input("Enter student's phone number: "),
                    date_of_enrollment=input("Enter student's date of enrollment (YYYY MM DD) "
                                             "separated by space and use digit"),
                    year=input("Enter student's year of study: "))

            elif student_major == '3':
                student = GlobalChallengesStudent(
                    student_email=input("Enter student's email: "),
                    student_name=input("Enter student's name: "),
                    gender=input("Enter student's gender: "),
                    date_of_birth=input("Enter student's date of birth: "),
                    address=input("Enter student's address: "),
                    phone_number=input("Enter student's phone number: "),
                    date_of_enrollment=input("Enter student's date of enrollment (YYYY MM DD) "
                                             "separated by space and use digit"),
                    year=input("Enter student's year of study: "),
                    mission=input("Enter student's mission: "))
            elif student_major == '4':
                student = EntrepreneurshipStudent(
                    student_email=input("Enter student's email: "),
                    student_name=input("Enter student's name: "),
                    gender=input("Enter student's gender: "),
                    date_of_birth=input("Enter student's date of birth (YYYY-MM-DD): "),
                    address=input("Enter student's address: "),
                    phone_number=input("Enter student's phone number: "),
                    date_of_enrollment=input("Enter student's date of enrollment (YYYY MM DD) "
                                             "separated by space and use digit"),
                    year=input("Enter student's year of study: "))

        elif action == '2':
            print("\nStudent information")
            print("-------------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    print(student.print_student_information())
                    break
            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '3':
            print("\nPromote student")
            print("---------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    print(student.promote_student())
                    break
            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '4':
            print("\nChange student's status")
            print("-----------------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    print(student.change_student_status())
                    break
            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '5':
            print("\nUpdate student information")
            print("--------------------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    print(student.update_student_information())
                    break

            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '6':
            print("\nView degree program outline")
            print("---------------------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    student.view_degree_program_outline()
                    break

            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '7':
            print("\nAdd student internship")
            print("---------------------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    print(student.add_student_internship())
                    break

            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '8':
            print("\nAdd student's venture")
            print("---------------------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    if student.major == "International Business And Trade" or student.major == "Entrepreneurship":
                        print(student.add_venture_details())
                        break
                    else:
                        print("Student's major must be IBT or ENT to add venture.")

            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

    elif user == '2':
        print("\nChoose \n"
              "1. Update information\n"
              "2. View degree program outline\n"
              "3. Add internship\n"
              "4. Add venture")
        action = input("Enter choice: ")
        if action == '1':
            print("\nUpdate student information")
            print("--------------------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    print(student.update_student_information())
                    break

            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '2':
            print("\nView degree program outline")
            print("---------------------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    student.view_degree_program_outline()
                    break

            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '3':
            print("\nAdd student internship")
            print("---------------------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    print(student.add_student_internship())
                    break

            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

        elif action == '4':
            print("\nAdd venture")
            print("----------------")
            email = input("Enter student email: ")
            for student in student_records:
                if student.student_email == email:
                    if student.major == "International Business And Trade" or student.major == "Entrepreneurship":
                        print(student.add_venture_details())
                        break
                    else:
                        print("You must be an IBT or ENT major to add venture.")
            else:
                print("Couldn't find the student with email provided! Check the email and try again.\n")

    re_run()


# This code calls the 'main' function
if __name__ == '__main__':
    main()