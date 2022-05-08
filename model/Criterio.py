import json

file = open("ListaCriterios.json", "r")
js = file.read()
lista_criterios = json.loads(js)

class Criterio:

    def __init__(self, observacion, nota1, nota2, ponderado):
        self._observacion = observacion
        self._criterio = lista_criterios
        self._nota1 = nota1
        self._nota2 = nota2
        self._ponderado = ponderado

    def __str__(self) -> None:
        return json.dump(self.__dict__)
