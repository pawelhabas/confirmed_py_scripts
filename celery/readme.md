Celery worker to komponent frameworka Celery służący do asynchronicznego przetwarzania zadań w tle. Celery umożliwia obsługę zadań w kolejce (message queue), takich jak RabbitMQ czy Redis, i delegowanie ich do workerów. Worker to proces, który pobiera zadania z kolejki i wykonuje je w niezależny sposób, co pozwala odciążyć główną aplikację. Jest szczególnie przydatny w aplikacjach wymagających dużej liczby operacji I/O lub intensywnych obliczeń. Dzięki skalowalności można uruchamiać wiele workerów, co zwiększa wydajność systemu.

Przykład wdrożenia Celery:

Instalacja:

pip install celery[redis]

Plik tasks.py:

from celery import Celery

# Konfiguracja Celery z backendem Redis
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Definicja zadania
@app.task
def add(x, y):
    return x + y

Plik run_task.py:

from tasks import add

# Wywołanie zadania Celery
result = add.delay(4, 6)
print(f"Zadanie wysłane. ID: {result.id}")

# Pobranie wyniku (opcjonalne)
print(f"Wynik: {result.get(timeout=10)}")

Uruchamianie:

1. Uruchom Redis (np. redis-server).


2. Uruchom workera Celery:

celery -A tasks worker --loglevel=info


3. Wykonaj skrypt run_task.py.



Worker przetworzy zadanie asynchronicznie i wynik zostanie zapisany w Redis, gotowy do pobrania.

