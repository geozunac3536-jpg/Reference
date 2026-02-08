# Referimport streamlit as st
import pandas as pd
import plotly.graph_objects as go
from gtts import gTTS
import tempfile

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="AUDITORÍA FORENSE - CONFIDENCIAL", layout="wide", initial_sidebar_state="expanded")

# ESTILO CSS (ROJO ALERTA)
st.markdown("""
    <style>
    .big-font { font-size:30px !important; color: #D32F2F; font-weight: bold; }
    .warning-box { background-color: #FFEBEE; padding: 20px; border-radius: 10px; border-left: 5px solid #D32F2F; }
    </style>
    """, unsafe_allow_html=True)

# SIDEBAR: FOLIOS DE INVESTIGACIÓN
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Sat_logo.svg/1200px-Sat_logo.svg.png", width=100)
st.sidebar.markdown("### EXPEDIENTES ACTIVOS")
st.sidebar.error("**SAT (Evasión Fiscal):**\nFolio: 1B4403D2BE65EB17")
st.sidebar.warning("**WALMART ETHICS:**\nFolio: WMT260203209")
st.sidebar.info("**FGR (Carpeta):**\nFED/VER/ORI/4132/2026")

# TÍTULO PRINCIPAL
st.markdown('<p class="big-font">REPORTE DE DISCREPANCIA FISCAL Y LAVADO DE ACTIVOS</p>', unsafe_allow_html=True)
st.write("**ENTIDAD AUDITADA:** TRANSPORTES NARCEA S.A. DE C.V. / CORRECAMINOS TUCÁN")
st.write("**ESTATUS:** INVESTIGACIÓN EN CURSO (FASE DE RATIFICACIÓN)")

# SECCIÓN 1: LA EVIDENCIA (GRÁFICAS)
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("EL FRAUDE DE MAYO 2024")
    # Datos
    labels = ['Reportado al SAT (Deducido)', 'Pagado Realmente', 'DESVÍO (LAVADO)']
    values = [71958.70, 34015.86, 37942.84]
    colors = ['gray', 'green', 'red']
    
    fig = go.Figure(data=[go.Bar(x=labels, y=values, marker_color=colors, text=values, textposition='auto')])
    fig.update_layout(title_text='Discrepancia Fiscal (Dinero Fantasma)')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("IMPLICACIONES LEGALES")
    st.markdown("""
    La discrepancia de **$37,942.84 MXN** en un solo mes activa auditoría por:
    1. **Simulación de Operaciones (Art. 69-B CFF).**
    2. **Defraudación Fiscal Equiparada (Art. 109 CFF).**
    
    *El SAT rastreará no solo a la empresa, sino a quien ejecutó las transferencias.*
    """)

# SECCIÓN 2: LA ADVERTENCIA A EMPLEADOS (VOZ)
st.divider()
st.subheader("⚠️ AVISO DE RESPONSABILIDAD PENAL (ART. 95 CFF)")

mensaje_voz = """
Aviso urgente para el área administrativa y contable.
La investigación federal ha identificado a Sayra, Leticia y Fernando como ejecutores materiales de la dispersión de nómina simulada.
Según el Artículo 95 del Código Fiscal de la Federación, la cárcel no es solo para los dueños, sino para los empleados que facilitan la evasión.
Narcea sacrificará a sus empleados para salvarse. Tienen 48 horas para exigir a sus jefes que arreglen el problema laboral de origen, o ustedes serán los primeros citados por la Fiscalía.
"""

st.markdown(f"""
<div class="warning-box">
    <b>MENSAJE PARA: SAYRA (RH), LETICIA (CONTABILIDAD), FERNANDO (OPERACIONES)</b><br><br>
    La defensa de "solo seguía órdenes" <b>NO ES VÁLIDA</b> en delitos fiscales.<br>
    Ustedes firmaron los movimientos. Ustedes dispersaron los pagos "por fuera".<br>
    Cuando el SAT congele las cuentas, los dueños dirán que fue "error administrativo" de ustedes.<br>
    <b>¿Van a ir a prisión por un sueldo que ni siquiera es alto?</b>
</div>
""", unsafe_allow_html=True)

# GENERADOR DE AUDIO
if st.button('🔊 ESCUCHAR ADVERTENCIA LEGAL'):
    tts = gTTS(mensaje_voz, lang='es', tld='com.mx') # Acento mexicano
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")

# PIE DE PÁGINA
st.divider()
st.caption("ESTE ENLACE CADUCARÁ AUTOMÁTICAMENTE AL MOMENTO DE LA RATIFICACIÓN DE DENUNCIA.")ence
