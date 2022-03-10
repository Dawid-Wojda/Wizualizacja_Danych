import math
#zad1
# zSporty = ["Rugby","Mma","Siłownia"]
# zSporty.reverse()
# zSporty.append("Koszykówka")
# zSporty.append("Boks")
# zSporty.append("Pływanie")

#zad2

#zSkroty = {"OMG":"Oh my God","RN":"Right now","BTW":"By the way","IMO":"In my opinion","IDK":"I don't know"}

#zad3

# zGry = {"Mass Effect":"BioWare","Wiedzmin 3":"CD Projekt","Dying Light":"Warner Bros","League Of Legends":"Riot Games"}
# print("Liczba gier = " + str(len(zGry)))

#zad4

# zZdanie = input("Podaj zdanie: ")
# print("litera a wstąpiła w tym zdaniu " + str(zZdanie.count('a')) + " razy")

#zad6

# tablica = [0] * 3
# tablica[0] = int(input("1 liczba: "))
# tablica[1] = int(input("2 liczba: "))
# tablica[2] = int(input("3 liczba: "))
# z = tablica[0]
# for element in tablica:
#     if(z < element):
#         z = element
# print("Największą liczbą jest: " + str(z))

#zad7

# Liczby = [5,2.5,9,12,1.33,120]
# for i in range(len(Liczby)):
#     Liczby[i] = math.pow(Liczby[i],2)
# print(Liczby)

#zad8
# Liczby2 = [0]*10
# i=0
# wynik=0
# while i < 10:
#     Liczby2[i] = int(input("Podaj " + str(i+1) + " liczbę:"))
#     i = i+1
# for x in Liczby2:
#     if(x%2==0):
#         wynik = wynik+x
# print("Suma parzystych liczb wynosi: "+str(wynik))

#zad9

# pierwiastek = float(input("Podaj liczbę do spierwiastkowania: "))
# try:
#     print("Pierwiastek wynosi: " +  str(math.sqrt(pierwiastek)))
# except ValueError:
#       print("Wprowadzona liczba jest niewłaściwa")
