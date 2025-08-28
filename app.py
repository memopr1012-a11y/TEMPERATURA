import streamlit as st

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

# Entrada manual con number_input
if opcion == "Celsius ➝ Fahrenheit":
    celsius = st.number_input("🌡️ Ingresa la temperatura en °C:", value=0.0, step=0.1)
    fahrenheit = (celsius * 9/5) + 32
    st.success(f"✅ {celsius:.2f} °C equivale a {fahrenheit:.2f} °F")

    # Mensaje dinámico
    if celsius < 0:
        st.warning("❄️ Hace bastante frío, abrígate bien.")
    elif celsius < 25:
        st.info("🌤️ Temperatura agradable.")
    else:
        st.error("🔥 ¡Hace calor, mantente hidratado!")

else:
    fahrenheit = st.number_input("🌡️ Ingresa la temperatura en °F:", value=32.0, step=0.1)
    celsius = (fahrenheit - 32) * 5/9
    st.success(f"✅ {fahrenheit:.2f} °F equivale a {celsius:.2f} °C")

    # Mensaje dinámico
    if fahrenheit < 32:
        st.warning("❄️ Está helado, mucho cuidado.")
    elif fahrenheit < 77:
        st.info("🌤️ Clima templado y cómodo.")
    else:
        st.error("🔥 ¡Mucho calor, hidrátate!")

# Línea final
st.divider()
st.caption("Desarrollado con ❤️ usando Streamlit")
