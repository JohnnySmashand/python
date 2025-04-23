# #tworzenie klas 

# #zad1
# class Samochod:
    
#     def __init__(self, marka: str, model: str, rok: int):
#         self.marka = marka #gdybym chciala atrybut prywatny to robie tak: self.__marka = marka
#         self.model = model
#         self.rok = rok

#     def opis(self) -> str:
#         return f"{self.marka} {self.model} z roku {self.rok}"

#     def __repr__(self) -> str:
#         return self.opis()

# SamochodExample = Samochod("Opel", "Astra", 2000)
# SamochodExample2 = Samochod("marka", "model", 2001)

# print(SamochodExample)
'''
1. 
tworzymy sobie klasę o nazwie samochod (troche jak przepis na ciasto)
2. 
def init: jakich info potrzebujemy o samochodzie,
self: odnosi się do klasy, którą tworzymy, 
marka: str, model:str, rok: int (uznalam ze tego potrzebuje)
self.marka = marka (odnosimy się do klasy zawsze; marka to nasza zmienna, którą wkładamy do pudełka self.marka, odnosze sie zawsze do pudelka, a nie do zmiennej)
self.model = model 
self.rok = rok 
3.
def opis(self): funkcja, ktora nalezy do samochodu, to jest moj opis samochodu
return f"...": tutaj wykorzystuje pudelka hihi
4.
def repr(self): jak ktos zrobi print, to pokaze ten opis samochodu
return self.opis(): zwraca nam ten opis cnie
5. przykladzik:
SamochodExample = Samochod("Opel", "Astra", 2000)

print(SamochodExample)

'''
'''
Polecenie: 
Zrob klase lampka, ma miec funkcje opisu w ktorej mam miec kolor lampki, rok produkcji lampki, cene lampki oraz moc świecenia w "W" (watach)
zrob wlacznik
'''


# class Lampka:
#     def __init__(self, kolor, rok, cena, moc, wlacznik:bool):
#        self.kolor = kolor
#        self.rok = rok
#        self.cena = cena
#        self.moc = moc
#        self.wlacznik = wlacznik
       
#     def warunek(self):
#         if self.wlacznik == True:
#             return f"włączona"
#         else:
#             return f"wyłączona"
    
#     def tworzenie(self):
#         self.wlacznik = not self.wlacznik #obecne pudełko = nieobecne pudełko
        
        
        
#     def opis(self):
#         return f"Lampka w kolorze {self.kolor}, wyprodukowana w {self.rok} roku, kosztuje {self.cena}zł, o mocy {self.moc}W, jest {self.warunek()}"
 
#     def __repr__(self):
#        return self.opis()
   
# Przyklad1 = Lampka('zielona', 2024, 120, 50, True)

# print(Przyklad1)
# Przyklad1.tworzenie()
# print(Przyklad1)
# Przyklad1.tworzenie() #nadpisalismy i teraz wywolujemy funkcje ktora zmienia wlacznik
# print(Przyklad1)

'''
Polecenie: 
Zrob klase konto bankowe, ma miec wlasciela i saldo poczatkowe, 
ma miec funkcje: wplacania kasy,
wyplacania kasy, jesli nie ma wystarczajacych srodkow to zeby wyswieltal komunikat
wyswietlania stanu konta,
naliczania odsetek czyli powiedzmy niech to bedzie 10% odsetek
'''
# class KontoBankowe:
    
#     def __init__(self, wlasciciel, saldo_pocz):
#         self.wlasciciel = wlasciciel 
#         self.saldo_pocz = saldo_pocz
    
#     def wplacanie(self, kwota): #dodajemy se zmienna
#         self.saldo_pocz = self.saldo_pocz + kwota
    
#     def wyplacanie(self, kwota):
#         if self.saldo_pocz >= kwota:
#             self.saldo_pocz = self.saldo_pocz - kwota #kod dziala od gory do dolu wiec musi byc tutaj 
#         else:
#             print(f"nie masz wystarczających środków na koncie")
    
#     def stan(self):
#         return f"{self.saldo_pocz}"
    
#     def __repr__(self):
#         return self.stan()
    
#     def odsetki(self):
#         self.saldo_pocz = self.saldo_pocz + self.saldo_pocz * 0.1
    
        
# konto = KontoBankowe("Marek", 100)
        
# konto.wyplacanie(200)
# print(konto)

