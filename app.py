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

# Entrada de temperatura única
valor = st.number_input("🌡️ Ingresa una temperatura:", value=0.0, step=0.1)

# Botón para convertir
if st.button("🔄 Convertir"):
    if opcion == "Celsius ➝ Fahrenheit":
        resultado = (valor * 9/5) + 32
        mensaje = f"{valor:.2f} °C ➝ {resultado:.2f} °F"
        st.success(f"✅ {mensaje}")
        st.session_state["historial"].append(("°C a °F", valor, resultado))
    else:
        resultado = (valor - 32) * 5/9
        mensaje = f"{valor:.2f} °F ➝ {resultado:.2f} °C"
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

    # Botón para borrar historial
    if st.button("🗑️ Borrar historial"):
        st.session_state["historial"] = []
        st.info("Historial borrado.")
else:
    st.info("ℹ️ Aún no tienes conversiones registradas.")

st.divider()
st.caption("Desarrollado con ❤️ usando Streamlit")
