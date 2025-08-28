import streamlit as st

import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️")

# Título y descripción
st.title("🌡️ Conversor de Temperatura")
st.markdown("Convierte fácilmente de **Celsius a Fahrenheit**.")

# Línea divisoria
st.divider()

# Ingreso de temperatura en Celsius
celsius = st.number_input("🌡️ Ingresa la temperatura en °C:", value=0.0, step=0.1)

# Conversión a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
st.success(f"✅ {celsius:.2f} °C equivale a {fahrenheit:.2f} °F")

# Pie de página
st.caption("Desarrollado con ❤️ usando Streamlit")
