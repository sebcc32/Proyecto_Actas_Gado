from model.CrearActa import CrearActa
from model.Criterio import Criterio
import json

file = open("model\ListaCriterios.json", "r")
js = file.read()
lista_criterios = json.loads(js)

def agregar_acta(st, controller):
    # Objecto que modelará el formulario
    acta_obj = CrearActa()
    acta_obj.numero = st.number_input("Id acta")
    acta_obj.nombre_del_trabajo = st.text_input("Titulo del trabajo")
    acta_obj.fecha = st.date_input("Fecha de creacion del trabajo")
    acta_obj.autor = st.text_input("Nombre estudiante")
    acta_obj.tipo_de_trabajo = st.selectbox('¿Tipo de trabajo?', ["Aplicado", "investigacion"])
    acta_obj.directora = st.text_input("Nombre Directora")
    acta_obj.codirector = st.text_input("Nombre Co-director")
    st.write("Si no hay codirector poner: N/A")
    acta_obj.jurado1 = st.text_input("Nombre Primer Jurado")
    acta_obj.jurado2 = st.text_input("Nombre Segundo Jurado")
    acta_obj.criterio = lista_criterios       #aqui creando un acta y colocando criterior predeterminados
    enviado_btn = st.button("Enviar")
    if enviado_btn:
        controller.agregar_acta(acta_obj)
        st.write("El archivo se ha creado exitosamente")
    return controller


    # Agregar campo para leer el tema y la versión de la evaluación del proyecto

def agregar_evaluacion(st, controller):
    actas_llaves = controller.actas.keys()
    acta_evaluar = st.selectbox("¿Que acta vas a calificar?", actas_llaves)  # Asi encuentro todas las llaves del directorio acta

    criterio_obj = Criterio()
    criterio_obj.criterio = st.selectbox('Criterio a evaluar?', lista_criterios )
    criterio_obj.observacion = st.text_input("Observaciones adicionales")
    criterio_obj.nota1 = st.text_input("Nota primer jurado")                        #aqui lleno los objetos de la clase criterio
    criterio_obj.nota2 = st.text_input("Nota segundo jurado")
    criterio_obj.ponderado = st.text_input("Ponderado") #pon el ponderado automaticamente de lista_criterios si puedes y vuelve a poner los ponderados en el jsonxD

    enviado_btn = st.button("Enviar")
    if enviado_btn:
        controller.actas[acta_evaluar].criterio = criterio_obj             #aqui estoy metiendo los objetos de criterio
        st.write("El archivo se ha creado exitosamente")                   #al diccionario criterio que tengo en acta que elegi

    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal


