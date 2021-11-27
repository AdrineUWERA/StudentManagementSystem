import unittest
from global_challenges_student import GlobalChallengesStudent


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.gc_student1 = GlobalChallengesStudent('m.don@alustudent.com', 'Marion Don', 'F', '2003-02-01',
                                                   'Kimironko', '+234788638856', '2020 01 01', 1, 'Health')
        self.gc_student2 = GlobalChallengesStudent('M.jimmy@alustudent.com', 'Jimmy Max', 'M', '2000-07-03',
                                                   'Gikondo', '+250789888876', '2018 01 01', 3, 'Education')

    @staticmethod
    def test__init__():
        gc_student1 = GlobalChallengesStudent('m.don@alustudent.com', 'Marion Don', 'F', '2003-02-01',
                                              'Kimironko', '+234788638856', '2020 01 01', 1, 'Health')

    def test_view_degree_program_outline(self):
        self.assertTrue(self.gc_student1.view_degree_program_outline())

    def test_promote_student(self):
        self.assertEqual(self.gc_student1.promote_student(), "Student is now in year 2")
        self.assertEqual(self.gc_student2.promote_student(), "The student is in his/her final year")

    def test_change_student_status(self):
        self.assertEqual(self.gc_student2.change_student_status(), "Student done is done with the degree program")
        self.assertEqual(self.gc_student1.change_student_status(), "Student will graduate on 2022-12-28 00:00:00")

    def test_print_student_information(self):
        self.assertEqual(self.gc_student1.print_student_information(),
'''Student information: 
Student email: m.don@alustudent.com
Student name: Marion Don
Gender: F
Date of birth: 2003-02-01
Address: Kimironko
Phone number: +234788638856
Major: Global Challenges
Date of enrollment: 2020-01-01 00:00:00
Year:1
Status: Current
Internships:[]
Mission: Health
Expected graduation date: 2022-12-28 00:00:00''')


if __name__ == '__main__':
    unittest.main()
