import streamlit as st
from streamlit_option_menu import option_menu

from controller.EvalController import EvaluadorController
from view.AboutPartial import consultar_instrucciones
from view.PruebaPartial import probar_streamlit, abrir_musica


class MainView:
    def __init__(self) -> None:
        super().__init__()

        """if 'main_view' not in st.session_state:
            self.menu_actual = "Inicio"

            self.controller = EvaluadorController()
            st.session_state['main_view'] = self
        else:
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller
"""
        self._dibujar_layout()

    def _dibujar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        """st.set_page_config(page_title="Análisis mercado energía", page_icon='', layout="wide",
                           initial_sidebar_state="expanded")"""
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3 = st.columns([1, 1, 1])

        # Define lo que abrá en la barra de menu
        self.menu_actual = option_menu(None, ["Asistente", 'Jurados', 'Director'],
                                           icons=['person', 'people', 'file-person'],
                                            menu_icon="cast", default_index=0, orientation="horizontal",
                                            styles = {
                                                "container": {"padding": "0!important", "background-color": "#fafafa"},
                                                "icon": {"color": "#c4c4c4", "font-size": "25px"},
                                                "nav-link": {"color": "#c4c4c4", "font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#6689ff"},
                                                "nav-link-selected": {"background-color": "#0b4bff", "color": "white"}, })

    def controlar_menu(self):
        if self.menu_actual == "Asistente":
            consultar_instrucciones(st)
            with st.sidebar:
                self.menu_actual = option_menu(None, ['Crear Acta', 'Ver Historicos'],
                                               icons=['mortarboard', 'stack-overflow'],
                                               menu_icon="cast", default_index=0, styles={"nav-link-selected": {"background-color": "#0b4bff"},})
        elif self.menu_actual == "Jurados":
            with st.sidebar:
                self.menu_actual = option_menu(None, ['Exportar Acta', 'Evaluar Trabajo'],
                                               icons=['file-pdf', 'pencil-square'],
                                               menu_icon="cast", default_index=0)
        elif self.menu_actual == "Director":
            with st.sidebar:
                self.menu_actual = option_menu(None, ['Modificar Criterios', 'Ver Historicos'],
                                               icons=['vector-pen', 'stack-overflow'],
                                               menu_icon="cast", default_index=0)
        if self.menu_actual == "Crear Acta":
            pass


# Main call
if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()
    
