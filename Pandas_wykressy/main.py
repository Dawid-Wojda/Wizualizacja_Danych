import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# funkcja biblioteki pandas generujaca skumulowana sume kolejnych elementow
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# print(df)

# agg - proces laczenia w wieksza calosc
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
# # grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', rot=0, legend=True, title='Populacja z podziałem na kontynenty')
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Mld')
# wykres.legend()
# wykres.set_title('Populacja z podziałem na kontynenty')
# wykres.tick_params(axis='x', labelrotation=0)
# # zmiana kierunku tekstu etykiet słupków
# #plt.xticks(rotation=0)
# plt.savefig('wykres.png')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# # df = pd.DataFrame(read)
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']})
# #wykres kolumnowy z wartościami procentowymi sformatowanymi z dokładnością 2 miejsc po przecinku
# #figsize ustawia wielkość wykresu w calach domyślnie [6.4, 4.8]
# grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6,6), colors=['red', 'green'])
# #wykres = grupa.plot.pie(subplots=True,autopct='%.2f%%', fontsize=20, figsize=(6,6))
# plt.legend(loc='lower right')
# plt.title('Suma zamówien dla sprzedawcy')
# plt.show()

# df = pd.read_excel('imiona.xlsx')
# df1 = pd.DataFrame(df)
# print(df1)
# grupa = df1.groupby(['Rok']).agg({'Liczba': ['sum']})
# print(grupa)
# wykres = grupa.plot()
# wykres.set_xlabel('Rok')
# wykres.set_ylabel('Dzieci urodzne w danym roku')
# wykres.set_title('Urodziny dzieci do roku')
# plt.xticks([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017], rotation=90)
# plt.show()

# korzysajac z funkcji random oraz data_range możemy wygenerować szereg czasowy danych
# ts = pd.Series(np.random.randn(1000))
# #funkcja biblioteki Pandas generująca skumulowaną sumę kolejnych elementów
# ts = ts.cumsum()
# #rzutowanie Series na DataFrame
# df = pd.DataFrame(ts, columns=['wartości'])
# print(df)
#
# # dodanie nowej kolumny i wykorzystanie funkcji rolling do stworzenia kolejnych wartości średniej kroczącej
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

# df = pd.read_excel('imiona.xlsx')
# df1 = pd.DataFrame(df)
# grupa = df1.groupby(['Plec']).agg({'Liczba': ['sum']})
# print(grupa)
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Płeć')
# wykres.set_ylabel('Liczba chłopców i dziewczynek')
# wykres.set_title('Liczba urodzonych chłopców i dziewczynek')
# plt.show()

df = pd.read_excel('imiona.xlsx')
df1 = pd.DataFrame(df)
new_df = df.loc[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
print(new_df)
grupa = new_df.groupby(['Plec']).agg({'Liczba': ['sum']})
grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6,6), colors=['red', 'green'])
plt.show()

