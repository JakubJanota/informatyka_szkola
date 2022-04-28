# class Uczen:
#     liczba_ucz = 0
 
#     # We remember that this function always calls when we create an object
#     # __init__
 
#     def __init__(self, imie, wiek) -> None:
#         self.imie = imie
#         self.wiek = wiek
 
#         Uczen.liczba_ucz += 1 #<<<<<
 
# u1 = Uczen("Ala1",17)
# u2 = Uczen("Ala1",17)
# u3 = Uczen("Ala1",17)
 
# print("-*-"*20)
# print(f"u1.liczba_ucz \t {u1.liczba_ucz}")
# print(f"u2.liczba_ucz \t {u2.liczba_ucz}")
# print(f"u3.liczba_ucz \t {u3.liczba_ucz}")
# print(f"Uczen.liczba_ucz \t {Uczen.liczba_ucz}")
# print("-*-"*20)





# -----------------------------------
# -----------------------------------
# -----------------------------------
# -----------------------------------
# -----------------------------------





class Uczen:
    liczba_ucz = 0

    # We remember that this function always calls when we create an object
    # __init__

    def __init__(self, imie, wiek) -> None:
        self.imie = imie
        self.wiek = wiek

        Uczen.add_ucz() #<<<<<<<<

    @classmethod #<<<<<<<<
    def add_ucz(cls):
        cls.liczba_ucz += 1

    @classmethod
    def return_liczba_ucz(cls):
        return cls.liczba_ucz


u1 = Uczen("Ala1",17)
u2 = Uczen("Ala1",17)
u3 = Uczen("Ala1",17) 

print("-*-"*20)
print(f"u1.return_liczba_ucz() \t {u1.return_liczba_ucz()}")
print(f"u2.return_liczba_ucz() \t {u2.return_liczba_ucz()}")
print(f"u3.return_liczba_ucz() \t {u3.return_liczba_ucz()}")
print(f"Uczen.return_liczba_ucz() \t {Uczen.return_liczba_ucz()}")
print("-*-"*20)





