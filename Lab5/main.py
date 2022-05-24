import numpy as np

# #inicjacja danych
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# print(a)
# print(b)
# #Wykonujemy operacje i zapisujemy do nowej zmiennej
# c = a - b
# print(c)
# #Wykonujemy operację kawdrat zawartości
# print(b ** 2)
# #Modyfikacja obecnych zmiennych
# print(a)
# a += b
# print(a)
# a -= b
# print(a)

# a = np.arange(12).reshape((3, 4))
# print(a)
# # Suma całej macierzy
# print(a.sum())
# #suma każdej z kolumn
# print(a.sum(axis = 0))
# #minimum każdego rzędu
# print(a.min(axis = 1))
# #skumulowawna asuma dla rzedu
# print(a.cumsum(axis = 1))

# Inicjacja ddanych
# a = np.arange(3)
# b = np.arange(3)
# print(a)
# print(b)
# print(a * b)
# print(a.dot(b))
# print(np.dot(a,b))

# #macierz całkowita
# a = np.ones(3, dtype='int32')
# print(a.dtype)
# #Macierz zmiennoprzecinkowa
# b = np.linspace(0, np.pi, 3)
# print(b)
# print(b.dtype)
#
# c = a + b
# print(c)
# print(c.dtype)
# #Wynikiem jest macierz liczb zespolonych
# d = np.exp(c * 1j)
# print(d)
# print(d.dtype)

# b = np.arange(3)
# print(b)
# print(np.exp(b))
# print(np.sqrt(b))
# c = np.array([2., -1., 4.])
# print(np.add(b,c))

# generujemy macierz 3x2
# a = np.arange(6).reshape((3, 2))
# print(a)
# print("\n")
# for b in a:
#     #iterujemy wzdluz 1 osi
#     print(b)
#     print("")

# a = np.arange(6).reshape((3,2))
# print(a)
# for b in a.flat:
#     #iterujemy jakby macierz była płaska
#     print(b)
#     print("")

# generujemy macierz 1x6
# a = np.arange(6)
# print(a)
# print(a.shape)
#
# b = np.array([np.arange(3), np.arange(3), np.arange(3)])
# print(b)
# print(b.shape)

# a = np.arange(6)
# print(a)
# print(a.shape)
# print(" ")
# przeksztalcamy ja na macierz 2x3
# b = a.reshape((2, 3))
# print(b)
# print(b.shape)
# print(" ")
# przekształcamy ją na macierz 3x2
# c = b.reshape((3, 2))
# print(c)
# print(c.shape)
# print(" ")

# splaszczamy macierz zyskujac pierwwotny ksztalt ze zmiennej a
# d = c.ravel()
# print(d)
# print(d.shape)
# print(" ")
# transpozycja macierzy
# e = b.T
# print(e)
# print(e.shape)

# LAB 5


# Zad 1
# a = np.array([1, 2, 3])
# b = np.array([5, 9, 12])
# c = a*b
# print(c)

# Zad 2
# a = np.array([[0, 5, 8], [7, 9, 18], [25, 14, 28]])
# print(a)
# print("\n")
# print(a.min(axis = 0))
# print(a.min(axis = 1))

# b = np.array([[53, 21, 59], [1, 0, 28], [79, 3, 22], [0, 3, 2]])
# # print(b)
# # print(" ")
# # print(b.min(axis = 0))
# # print(b.min(axis = 1))

# Zad 3
# c = a.dot(b)
# print(c)

# Zad 4
# a = np.array([5, 23, 51])
# b = np.array([[np.sqrt(5), 1.25, -2]])
# c = a*b
# print(c)

# Zad 5
# z1 = np.arange(1, 12, 2)
# z1 = z1.reshape(2, 3)
# a = np.sin(z1)
# print(a)
# print(" ")

# Zad 6
# z2 = np.arange(1, 7)
# z2 = z2.reshape(2, 3)
# b = np.cos(z2)
# print(b)

# Zad 7
# print(" ")
# z3 = a+b
# print(z3)

# Zad 8
# a = np.arange(9).reshape((3, 3))
# print(a)
# for x in a:
#     print(x)
#     print(" ")

# Zad 9
# a = np.arange(9).reshape(3, 3)
# for x in a.flat:
#     print(x)
#     print(" ")

# a = np.arange(81).reshape((9, 9))
# b = a.reshape(3, 27)
# c = a.reshape(27, 3)
# e = a.reshape(1, 81)
# f = a.reshape(81, 1)
# print(b)
# print(c)
# print(e)
# print(f)

# Mamy takie możliwości poniewaaz liczba kolumny i wierszy pomnozona musi dawać 81.

# Zad 11

# a = np.arange(12)
# b = a.reshape(3, 4)
# c = a.reshape(4, 3)
# d = a.reshape(2, 6)
#
# for x in b.flat:
#     print(x)
#     print(" ")
#
# for x in c.flat:
#     print(x)
#     print(" ")
#
# for x in d.flat:
#     print(x)
#     print(" ")
