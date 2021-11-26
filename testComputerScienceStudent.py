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

    # def test_change_student_status(self):
    #     self.assert
    #     pass


if __name__ == '__main__':
    unittest.main()
