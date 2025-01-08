current_year = int(input("Vad är nuvarande år?\n"))
birth_year = int(input("Vilket år föddes du?\n"))

age = current_year - birth_year

print(f"Du är {age} år gammal")

# age variabeln är som en låda, förenkla. två lådor, inte fler rader



x = 5
y = 10
z = 15
print((x > y and x < z) or y <= z)


""" Fråga 3 (10 poäng)

Skriv ett program som ber användaren om deras 
ålder och priset på varan. Sedan räknar programmet ut 
rabatten baserat på åldern:

- Under 18 år: 20% rabatt
- Mellan 18 och 65 år: 0% rabatt
- Över 65 år: 30% rabatt

Tips: Använd
- input() och int()
- 0.8 * price = 80% of price (20% rabatt)

Exempel:
> Hur gammal är du?
15
> Vad kostar varan?
100
> Du betalar 80 kr""" 


age = int(input("Hur gammal är du?\n"))
price = int(input("Vad kostar varan?\n"))
if (age < 18):
    print("Du betalar",  0.8*price)
elif (age >= 18 and age <= 65):
    print("Du betalar" ,  0*price)
else:
    print("Du betalar" , 0.7*price)
