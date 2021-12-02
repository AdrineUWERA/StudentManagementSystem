import unittest
from student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student1 = Student("a.ana@alustudent.com", "Allie Ana", "F", "2003-02-01",
                                "Kimironko", "+234788888888", "2020-11-26", 1)

    def test_update_student_information(self):
        self.assertIn(self.student1.update_student_information(), f"Phone number updated successfully to "
                                                                  f"{self.student1.phone_number}!")
        self.assertIn(self.student1.update_student_information(), f"Address updated successfully to"
                                                                  f" {self.student1.address}")

    def test_promote_student(self):
        self.assertEqual(self.student1.promote_student(), "Student is now in year 2")

    def test_add_student_internship(self):
        self.assertEqual(self.student1.add_student_internship(), "internship added successfully!")

    def test_print_student_information(self):
        self.assertEqual(self.student1.print_student_information(),
'''Student information: 
Student email: a.ana@alustudent.com
Student name: Allie Ana
Gender: F
Date of birth: 2003-02-01
Address: Kimironko
Phone number: +234788888888
Major: 
Date of enrollment: 2020-11-26 00:00:00
Year:1
Status: Current
Internships:[]''')


if __name__ == '__main__':
    unittest.main()
