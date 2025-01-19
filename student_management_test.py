# byter funktion varje gång för att testa
# göra med testnamn som inte finns


import student_management
import unittest

class StudentManagementTest(unittest.TestCase):
    def test_addStudent(self):
        res = student_management.add([], 3, "Olle")
        self.assertEqual(res, [{ "id": 3, "name": "Olle" }])

    def test_displayStudent(self):
        student = student_management.display([
            { "id": 3, "name": "Olle" }, 
            { "id": 8, "name": "Charles" }
        ], 7)
        self.assertEqual(student, { "id": 3, "name": "Olle" })

if __name__ == '__main__':
    unittest.main()       
