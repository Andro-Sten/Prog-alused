# Importin random mooduli, et saada juhuslikke numbreid.
import random

# Defineerin mitu probleemi on ja kõige suurema numbri
num_problems = 10
min_num = 1
max_num = 30
probleemid = ["+", "-", "*",]

# Jätan meelde õiged vastused
num_correct = 0

# Esitada probleemid ja kontrollida vastuseid
for i in range(num_problems):
  # Generate two random numbers
  a = random.randint(min_num, max_num)
  b = random.randint(min_num, max_num)
  vm = random.choice(probleemid)

  # Küsin kasutajalt tehte lahendust
  print(f"Mis on {a} {vm} {b}?")
  answer = float(input())

  # Vaatan kas lahendus on õige ja pean järge mitu on õigesti pandud.
  if vm == "+":
    correct_answer = a + b
  elif vm == "-":
    correct_answer = a - b
  elif vm == "*":
    correct_answer = a * b

    if abs(answer - correct_answer) < 1e-6:
       print("Õige! Hästi tehtud!")
       num_correct += 1
    else:
       print(f"Vabandust, õige vastus on {correct_answer}.")

# Lõpptulemus
print(f"Sa said {num_correct} {num_problems} tehtest õigesti.")