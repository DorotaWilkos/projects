import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#wczytywanie pliku z danymi
df = pd.read_csv(r"C:\Users\dorot\Downloads\bank.csv", sep=';')

#wyświetlanie podstawowych informacji o kolumnach z tabeli danych
print(df.info())

#wyświetlanie 10 pierwszych wierszy tabeli z danymi (T oznacza transponowane - tytuły i wiersze wyświetlane są nie pod sobą a w poziomie)
df.head(10).T

#wyświetlenie podstawowych informacji o wartościach liczbowych w tabeli (można tu wykryć anomalie albo zauważyć jakieś prawidłowe ale nietypowe dane jak np najstarsza osoba której oferowano lokatę miała 98 lat)
df.describe().T

# Sprawdzenie pustych i nieprawidłowych wartości wartości

#zamiana wartości "unknown" (występują w danych) na wartość rozpoznawaną przez pandas jako wartość pusta
df.replace('unknown', np.NAN , inplace=True)

#wyświetlenie zestawienia ile brakuje danych i w jakich kolumnach
df.isnull().sum()

print(f"Łącznie brakuje {df.isnull().sum().sum()} warości")

#czyszczenie danych
before_cleaning = df.shape[0]

#usuwanie pustych wartości (w tym wartości NaN)
df.dropna(axis='index',inplace=True)
after_cleaning = df.shape[0]

print(f"Przed czyszczeniem: {before_cleaning} wierszy")
print(f"Po czyszczeniu: {after_cleaning} wierszy")
print(f"Usunięto: {before_cleaning - after_cleaning} wierszy")

#sprawdzanie czy występują zduplikowane wiersze
print(f"Liczba wierszy ze zduplikowanymi danymi: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)

print(f"Ostateczna liczba wierszy po oczyszczeniu danych: {df.shape[0]}")

def all_linear_by_column(column_name, xlabel, title):
    df_temp = df
    df_temp = df_temp.set_index(column_name)
    df_temp = df_temp.groupby(column_name)['y'].count()

    # tworzenie wykresów
    plt.figure(figsize=(14, 8))
    plt.plot(df_temp)
    plt.grid()
    plt.xlabel(xlabel)
    plt.title(title)
    plt.ylabel('liczba klientów')


# funkcja rysująca wykres liniowy (2 linie)
def compare_linear_by_column(column_name, xlabel, title):
    # dane 1
    yes = df[df["y"].str.contains("yes")]
    yes = yes.set_index(column_name)
    yes = yes.groupby(column_name)['y'].count()

    # dane 2
    no = df[df["y"].str.contains("no")]
    no = no.set_index(column_name)
    no = no.groupby(column_name)['y'].count()

    # tworzenie wykresów
    plt.figure(figsize=(14, 8))
    plt.plot(yes, label="otworzono lokatę")
    plt.plot(no, label="nie skorzystano z oferty")
    plt.legend()
    plt.grid()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('liczba klientów')

    plt.show()

#funkcja rysująca wykres pierścieniowy
def ring_chart(column_name, labels, title):
    # wybranie kolumny z danymi
    yr = df[column_name].value_counts()
    # rysowanie wykresów
    plt.figure(figsize=(6, 5))
    plt.pie(yr, labels=labels)
    # dodanie koła w środku,
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.title(title)
    plt.show()

all_linear_by_column('age','wiek','wiek osób uczestniczących w kampani')
compare_linear_by_column('age','wiek','lokata/wiek')
ring_chart('y',['Klienci którzy nie otworzyli lokaty','Klienci którzy założyli lokatę w banku'], "Wyniki kampanii marketingowej banku")


