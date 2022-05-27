import pandas as pd
import numpy as np

# Series
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index = ['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
# print(s)

# DataFrame
# Tworzenie DataFrame na podstawie słownika
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brassillia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# DataFrame przechowuje typ dla każdej kolumny co możemy sprawdzić wpisując
# print(df.dtypes)
# możemy również w prosty sposób stworzyć serię danych - czyli próbki dla kolejnych dat, pomiarów czasu
# daty = pd.date_range('20210324', periods=5)
# print(daty)
# df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df)

# Biblioteka Pandas umożliwia również tworzenie DataFrame'ów z zewnętrznych źródeł danych
# CSV, odczyt i zapis
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=',')
# print(df)
# df.to_csv('plik.csv', index=False)

# Excel - wymagana jest biblioteka openpyxl
# df = pd.read_excel('dane.xlsx', header=0)
# print(df)
# df.to_excel('wyniki.xlsx', sheet_name="Arkusz pierwszy")

# Pobieranie danych ze struktur
# s = pd.Series([10, 12, 8 ,14], index = ['Ala', 'Marek', 'Wiesiek', 'Eeleonora'])
# print(s)
#
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', ],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)

# pojedynczy element serii, odnosimy się do nazwy indeksu
# print(s['Wiesiek'])
# Mozemy sie rowniez dostać do wartosci serii jak do pola klasy
# print(s.Wiesiek)

# pojedynczy element ramki danych, tak jak przy cięciu tablic, tylko tu jest oparte na indeksach
# print(df[0:1])
# print("")
# #kolumna po etykiecie
# print(df['Populacja'])
# pobieranie pojedynczej wartości po indeksie wiersza i kolumny
# print(df.iloc[0], [0])
# pobieranie wartosci po indeksie wiersza i etykiecie kolumny
# print(df.loc[[0], ["Kraj"]])
# print(df.at[0, "Kraj"])

# podobnie jak w przypadku serii można odwoływać się do kolumn jak do pół klasy
# dodatkowo print jest wywoływany jak w pętli dla każdego elemeentu ddanej kolumny
# print('kraj: ' + df.Kraj)

# Pandas posiada również funkcje pozwalające na losowe pobieranie elementów lub
# w odniesieniu do procentowej wielkości całego zbioru

# jeden losowy element
# print(df.sample())
# n losowych elementów
# print(df.sample(2))
# ilosc elementów procentowo, uwaga na zaokrąglenie
# print(df.sample(frac=0.5))

# jezeli potrzeba nam wiecej probek niz znajduje sie w zbiorze i dopuszczamy duplikaty to mozemy użyć parametru
# replace, który będzie losował z powtórzeniami
# print(df.sample(n=10, replace=True))

# zamiast wyświetlać całą kolekcje możemy wyświetlać cala kolekcje mozemy wyświetlić określoną ilość elementów od
# początku kolekcji lub od jej końca
# print("")
# print(df.head())
# print("")
# print(df.head(2))
# print("")
# print(df.tail(1))

# Pandas jest też w stanie wyświetlić statystykę dla wartości, które dana kolekcja zawiera, o ile są jakieś kolumny
# z danymi numerycznymi
# print(df.describe())
# transpozycja to zmienna T kolekcji, podobniee jak w numpy
# print(df.T)
# Filtrowanie, grupowanie i agregowanie danych
# s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
# print(s)
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brassillia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# Wyświetla dane z serii gdzie wartość większa od 9
# print(s[(s>9)])
# Nieco inny efekt mozna uzyskac wykorzystujac funkcje where, która zwraca kolekcję w oryginalnej wielkości
# (liczebności) elementów, ale wartości nie spełniające warunku uzupełnia wartością NaN
# print(s.where(s>10))
# Mozemy tez poddać wartosc, ktora zostanie podstawiona zamiast NaN
# print(s.where(s>10, 'za duze'))
# Jeszcze inna własność where pozwala na modyfikowanie oryginalnego zbioru(domyślnie zwracana jest kopia)
# seria = s.copy()
# seria.where(seria > 10, "ze duże", inplace=True)
# print("########")
# print(seria)

# Wyświetla dane z serii, gdzie wartość nie jest większa od 10
# print(s[(s>10)])
# Warunki możemy też łączyć
# print(s[(s<13) & (s>8)])

# Warunki dla pobierania DataFrame
# print(df[df['Populacja'] > 1200000000])
# bardziej skomplikowane warunki
# print(df[df.Populacja > 1000000 & (df.index.isin([0,2]))])
# inny przypaddek z lista dopuszczalnych wartossci oraz isin zwracajacych wartosci boolowsksie
# print('######')
# szukaj = ['Belgia', 'Brasilia']

# zmiana usuowanie i doddawanie danych

# w przypaddku serii mozemy ddodadc(zmienic wartosc przez odwolanie sie  do elementu serii przez klucz(indeks)
# s['Wiesiek'] = 15
# print(s.Wiesiek)
# s['Alan'] = 16
# print(s)

# Podobna operacja dla DataFrame ma nieco inny efekt - wartość ustawiona dla wszystkich kolumn
# df.loc[3] = 'dodane'
# print(df)
# ale moznaa doddac wiersz w postaci listy
# df.loc[4] = ['Polska', 'Warszawa', 38675467]
# print(df)
# usuawnie dadnych mozna wwykonac przez funkcje ddrop, ale pamietajmy ze operacja nie wykonuje sie in-place wiec
# zwracana jest kopa dataFrame z usunietymi wartościami
# new_df = df.drop([3])
# print(new_df)

# wiec jezeli chcemy zmienic pierwotny zbiór dodajemy parametr inlace = true
# df.drop([3], inplace=True)
# print(df)
# mozna rowniez usuawc cale kolumny po nazwie indesku, ale wykonanie tej komenddy uniemozliwwi wykonanie dalszego
# kodu (mozna przetestowawc po zakomentowaniu dalszej czesci listingu)
# df.drop('Kraj', axis=1, inplace=True)

# do DataFrame'ow mozemy dodawac rowniez kolumny zamiast wierszy
# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
# print(df)

# Pandas ma również własne funkcje sortowania danych
# print(df.sort_values(by = 'Kraj'))

# grupowania
# grouped = df.groupby(['Kontynent'])
# print(grouped.get_group('Europa'))
# #mozna tez rowniez tak jak w sql czy excelu uruchomic funkcje agregrujace na dadnej kolumnie
# print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}))

# LAB  6

# Zad 2

# df = pd.read_excel('imiona.xlsx', header=0)
# print(df)
# print(df.loc[df['Liczba'] > 1000])
# print(df.loc[df['Imie'] == 'DAWID'])
# print(df.Liczba.sum())
# print(df.loc[((df['Rok'] >= 2000) & (df['Rok'] <= 2005))].Liczba.sum())
# print(df.loc[(df['Plec'] == 'M')].Liczba.sum())
# print(df.loc[(df['Plec'] == 'K')].Liczba.sum())
# print(df.loc[df['Plec'].str.contains('M')].groupby(['Rok']).head(1))
# print(df.loc[df['Plec'].str.contains('K')].groupby(['Rok']).head(1))
# print(df.loc[df['Plec'].str.contains('M')].sort_values(by='Liczba', ascending=False).head(1))
# print(df.loc[df['Plec'].str.contains('K')].sort_values(by='Liczba', asceding=False).head(1))

# Zad 3

# df = pd.read_csv('zamowienia.csv', header=0, delimiter=';', decimal='.')
# df_zam = pd.read_csv('zamowienia.csv', sep=';', decimal='.')
# df_zam_u = df_zam.drop_duplicates(subset=['Sprzedawca'])
# for index, row in df_zam_u.iterrows():
#     print(index, row['Sprzedawca'])
# print(df.drop_duplicates(subset=['Sprzedawca']))
# print(df.sort_values(by='Utarg', ascending=False).head(5))
# df['count'] = 1
# print(df.groupby(['Sprzedawca']).count()['count'])
# print(df.loc[(df['Data zamowienia'].str.contains('2005') & (df['Kraj'] == 'Polska'))].Utarg.sum())
# print(df.loc[(df['Data zamowienia'].str.contains('2004'))].Utarg.mean())
# mean - średnia zapamiętać
# df_2004 = df.loc[df['Data zamowienia'].str.contains('2004')]
# df_2004.to_csv('rok2004')
# df_2005 = df.loc[df['Data zamowienia'].str.contains('2005')]
# df_2005.to_csv('rok2005')
