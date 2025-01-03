# Przykłady wykorzystania Beautiful Soup

## 1. Pobieranie i analizowanie tytułu strony
```python
from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Pobranie tytułu strony
title = soup.title.string
print("Tytuł strony:", title)
```

## 2. Pobieranie wszystkich linków na stronie
```python
for link in soup.find_all('a'):
    href = link.get('href')
    print(href)
```

## 3. Wyszukiwanie elementów za pomocą selektorów CSS
```python
# Wybieranie elementów za pomocą klasy
elements = soup.select('.example-class')
for element in elements:
    print(element.text)
```

## 4. Pobieranie tabeli danych
```python
# Znalezienie tabeli na stronie
table = soup.find('table')

# Pobranie wszystkich wierszy z tabeli
rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    data = [col.text.strip() for col in columns]
    print(data)
```

## 5. Filtrowanie na podstawie atrybutów
```python
# Znalezienie obrazków z określonym atrybutem 'alt'
images = soup.find_all('img', alt=True)
for img in images:
    print(img['src'], img['alt'])
```

## 6. Pobieranie nagłówków (np. h1, h2, h3)
```python
# Pobranie wszystkich nagłówków h1
headers = soup.find_all('h1')
for header in headers:
    print(header.text)
```

## 7. Wyszukiwanie z użyciem wyrażenia regularnego
```python
import re

# Wyszukiwanie elementów, których tekst pasuje do wzorca
matches = soup.find_all(string=re.compile('Python'))
for match in matches:
    print(match)
```

## 8. Zmiana struktury HTML
```python
# Dodanie nowego elementu
new_tag = soup.new_tag("p")
new_tag.string = "To jest nowy paragraf."
soup.body.append(new_tag)

print(soup.prettify())
```

## 9. Zapis zaktualizowanego HTML do pliku
```python
# Zapisanie zmodyfikowanego HTML
with open("updated.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
```

## 10. Usuwanie elementów z drzewa HTML
```python
# Usunięcie wszystkich elementów z klasą 'remove-me'
for element in soup.select('.remove-me'):
    element.decompose()

print(soup.prettify())
```
