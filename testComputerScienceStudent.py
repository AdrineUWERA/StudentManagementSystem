import unittest
from computer_science_student import ComputerScienceStudent


class TestComputerScienceStudent(unittest.TestCase):

    def setUp(self):
        self.cs_student1 = ComputerScienceStudent('a.ana@alustudent.com', 'Allie Ana', 'F', '2003-02-01',
                                                  'Kimironko', '+234788888888', '2021 01 09', 1, 'AllieAn')
        self.cs_student2 = ComputerScienceStudent('k.rema@alustudent.com', 'Kofi Rema', 'M', '2000-07-03',
                                                  'Gikondo', '+250789888876', '2017 01 01', 4, 'KofiRem')

    def test__init__(self):
        cs_student1 = ComputerScienceStudent('a.ana@alustudent.com', 'Allie Ana', 'F', '2003-02-01',
                                             'Kimironko', '+234788888888', '2021 01 09', 1, 'AllieAn')

    def test_view_degree_program_outline(self):
        self.assertTrue(self.cs_student1.view_degree_program_outline())

    def test_promote_student(self):
        self.assertEqual(self.cs_student1.promote_student(), "Student is now in year 2")
        self.assertEqual(self.cs_student2.promote_student(), "The student is in his/her final year")

    def test_change_student_status(self):
        self.assertEqual(self.cs_student2.change_student_status(), "Student done is done with the degree program")
        self.assertEqual(self.cs_student1.change_student_status(), "Student will graduate on 2025-01-04 00:00:00")

    def test_print_student_information(self):
        self.assertEqual(self.cs_student1.print_student_information(),
'''Student information: 
Student email: a.ana@alustudent.com
Student name: Allie Ana
Gender: F
Date of birth: 2003-02-01
Address: Kimironko
Phone number: +234788888888
Major: Computer Science
Date of enrollment: 2021-01-09 00:00:00
Year:1
Status: Current
Internships:[]
Github username: AllieAn
Expected graduation date: 2025-01-04 00:00:00''')


if __name__ == '__main__':
    unittest.main()
