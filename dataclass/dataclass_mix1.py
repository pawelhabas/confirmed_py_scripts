from dataclasses import dataclass, field

@dataclass
class Product:
  name: str = field(compare=True)  
  category: str = field(compare=True)
  unit_price: float = field(compare=False)
  tax_percent: float = field(compare=False) # To pole nie wpływa na porównania
  abstract_list_parametr: list = field(default_factory=list)  # Używamy default_factory dla mutable types
  #  Nie używaj default=[], bo wtedy wszystkie instancje będą miały tę samą listę!

  def __post_init__(self) -> None:
    if self.unit_price < 0:
      raise ValueError("unit_price attribute must be greater then zero.")

  @property
  def price_with_tax(self):
    return self.unit_price * self.tax_percent

  @price_with_tax.setter
    def price_with_tax(self, value: float):
        self.unit_price = value / (1 + self.tax_percent) 


def example_field_compare():
  """Przykład dla wyjaśnienia do czego służy argument field-compare"""
  p1 = Product("Laptop", "RTV", 3000, 0.08)
  p2 = Product("Tablet", "RTV", 1500, 0.23)
  p3 = Product("Laptop", "RTV", 2500, 0.08)
  
  print(p1 == p3)  # True, bo 'name' jest brane pod uwagę w porównaniach
  print(p1 < p2)   # Porównanie na podstawie 'name', bo 'price' ma compare=False

def example_decorator_property():
  """Dekorator @property pozwala odwołać się do wyliczanej w locie wartości, bez używania nawiasów.
  @price_with_tax.setter umożliwia przypisywanie wartości, jednoargumentowe """
  p = Product("Laptop", "RTV", 3000, 0.23)
  print(p.price_with_tax)  # 3690.0
  
  p.price_with_tax = 4000  # Ustawienie ceny brutto przeliczy cenę netto!
  print(p.price)  # 3252.03
