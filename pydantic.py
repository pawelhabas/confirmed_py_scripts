from pydantic import BaseModel, ValidationError, Field
from typing import List, Optional
from datetime import datetime

# Definicja modelu danych
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True  # Domyślna wartość
    friends: Optional[List[int]] = []  # Lista ID znajomych, może być pusta
    signup_date: datetime = Field(default_factory=datetime.utcnow)  # Automatyczna wartość

# Dane wejściowe
input_data = {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "friends": [2, 3, 4]
}

# Walidacja i parsowanie
try:
    user = User(**input_data)
    print(user)
except ValidationError as e:
    print("Błąd walidacji:", e)

# Dane wyjściowe (serializacja)
print(user.dict())  # Konwersja do słownika