import json
from model.Criterio import Criterio

class EvaluacionAnteproyecto:

    def __init__(self) -> None:
        super().__init__()
        self.criterio = Criterio()

        # Datos de toda evaluacion
        self._numero = ""
        self._fecha = ""
        self._autor = ""
        self._nombre_del_trabajo = ""
        self._director = " "
        self._codirector = " "
        self._jurado1 = " "
        self._jurado2 = " "

    def __str__(self) -> str:
        return json.dumps(self.__dict__)
