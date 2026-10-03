import streamlit as st
import base64

st.set_page_config(page_title="Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def get_font_face_css():
    font_300 = get_base64('rawline-300.ttf')
    font_400 = get_base64('rawline-400.ttf')
    font_700 = get_base64('rawline-700.ttf')
    css = ""
    if font_300:
        css += f"@font-face {{ font-family: 'Rawline'; src: url('data:font/ttf;base64,{font_300}') format('truetype'); font-weight: 300; }}"
    if font_400:
        css += f"@font-face {{ font-family: 'Rawline'; src: url('data:font/ttf;base64,{font_400}') format('truetype'); font-weight: 400; }}"
    if font_700:
        css += f"@font-face {{ font-family: 'Rawline'; src: url('data:font/ttf;base64,{font_700}') format('truetype'); font-weight: 700; }}"
    if not css:
        return "@import url('https://cdntgr.servicos.gov.br/fonts/rawline/rawline.css');"
    return css

def set_background(png_file):
    bin_str = get_base64(png_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
        return True
    return False

if not set_background('fundo.jpg'):
    if not set_background('fundo.png'):
        st.warning("⚠️ Imagem de fundo não encontrada!")

font_css = get_font_face_css()

st.markdown(f"""
<style>
    {font_css}

    html, body, .stApp, .stApp * {{
        font-family: 'Rawline', 'Segoe UI', Tahoma, sans-serif !important;
    }}

    [data-testid="stIconMaterial"],
    .material-symbols-rounded,
    span[class*="material-symbols"],
    .material-icons {{
        font-family: 'Material Symbols Rounded', 'Material Icons' !important;
    }}

    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp p, .stApp span, .stApp div, .stApp a, .stApp li,
    .stApp label, [data-testid="stMarkdownContainer"],
    [data-testid="stWidgetLabel"] {{
        color: #FFFFFF !important;
    }}

    .block-container {{
        max-width: 880px !important;
        margin-left: 0 !important;
        margin-right: auto !important;
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        padding-left: 1.8rem;
        padding-right: 1.5rem;
    }}

    /* ===== TÍTULO DISCRETO (canto superior) ===== */
    .brand-titulo {{
        text-align: left !important;
        color: #FFFFFF !important;
        font-weight: 700;
        font-size: 1.05rem;
        letter-spacing: 0.3px;
        line-height: 1.3;
        margin: 0 0 1.5rem 0;
        padding-bottom: 0.6rem;
        border-bottom: 1px solid rgba(148, 163, 184, 0.25);
        text-shadow: 0 2px 6px rgba(0, 0, 0, 0.9);
    }}

    .brand-titulo .icone {{ opacity: 0.75; margin-right: 6px; }}

    /* ===== RÓTULO SIMPLES (substitui caixa azul) ===== */
    .secao-label {{
        text-align: left;
        color: #94A3B8 !important;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin: 0 0 0.7rem 0;
        padding-left: 2px;
    }}

    /* ===== ITEM DA LISTA (mais contraste sobre fundo carregado) ===== */
    a.app-item {{
        display: block !important;
        width: 100% !important;
        padding: 0.7rem 0.95rem !important;
        margin-bottom: 0.45rem !important;
        background: rgba(20, 23, 30, 0.85) !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(148, 163, 184, 0.12) !important;
        border-radius: 8px !important;
        color: #E2E8F0 !important;
        font-size: 0.92rem !important;
        font-weight: 400 !important;
        text-align: left !important;
        text-decoration: none !important;
        transition: all 0.18s ease !important;
    }}

    a.app-item:hover {{
        background: rgba(59, 130, 246, 0.22) !important;
        border-color: rgba(96, 165, 250, 0.5) !important;
        color: #FFFFFF !important;
        transform: translateX(3px) !important;
        text-decoration: none !important;
    }}

    /* ===== AGRUPADOR (para os 3 de Solicitação de Vagas) ===== */
    .grupo-titulo {{
        color: #CBD5E1 !important;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.4px;
        margin: 0.4rem 0 0.35rem 0;
        padding-left: 2px;
    }}

    a.app-subitem {{
        display: block !important;
        width: 100% !important;
        padding: 0.55rem 0.95rem 0.55rem 1.6rem !important;
        margin-bottom: 0.35rem !important;
        background: rgba(20, 23, 30, 0.75) !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(148, 163, 184, 0.1) !important;
        border-left: 3px solid rgba(96, 165, 250, 0.5) !important;
        border-radius: 6px !important;
        color: #CBD5E1 !important;
        font-size: 0.88rem !important;
        text-align: left !important;
        text-decoration: none !important;
        transition: all 0.18s ease !important;
    }}

    a.app-subitem:hover {{
        background: rgba(59, 130, 246, 0.2) !important;
        border-left-color: #60A5FA !important;
        color: #FFFFFF !important;
        text-decoration: none !important;
    }}

    /* ===== RODAPÉ ENXUTO (1 linha) ===== */
    .rodape-minimo {{
        text-align: left;
        color: #64748B !important;
        font-size: 10.5px;
        margin-top: 2.2rem;
        font-weight: 400;
        letter-spacing: 0.3px;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.9);
    }}

    .rodape-minimo a {{
        color: #94A3B8 !important;
        text-decoration: none;
    }}
</style>
""", unsafe_allow_html=True)

# --- Branding discreto (título pequeno) ---
st.markdown(
    '<h1 class="brand-titulo"><span class="icone">🏫</span>Gerenciamento Escolar</h1>',
    unsafe_allow_html=True
)

# --- Rótulo de seção (substitui a caixa azul chamativa) ---
st.markdown('<div class="secao-label">Aplicativos</div>', unsafe_allow_html=True)

# --- Dicionário de Aplicativos ---
apps = {
    "Apura Resultado": "https://apura-resultado-final.streamlit.app/",
    "Avaliação Especial": "https://avaliacaoespecialcontagem.streamlit.app/",
    "Bolsa Família": "https://bolsafamilia2.streamlit.app/",
    "Contagem de Aulas": "https://contagemdeaulasnosiea.streamlit.app/",
    "Criação de Horário": "https://sistemadecriacaodehorarioescolar.streamlit.app/",
    "Pontuação no SGE": "https://conceitosnosge.streamlit.app/",
    "Aulas Faltam": "https://aulasprevistasxaulasrealizadas.streamlit.app/",
    "Notas em Branco": "https://verificarnotasembranconosdiarios.streamlit.app/",
}

# Apps de Solicitação de Vagas (agrupados)
vagas = {
    "Participante": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html",
    "QR Code": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html",
    "Secretaria": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html",
}

# --- Layout em 2 colunas ---
col_esq, col_dir = st.columns([1, 1])

with col_esq:
    for nome, url in apps.items():
        st.markdown(
            f'<a class="app-item" href="{url}" target="_blank" rel="noopener noreferrer">{nome}</a>',
            unsafe_allow_html=True
        )

with col_dir:
    st.markdown('<div class="grupo-titulo">Solicitação de Vagas</div>', unsafe_allow_html=True)
    for nome, url in vagas.items():
        st.markdown(
            f'<a class="app-subitem" href="{url}" target="_blank" rel="noopener noreferrer">↳ {nome}</a>',
            unsafe_allow_html=True
        )

# --- Rodapé enxuto (1 linha) ---
st.markdown(
    '<p class="rodape-minimo">André Torres · © 2026 · andretorres.adm@gmail.com</p>',
    unsafe_allow_html=True
)