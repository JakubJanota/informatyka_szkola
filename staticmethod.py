class Matama:

    def dodawanie(self):
        a, b = float(input("a = ")), float(input("b = "))
        print(f"dodawanie a+b = \t {a+b}")

    def dodawanie2(self,a,b):
        print(f"dodawanie2 a+b = \t {a+b}")    

m = Matama()
m.dodawanie()
m.dodawanie2(10,10)

print("<>"*30)

# TypeError: Matama.dodawanie() missing 1 required positional argument: 'self'
# Matama.dodawanie()

# ------------------------------------

class Matma_static:

    @staticmethod
    def dodawanie():
        a, b = float(input("a = ")), float(input("b = "))
        print(f"a+b = \t {a+b}")

    @staticmethod
    def dodawanie2(a,b):
        print(f"a+b = \t {a+b}")

Matma_static.dodawanie()
Matma_static.dodawanie2(100,100)