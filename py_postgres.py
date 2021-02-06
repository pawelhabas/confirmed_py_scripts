#   Basic operations PY <-> PostgreSQL

import psycopg2 #   podstawowa biblioteka
import psycopg2.extras  #   biblioteka do wyświetlania/ wyszukiwania po nazwach kolumn
#   połączenie
postgres_connection = psycopg2.connect(dbname = 'baza', user='user', password='pass', host='localhost', port=5432)

#   ustawienie kursora
postgres_cursor = postgres_connection.cursor()
postgres_cursor2 = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

#   Wykonanie zapytania tworzącego, aktualizującego
postgres_cursor.execute("CREATE TABLE tabela (is SERIAL PRIMARY KEY, kolumna1 VARCHAR, kolumna2 INT);")
postgres_cursor2

#   Zatwierdzenie zmian
postgres_connection.commit()

#   Pobranie danych z tabeli
postgres_cursor.execute("SELECT * FROM tabela;")

#   przypisanie wyniku do listy
wynik = postgres_cursor.fetchall()
wynik2 = postgres_cursor2.fetchall()['id']

#   przypisanie jednego rekordu do zmiennej
wynik_1 = postgres_cursor.fetchone()
wynik2_1 = postgres_cursor2.fetchone()['id']

#   zakonczenie połączenia
postgres_connection.close()
