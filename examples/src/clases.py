diccionario_simple_de_dulces_con_sus_calorias = {
    "Tortita": 227,
    "Gofre": 291,
    "Galleta": 488,
    "Torrija": 229,
    "Tarta": 372,
    "Magdalena": 377,
    "Croissant": 466,
    "MARTILLO": 1000000,
}

from collections import abc
from collections.abc import Iterator


class MiDiccionarioEspecialDeDulces(abc.MutableMapping):
    def __init__(self) -> None:
        self.diccionario_de_dulces_con_sus_calorias = {}
        self.cosas_que_no_son_dulces = set()

    def __len__(self) -> int:
        return len(self.diccionario_de_dulces_con_sus_calorias)

    def __iter__(self) -> Iterator[str]:
        return self.diccionario_de_dulces_con_sus_calorias.__iter__()

    def __setitem__(self, clave: str, valor: int) -> None:
        if clave in self.cosas_que_no_son_dulces:
            print(f'Se ha descartado "{clave}" porque no es un dulce')
        else:
            self.diccionario_de_dulces_con_sus_calorias[clave] = valor

    def __delitem__(self, clave: str) -> None:
        try:
            del self.diccionario_de_dulces_con_sus_calorias[clave]
        except KeyError:
            msg = f"Este Contenedor no tiene la clave '{clave}'"
            raise KeyError(msg)

    def __getitem__(self, clave: str) -> int:
        try:
            return self.diccionario_de_dulces_con_sus_calorias[clave]
        except KeyError:
            msg = f"Este Contenedor no tiene la clave '{clave}'"
            raise KeyError(msg)


mi_dicc = MiDiccionarioEspecialDeDulces()
mi_dicc.diccionario_de_dulces_con_sus_calorias = diccionario_simple_de_dulces_con_sus_calorias
print(mi_dicc.diccionario_de_dulces_con_sus_calorias)

print("Longitud del diccionario")
print(mi_dicc.__len__())

print("Iterador de dulces diccionario (claves)")
print(list(mi_dicc.__iter__()))
