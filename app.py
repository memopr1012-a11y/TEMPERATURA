import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️")

st.title("🌡️ Conversor de Temperatura")
st.markdown("Convierte entre **Celsius y Fahrenheit** con historial interactivo 🎉")

st.divider()

# --- Inicializar historial en session_state ---
if "historial" not in st.session_state:
    st.session_state["historial"] = []

# Selección del tipo de conversión
opcion = st.radio("📌 Selecciona el tipo de conversión:", 
                  ("Celsius ➝ Fahrenheit", "Fahrenheit ➝ Celsius"))

# Entrada de temperatura como número entero
valor = st.number_input("🌡️ Ingresa una temperatura (solo enteros):", 
                        value=0, step=1, format="%d")

# Botón para convertir
if st.button("🔄 Convertir"):
    if opcion == "Celsius ➝ Fahrenheit":
        resultado = int((valor * 9/5) + 32)   # Redondea a entero
        mensaje = f"{valor} °C ➝ {resultado} °F"
        st.success(f"✅ {mensaje}")
        st.session_state["historial"].append(("°C a °F", valor, resultado))

        # Animaciones
        if valor < 0:
            st.snow()
        elif valor > 30:
            st.balloons()

    else:
        resultado = int((valor - 32) * 5/9)   # Redondea a entero
        mensaje = f"{valor} °F ➝ {resultado} °C"
        st.success(f"✅ {mensaje}")
        st.session_state["historial"].append(("°F a °C", valor, resultado))

        if valor < 32:
            st.snow()
        elif valor > 90:
            st.balloons()

# Mostrar historial
if st.session_state["historial"]:
    st.divider()
    st.subheader("📜 Historial de Conversiones")

    df = pd.DataFrame(st.session_state["historial"], 
                      columns=["Conversión", "Ingresado", "Resultado"])
    st.dataframe(df, use_container_width=True)

    if st.button("🗑️ Borrar historial"):
        st.session_state["historial"] = []
        st.info("Historial borrado.")
else:
    st.info("ℹ️ Aún no tienes conversiones registradas.")

st.divider()
st.caption("Desarrollado con ❤️ y 🎉 usando Streamlit")
