import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️")

# Título y descripción
st.title("🌡️ Conversor de Temperatura")
st.markdown("Convierte fácilmente entre **Celsius y Fahrenheit**.")

# Línea divisoria
st.divider()

# Selección del tipo de conversión
opcion = st.radio("📌 Selecciona el tipo de conversión:", 
                  ("Celsius ➝ Fahrenheit", "Fahrenheit ➝ Celsius"))

# Entrada de múltiples temperaturas
st.markdown("✍️ Ingresa varias temperaturas separadas por comas (ejemplo: `0, 25, 100`).")
entrada = st.text_input("Temperaturas:")

if entrada:
    try:
        # Convertir texto en lista de números
        valores = [float(x.strip()) for x in entrada.split(",")]

        # Procesar según la opción
        if opcion == "Celsius ➝ Fahrenheit":
            resultados = [(c, (c * 9/5) + 32) for c in valores]
            df = pd.DataFrame(resultados, columns=["Celsius (°C)", "Fahrenheit (°F)"])
        else:
            resultados = [(f, (f - 32) * 5/9) for f in valores]
            df = pd.DataFrame(resultados, columns=["Fahrenheit (°F)", "Celsius (°C)"])

        # Mostrar tabla con resultados
        st.success("✅ Conversión realizada:")
        st.dataframe(df, use_container_width=True)

    except ValueError:
        st.error("⚠️ Asegúrate de ingresar solo números separados por comas.")
else:
    st.info("ℹ️ Esperando que ingreses temperaturas...")

# Línea final
st.divider()
st.caption("Desarrollado con ❤️ usando Streamlit")
