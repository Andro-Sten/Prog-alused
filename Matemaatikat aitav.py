def mata_aitaja():
    print("Tere tulemast minu matemaatikat õpetavasse programmi!")
    print("Mida tahate õppida täna?")
    print("1. Liitmist")
    print("2. Lahutamist")
    print("3. Korrutamist")
    print("4. Jagamist")

    valik = input("Vali vastav number sellele, mida tahad õppida: ")

    if valik == "1":
        print("Harjutame liitmist.")
        num1 = int(input("Sisesta üks number: "))
        num2 = int(input("Sisesta veel üks number: "))
        result = num1 + num2
        print("Vastuseks on: " + str(result))

    elif valik == "2":
        print("Harjutame lahutamist.")
        num1 = int(input("Sisesta üks number: "))
        num2 = int(input("Sisesta veel üks number: "))
        result = num1 - num2
        print("Vastuseks on: " + str(result))

    elif valik == "3":
        print("Harjutame korrutamist.")
        num1 = int(input("Sisesta üks number: "))
        num2 = int(input("Sisesta veel üks number: "))
        result = num1 * num2
        print("Vastuseks on: " + str(result))

    elif valik == "4":
        print("Harjutame jagamist.")
        num1 = int(input("Sisesta üks number: "))
        num2 = int(input("Sisesta veel üks number: "))
        result = num1 / num2
        print("Vastuseks on: " + str(result))

    else:
        print("Kehtetu sisend. Palun proovi uuesti")
        mata_aitaja()


mata_aitaja()