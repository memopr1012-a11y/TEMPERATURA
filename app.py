import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️")

st.title("🌡️ Conversor de Temperatura")
st.markdown("Convierte entre **Celsius y Fahrenheit** con historial interactivo y animaciones 🎉")

st.divider()

# --- Inicializar historial en session_state ---
if "historial" not in st.session_state:
    st.session_state["historial"] = []

# Selección del tipo de conversión
opcion = st.radio("📌 Selecciona el tipo de conversión:", 
                  ("Celsius ➝ Fahrenheit", "Fahrenheit ➝ Celsius"))

# Entrada de temperatura (soporta negativos y decimales)
valor = st.number_input("🌡️ Ingresa una temperatura (puede ser negativa o con decimales):", value=0.0, step=0.1)

# Botón para convertir
if st.button("🔄 Convertir"):
    if opcion == "Celsius ➝ Fahrenheit":
        resultado = (valor * 9/5) + 32
        mensaje = f"{valor:.2f} °C ➝ {resultado:.2f} °F"
        st.success(f"✅ {mensaje}")
        st.session_state["historial"].append(("°C a °F", f"{valor:.2f}", f"{resultado:.2f}"))

        # Animaciones según la temperatura
        if valor < 0:
            st.snow()  # Efecto nieve
        elif valor > 30:
            st.balloons()  # Efecto globos
    else:
        resultado = (valor - 32) * 5/9
        mensaje = f"{valor:.2f} °F ➝ {resultado:.2f} °C"
        st.s
