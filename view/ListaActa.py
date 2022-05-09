from view.EvalTrabajoGrado import agregar_acta

def listar_actas(st, controller):
    #Itera los elementos de evaluacion agregados y los muestra

    st.title("Datos guardados:")
    for key in controller.actas:
        st.write(key), ":", st.json(controller.actas[key])         #No sirve listar, intente recorrer el diccionario actas pero no quiere servir
"""    for key in controller.actas:                                #Ni con el metodo que mostro la profesora sirve, no se como cambiar eso
        #with st.container():
        st.write()"""
"""            st.write(acta.numero)
            st.write(acta.nombre_del_trabajo)
            st.write(acta.fecha)
            st.write(acta.autor)
            st.write(acta.tipo_de_trabajo)
            st.write(acta.directora)
            st.write(acta.codirector)
            st.write(acta.jurado1)
            st.write(acta.jurado2)
            st.write(acta.criterio)"""

