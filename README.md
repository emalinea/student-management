Hur man kör systemet lokalt:
1. Klona repo med rätt url från Github: 'git clone <repository_url>'.
2. Gå till projektmappen 'cd <projektmapp>.
3. Installera 'pip install -r requirements.txt'.
4. Kör systemet: 'python student_management.py'


Hur man testar systemet lokalt:
1. Gå till 'test'-branchen genom att ange: 'git checkout test'. 
2. Kör tester: 'python -m unittest student_management_test.py'.
3. Kontrollera testresultatet.


Arbetsflöde för att merga mellan brancherna (test -> dev -> main)
1. Arbeta och pusha i dev-branchen.
2. Pusha till test-branchen och kör tester där.
3. Merga från test-branch till dev-branch när testerna har genomförts utan error/failure där det enbart står OK.
4. Merga dev-branch till main-branch när filerna är testade och stabila. 

