import student_management
import unittest

class StudentManagementTest(unittest.TestCase):
    def test_add_student_to_empty_list(self):
        res = student_management.add([], 5, "Olle")
        self.assertEqual(res, [{ "id": 5, "name": "Olle" }])

    def test_display(self):
        student = student_management.display([
            { "id": 5, "name": "Olle" },
            { "id": 6, "name": "Pelle" }
        ], 7)
        self.assertEqual(student, { "id": 5, "name": "Olle"})

if __name__ == '__main__':
    unittest.main()