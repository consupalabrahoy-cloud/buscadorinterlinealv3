import streamlit as st
import requests

st.title("Lector de Archivos de Texto desde GitHub")
st.write("Ingresa la URL del archivo .txt en tu repositorio para procesarlo.")

# Pide al usuario que ingrese la URL del archivo en formato "raw"
github_url = st.text_input("URL del archivo de texto (en formato raw)", "https://raw.githubusercontent.com/consupalabrahoy-cloud/constructorinterlineal/main/mi_archivo.txt")

# Botón para cargar el archivo
if st.button("Cargar archivo"):
    try:
        # Realiza una solicitud HTTP para obtener el contenido del archivo
        response = requests.get(github_url)

        # Verifica que la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtiene el contenido del archivo como texto
            contenido_del_archivo = response.text
            st.success("¡Archivo cargado con éxito!")
            
            # --- Aquí puedes integrar el código de tu procesador interlineal ---
            # Por ejemplo:
            st.text_area("Contenido del Archivo", contenido_del_archivo, height=300)
            
            # Puedes usar 'contenido_del_archivo' en tu lógica de procesamiento
            # lista_palabras = contenido_del_archivo.split('\n')
            # ... y el resto de tu lógica.
            
        else:
            st.error(f"Error al cargar el archivo. Código de estado: {response.status_code}. Por favor, revisa la URL.")
            st.info("Asegúrate de que la URL sea para el archivo en formato 'raw' y que sea público.")

    except Exception as e:
        st.error(f"Ocurrió un error inesperado: {e}")
