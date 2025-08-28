import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️")

st.title("🌡️ Conversor de Temperatura")
st.markdown("Convierte entre **Celsius y Fahrenheit** con historial de resultados.")

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
        resultado = int((valor * 9/5) + 32)   # Conversión redondeada a entero
        mensaje = f"{valor} °C ➝ {resultado} °F"
        st.success(f"✅ {mensaje}")
        st.session_state["historial"].append(("°C a °F", valor, resultado))
    else:
        resultado = int((valor - 32) * 5/9)   # Conversión redondeada a entero
        mensaje = f"{valor} °F ➝ {resultado} °C"
        st.success(f"✅ {mensaje}")
        st.session_state["historial"].append(("°F a °C", valor, resultado))

# Mostrar historial si existe
if st.session_state["historial"]:
    st.divider()
    st.subheader("📜 Historial de Conversiones")

    # Convertir historial a DataFrame
    df = pd.DataFrame(st.session_state["historial"], 
                      columns=["Conversión", "Ingresado", "Resultado"])
    st.dataframe(df, use_container_width=True)

    # Bo
