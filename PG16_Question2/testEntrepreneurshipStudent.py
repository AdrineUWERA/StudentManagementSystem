import unittest
from entrepreneurship_student_class import EntrepreneurshipStudent


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ent_student1 = EntrepreneurshipStudent("K.rema@alustudent.com", "Kuma Rema", "M", "2000-05-08",
                                                    "Kabeza", "+242788786299", "2020-11-26", 1)
        self.ent_student2 = EntrepreneurshipStudent("l.rema@alustudent.com", "Kuma Rema", "M", "2000-05-08",
                                                    "Kabeza", "+242788786299", "2019-11-26", 2)

    @staticmethod
    def test__init__():
        ent_student3 = EntrepreneurshipStudent("m.rema@alustudent.com", "Kuma Rema", "M", "2000-05-08",
                                               "Kabeza", "+242788786299", "2019-11-26", 2)

    def test_view_degree_program_outline(self):
        self.assertTrue(self.ent_student1.view_degree_program_outline())

    def test_promote_student(self):
        self.assertEqual(self.ent_student1.promote_student(), "Student is now in year 2")
        self.assertEqual(self.ent_student2.promote_student(), "The student was in his/her final year.")

    def test_change_student_status(self):
        self.assertEqual(self.ent_student1.change_student_status(), "Student will graduate 2022-11-24 00:00:00")
        self.assertEqual(self.ent_student2.change_student_status(), "The student is done with the degree program!")

    def test_print_student_information(self):
        self.assertEqual(self.ent_student1.print_student_information(),
'''Student information: 
Student email: K.rema@alustudent.com
Student name: Kuma Rema
Gender: M
Date of birth: 2000-05-08
Address: Kabeza
Phone number: +242788786299
Major: Entrepreneurship
Date of enrollment: 2020-11-26 00:00:00
Year:1
Status: Current
Internships:[]
Venture:[]
Expected graduation date:2022-11-24 00:00:00''')

    def test_add_venture_details(self):
        self.assertEqual(self.ent_student1.add_venture_details(), "Venture added successfully!")


if __name__ == '__main__':
    unittest.main()
