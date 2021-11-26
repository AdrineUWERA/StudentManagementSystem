import unittest
from international_business_and_trade_student_class import InternationalBusinessAndTradeStudent


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ibt_student1 = InternationalBusinessAndTradeStudent("a.ana@alustudent.com", "Allie Ana", "F",
                                                                "2003 - 02 - 01",
                                                                "Kimironko", "+234788888888", "2020 11 26", 1)
        self.ibt_student2 = InternationalBusinessAndTradeStudent("b.ana@alustudent.com", "Allie Ana", "F",
                                                                "2003 - 02 - 01",
                                                                "Kimironko", "+234788888888", "2018 11 26", 3)

    @staticmethod
    def test__init__():
        ibt_student3 = InternationalBusinessAndTradeStudent("c.ana@alustudent.com", "Allie Ana", "F", "2003 - 02 - 01",
                                                           "Kimironko", "+234788888888", "2020 11 26", 1)

    def test_view_degree_program_outline(self):
        self.assertTrue(self.ibt_student1.view_degree_program_outline())

    def test_promote_student(self):
        self.assertEqual(self.ibt_student1.promote_student(), "Student is now in year 2")
        self.assertEqual(self.ibt_student2.promote_student(), "The student was in his/her final year.")

    def test_change_student_status(self):
        self.assertEqual(self.ibt_student1.change_student_status(), "Student will graduate 2023-11-23 00:00:00")
        self.assertEqual(self.ibt_student2.change_student_status(), "The student is done with the degree program!")

    def test_print_student_information(self):
        self.assertEqual(self.ibt_student1.print_student_information(),
'''Student information: 
Student email: a.ana@alustudent.com
Student name: Allie Ana
Gender: F
Date of birth: 2003 - 02 - 01
Address: Kimironko
Phone number: +234788888888
Major: International Business And Trade
Date of enrollment: 2020-11-26 00:00:00
Year:1
Status: Current
Internships:[]
Venture:[]
Expected graduation date:2023-11-23 00:00:00''')

    def test_add_venture_details(self):
        self.assertEqual(self.ibt_student1.add_venture_details(), "Venture added successfully!")


if __name__ == '__main__':
    unittest.main()