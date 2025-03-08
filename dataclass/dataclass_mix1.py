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



def example_field_compare():
  """Przykład dla wyjaśnienia do czego służy argument field-compare"""
  p1 = Product("Laptop", "RTV", 3000, 8)
  p2 = Product("Tablet", "RTV", 1500, 23)
  p3 = Product("Laptop", "RTV", 2500, 8.5)
  
  print(p1 == p3)  # True, bo 'name' jest brane pod uwagę w porównaniach
  print(p1 < p2)   # Porównanie na podstawie 'name', bo 'price' ma compare=False
