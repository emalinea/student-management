import student_management
import unittest

class StudentManagementTest(unittest.TestCase):
    def test_add(self):
        res = student_management.add([], 5, "Olle", 20, "A", "Math", "Chemistry")
        self.assertEqual(res, [{ "id": 5, "name": "Olle", "age": 20, "grade": "A", "subjects": "Math", "Chemistry" }])

    def test_display(self):
        student = student_management.display([
            { "id": 5, "name": "Olle" },
            { "id": 6, "name": "Pelle" }
        ], 7)
        self.assertEqual(student, { "id": 5, "name": "Olle", "age": 20, "grade": "VG", "subjects": "Math, Chemistry"})    

if __name__ == '__main__':
    unittest.main()