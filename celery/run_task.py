from tasks import add

# Wywołanie zadania Celery
result = add.delay(4, 6)
print(f"Zadanie wysłane. ID: {result.id}")

# Pobranie wyniku (opcjonalne)
print(f"Wynik: {result.get(timeout=10)}")