nimi = str(input("Sisestage oma nimi: "))
lubatud = str(input("Sisestage lubatud kiirus: "))
tegelik = str(input("Sisestage tegelik kiirus: "))
summa = (int(tegelik) - int(lubatud)) * 3
print(f"{nimi} kiiruse ületamise trahv on {summa} euri")
