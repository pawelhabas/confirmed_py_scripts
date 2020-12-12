#   Funkcje PyAutoGui
import pyautogui 
import time
import datetime

class Pag:
    # klasa do funkcji PyAutoGui
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True
    NR_ID = {}

    def __init__(self):
        self.NR_ID = {}
    
    def czas(self):
        #   Zwraca aktualną datę i czas w ustalonym formacie
        teraz = datetime.datetime.now()
        godzina = str(teraz.hour)
        minuta = str(teraz.minute)
        sekunda = str(teraz.second)
        if int(godzina) < 10:
            godzina = '0' + str(godzina)
        if int(minuta) < 10:
            minuta = '0' + str(minuta)
        if int(sekunda) < 10:
            sekunda = '0' + str(sekunda)
        mes = '{0:2s}:{1:2s}:{2:2s} - '
        return mes.format(godzina, minuta, sekunda)

    def move(self,tm, x, y, opis):
        #   Wypisuje w konsoli opis, po określonym czasie tm, przesuwa wskaźnik na koordy(x,y), wykonuje pojedynczy click
        print(self.czas(),str(opis))
        if tm > 0:
            time.sleep(int(tm))
        pyautogui.moveTo(int(x), int(y), 0.5)
        pyautogui.click()

    def wpisz(self,tm, txt, opis):
        #   Wypisuje w konsoli opis, po określonym czasie tm, wypisuje w aktualnym miejscu txt
        print(self.czas(),str(opis))
        if tm > 0:
            time.sleep(int(tm))
        pyautogui.write(txt, interval=0.1)

    def pobierz_tekst(self,tm, pole, **opisy):
        #   Wypisuje w konsoli opis, po określonym czasie tm, do self.NR_ID[pole] pobiera tekst oknem prompt(txt = 'Treść pytania', tytul='Tytuł okna', deff = 'Wartość domyślna')
        print(self.czas(),str(opisy['opis']))
        if tm > 0:
            time.sleep(int(tm))
        self.NR_ID[pole] = pyautogui.prompt(text=opisy['txt'], title=opisy['tytul'] , default=opisy['deff'])

# pg = Pag()
# pg.pobierz_tekst(0,'test',txt = 'Treść', tytul='Tytuł', deff = '',opis = 'Opis testowy')
# pg.wpisz(1,pg.NR_ID['test'],'Opis test')
# pg.move(2,800,600,'Opis test')
