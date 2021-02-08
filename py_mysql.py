#   Basic operations PY <-> PostgreSQL

import mysql.connector

db = mysql.connector.connect(
    host = "serwer_host",
    user = "db_user",
    passwd = "db_pass",
    database = "db_name"
)
# Ustawienie kursora
mycursor = db.cursor()

# Pobranie wszystkich tabel
mycursor.execute("SHOW TABLES")

# Pobranie opisu konkretnej tabeli
mycursor.execute("DESC table1")

# Przygotowanie zapytania dodającego do bazy
Q1 = "INSERT INTO table1 (data, tresc) VALUES (%s, %s)"

# Wykonanie zapytania dodającego
mycursor.execute(Q1, ('2021-02-08','test'))

# Zatwierdzenie wprowadzenia zmian 
# UWAGA Commit robimy na zmiennej bazowej 'db' a nie na kursorze
db.commit()

# Pobranie wszystkich rekordów z bazy
mycursor.execute("SELECT * FROM table1")

# Uniwersalne ypisanie wyników
for x in mycursor:
  print(x)
  
