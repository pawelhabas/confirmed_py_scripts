from PyQt5.QWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys

class MyWindow(QWidget):

  def __init__(self):
    super().__init__()
    
    # Ustawienie pozycji i wymiarów (pozycja x,y, wymiary x,y)
    self.setGemometry(100,100, 800,600) 
    
    # Ustawienie tytułu okna
    self.setWindowTitle("Tytuł okna")
    
    # Ustawienie ikony dla okna
    self.setWindowIcon(QIcon("myIcon.png"))
    
    # Ustawienie wymiarów okna na stałe - bez możliwości resize okna
    self.setFixedHeight(400)
    self.setFixedWidth(300)
    
    # Ustawienie przezroczystości okna
    self.setWindowOpacity(0.5)
    
    # Ustawienie parametrów graficznych okna, np. kolor tła
    self.setStyleSheet("background-color:green")
    
    
    self.show()
    
app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
