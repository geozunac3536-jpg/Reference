import streamlit as st
import plotly.graph_objects as go
from gtts import gTTS
import tempfile

# --- CONFIGURACIÓN DE LA PÁGINA (MODO DARK/SINESTRO) ---
st.set_page_config(page_title="PROTOCOLO DE COLUSIÓN DETECTADO", layout="centered", initial_sidebar_state="collapsed")

# --- CSS PARA ESTILO "TERMINAL DEL JUICIO FINAL" ---
st.markdown("""
    <style>
    /* Fondo Negro Total */
    .stApp { background-color: #000000; }
    
    /* Textos en Rojo Neón y Blanco Terminal */
    h1, h2, h3 { color: #ff3333 !important; font-family: 'Courier New', monospace; font-weight: bold; }
    p, div, label { color: #e0e0e0 !important; font-family: 'Courier New', monospace; }
    
    /* Cajas de Alerta Siniestras */
    .doom-box { 
        background-color: #1a0505; 
        border: 2px solid #ff0000; 
        padding: 20px; 
        border-radius: 0px; 
        box-shadow: 0 0 15px #ff0000;
        margin-bottom: 20px;
    }
    
    /* Botón Siniestro */
    .stButton>button {
        color: #000000;
        background-color: #ff3333;
        border: none;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff6666;
        box-shadow: 0 0 10px #ff3333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("⚠️ ALERTA DE RIESGO CORPORATIVO: R-CONTROL")
st.markdown("### EXPEDIENTE VINCULADO: ERIKA SÁNCHEZ")
st.divider()

# --- EL MENSAJE DE VOZ (GUION GRAVE) ---
# Usamos slow=True para que suene más grave, pausado y amenazante.
mensaje_voz = """
Erika Sánchez. R Control.
Escucha con atención.
Has cometido un error de cálculo matemático.
Al mantener el boletinaje de Genaro Carrasco, R Control se ha convertido técnicamente en cómplice de encubrimiento de delitos federales.
Narcea ya cayó. El folio del SAT uno be cuarenta y cuatro y el folio de Walmart W M T veintiseis ya están activos.
Cuando Narcea caiga por evasión fiscal, se llevará consigo a sus aliados.
Walmart Ethics no tolera proveedores que facilitan represalias contra denunciantes de corrupción.
Si Genaro no sale de tu lista negra en 24 horas, el reporte de colusión llegará a las oficinas centrales de tus clientes en Estados Unidos.
No sacrifiques tu empresa por proteger a un cadáver financiero como Narcea.
El tiempo corre.
"""

# --- SECCIÓN 1: LA CADENA DE CONTAGIO (GRÁFICA) ---
st.markdown("""
<div class="doom-box">
    <h3 style="text-align: center;">EL EFECTO DOMINÓ (RIESGO SISTÉMICO)</h3>
    <p>El incumplimiento normativo de NARCEA (Lavado de Activos) contamina legalmente a sus socios comerciales (R-CONTROL) bajo las normas de <b>Walmart Global Ethics & Compliance</b>.</p>
</div>
""", unsafe_allow_html=True)

# Diagrama Sankey (Flujo de Contaminación)
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["NARCEA (Fraude Fiscal)", "GENARO (Denunciante)", "R-CONTROL (Cómplice)", "WALMART (Cliente)", "SAT (Autoridad)", "SANCIÓN MASIVA"],
      color = ["red", "blue", "red", "white", "white", "red"]
    ),
    link = dict(
      source = [0, 0, 2, 2, 1, 4], # Indices de origen
      target = [2, 4, 3, 5, 4, 0], # Indices de destino
      value =  [50, 50, 40, 60, 10, 100],
      color = ["rgba(255,0,0,0.4)", "rgba(255,0,0,0.4)", "rgba(255,0,0,0.8)", "rgba(255,0,0,0.8)", "blue", "red"]
  ))])

fig.update_layout(
    title_text="DIAGRAMA DE CONTAGIO LEGAL (FOLIO WMT260203209)", 
    font_size=12, 
    paper_bgcolor='black', 
    plot_bgcolor='black',
    font=dict(color='white')
)
st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN 2: LA ADVERTENCIA DIRECTA ---
st.markdown(f"""
<div class="doom-box">
    <h3>MENSAJE PARA: ERIKA SÁNCHEZ</h3>
    <p><b>ASUNTO:</b> COLUSIÓN EN REPRESALIAS (WHISTLEBLOWER RETALIATION)</p>
    <p>Usted administra una base de datos. Hoy, esa base de datos está siendo usada por <b>Transportes Narcea</b> para castigar a un ciudadano que denunció lavado de dinero ante la FGR.</p>
    <p>Al mantener el bloqueo (R-Control), usted se alinea con el denunciado (Narcea) y se convierte en <b>OBSTRUCTOR DE LA JUSTICIA FEDERAL</b>.</p>
    <p>¿Vale la pena perder su contrato con Walmart por defender a Sayra y Fernando?</p>
</div>
""", unsafe_allow_html=True)

# --- REPRODUCTOR DE VOZ ---
col1, col2 = st.columns([1, 4])
with col2:
    if st.button('🔊 ESCUCHAR LA SENTENCIA LÓGICA'):
        try:
            # slow=True hace que la voz sea pausada y más grave/siniestra
            tts = gTTS(mensaje_voz, lang='es', tld='com.mx', slow=True) 
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                st.audio(fp.name, format="audio/mp3")
        except Exception as e:
            st.error(f"Error de sistema: {e}")

st.divider()
st.markdown("<p style='text-align: center; color: #555;'>ESTE NODO SE AUTODESTRUIRÁ AL EJECUTARSE LA ORDEN DE APREHENSIÓN CONTRA NARCEA.</p>", unsafe_allow_html=True)
