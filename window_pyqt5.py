# #!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QButtonGroup
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtWidgets import QPlainTextEdit  
from PyQt5.QtCore import Qt

class MyWindow(QWidget):

    przyciski = []
    przyciski.append({'nazwa':'Nazwa przycisku','enable':True})
    buttons = []
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        #   Utworzenie układu tabelarycznego
        ukladT = QGridLayout()
        #   przyciski
        for i in range(0,len(self.przyciski)):
            self.buttons.append(QPushButton(self.przyciski[i]['nazwa'], self))
            self.buttons[i].setEnabled(self.przyciski[i]['enable'])
            ukladT.addWidget(self.buttons[i], i, 0)

        #   pola tekstowe
        self.ta_main = QPlainTextEdit(self)

        #   Ustawienie parametrów pól
        self.ta_main.setReadOnly(True)
        self.ta_main.resize(1180,600)
        self.ta_main.insertPlainText("Start")

        ukladT.addWidget(self.ta_main, 0, 1, len(self.buttons),3)
        
        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        self.setGeometry(50, 50, 1200, 800)      #  OKNO (pozycja X, pozycja Y, wielkość x, wielkość y)
        self.setWindowTitle("Okno Window")

        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        for but in self.buttons:
            self.btn_grp.addButton(but)

        self.btn_grp.buttonClicked.connect(self.on_click)

        self.show()

    def on_click(self, btn):
        self.ta_main.clear()
        self.ta_main.appendPlainText(str(btn.text()))

    def koniec(self):
        self.close()
    
    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = MyWindow()
    sys.exit(app.exec_())
