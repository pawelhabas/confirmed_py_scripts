from celery import Celery

# Konfiguracja Celery z backendem Redis
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Definicja zadania
@app.task
def add(x, y):
    return x + y