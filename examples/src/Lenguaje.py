class Lenguaje:
    def __init__(self, name, year) -> None:
        self.name = name
        self.year = year

    def description(self):
        print(f"{self.name} fue creado en {self.year}")


leng = Lenguaje("JavaScript", 1995)
leng.description()

leng = Lenguaje("HTML", 1993)
leng.description()

leng = Lenguaje("CSS", 1996)
leng.description()
