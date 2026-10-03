import streamlit as st
import base64

st.set_page_config(page_title="Sistema de Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

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
            background-image: linear-gradient(rgba(0, 0, 0, 0.80), rgba(0, 0, 0, 0.80)), url("data:image/jpeg;base64,{bin_str}");
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

    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp p, .stApp span, .stApp div, .stApp a, .stApp li,
    .stApp label, [data-testid="stMarkdownContainer"],
    [data-testid="stWidgetLabel"] {{
        color: #FFFFFF !important;
    }}

    /* ===== Container mais estreito ===== */
    .block-container {{
        max-width: 980px !important;
        margin: 0 auto !important;
        padding-top: 1.8rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }}

    /* ===== TÍTULO ===== */
    .titulo-central {{
        text-align: center !important;
        color: #FFFFFF !important;
        font-weight: 700;
        font-size: 1.75rem;
        line-height: 1.25;
        margin: 0 0 0.5rem 0;
        letter-spacing: 0.3px;
        text-shadow: 0 2px 12px rgba(0, 0, 0, 1);
    }}

    /* ===== Subtítulo ===== */
    .subtitulo-central {{
        text-align: center !important;
        color: #CBD5E1 !important;
        font-weight: 400;
        font-size: 0.9rem;
        margin: 0 0 2.4rem 0;
        letter-spacing: 0.2px;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 1);
    }}

    /* ===== CARD (usando container do Streamlit) ===== */
    div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] {{
        background: rgba(45, 50, 60, 0.95) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(203, 213, 225, 0.2) !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5) !important;
        padding: 0.75rem 1.15rem !important;
        margin-bottom: 0.55rem !important;
        transition: all 0.22s ease !important;
        align-items: center !important;
    }}

    div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:hover {{
        background: rgba(60, 65, 75, 1) !important;
        border-color: rgba(96, 165, 250, 0.8) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3) !important;
    }}

    /* Remove o padding padrão das colunas */
    div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {{
        padding: 0 !important;
    }}

    /* ===== TEXTO DO CARD ===== */
    div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] .app-name {{
        font-size: 1.05rem !important;
        font-weight: 500 !important;
        color: #E2E8F0 !important;
        line-height: 1.35 !important;
        text-align: left !important;
        transition: color 0.22s ease !important;
        display: flex !important;
        align-items: center !important;
        height: 100% !important;
    }}

    div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:hover .app-name {{
        color: #FFFFFF !important;
    }}

    /* ===== LINK DO CARD ===== */
    div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] a {{
        text-decoration: none !important;
        color: inherit !important;
        display: block !important;
        width: 100% !important;
    }}

    /* ===== IMAGEM DO ÍCONE ===== */
    div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] img {{
        width: 22px !important;
        height: 22px !important;
        opacity: 0.85 !important;
        transition: all 0.22s ease !important;
        filter: invert(62%) sepia(88%) saturate(1855%) hue-rotate(190deg) brightness(101%) contrast(96%) !important;
        margin: 0 auto !important;
        display: block !important;
    }}

    div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:hover img {{
        opacity: 1 !important;
        transform: translateX(3px) !important;
        filter: invert(75%) sepia(60%) saturate(1200%) hue-rotate(190deg) brightness(110%) contrast(100%) !important;
    }}

    .rodape-minimo {{
        text-align: center;
        color: #94A3B8 !important;
        font-size: 12px;
        margin-top: 2.5rem;
        letter-spacing: 0.3px;
        line-height: 1.6;
        text-shadow: 0 1px 4px rgba(0, 0, 0, 1);
    }}

    .rodape-minimo strong {{
        color: #CBD5E1 !important;
        font-weight: 600;
    }}
</style>
""", unsafe_allow_html=True)

# --- Título ---
st.markdown('<h1 class="titulo-central">🏫 Sistema de Gerenciamento Escolar</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo-central">Clique em um aplicativo para abri-lo em uma nova aba</p>', unsafe_allow_html=True)

# --- Dicionário de Ícones (URLs diretas do Phosphor Icons via CDN) ---
ICONS = {
    "trophy": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/trophy.svg",
    "check-square": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/check-square.svg",
    "money": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/money.svg",
    "book-open": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/book-open.svg",
    "calendar": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/calendar-blank.svg",
    "chart-bar": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/chart-bar.svg",
    "user": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/user.svg",
    "qr-code": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/qr-code.svg",
    "building": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/buildings.svg",
    "search": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/magnifying-glass.svg",
    "file-text": "https://unpkg.com/@phosphor-icons/core@2.0.3/assets/regular/file-text.svg",
}

# --- Dicionário de Aplicativos ---
apps = {
    "Apura Resultado": {"url": "https://apura-resultado-final.streamlit.app/", "icon": ICONS["trophy"]},
    "Avaliação Especial": {"url": "https://avaliacaoespecialcontagem.streamlit.app/", "icon": ICONS["check-square"]},
    "Bolsa Família": {"url": "https://bolsafamilia2.streamlit.app/", "icon": ICONS["money"]},
    "Contagem de Aulas no Siea": {"url": "https://contagemdeaulasnosiea.streamlit.app/", "icon": ICONS["book-open"]},
    "Criação de Horário Escolar": {"url": "https://sistemadecriacaodehorarioescolar.streamlit.app/", "icon": ICONS["calendar"]},
    "Pontuação no SGE": {"url": "https://conceitosnosge.streamlit.app/", "icon": ICONS["chart-bar"]},
    "Solicitação de Vagas - Participante": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html", "icon": ICONS["user"]},
    "Solicitação de Vagas - QR Code": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html", "icon": ICONS["qr-code"]},
    "Solicitação de Vagas - Secretaria": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html", "icon": ICONS["building"]},
    "Verificar Aulas que Faltam nos Diários": {"url": "https://aulasprevistasxaulasrealizadas.streamlit.app/", "icon": ICONS["search"]},
    "Verificar Notas em Branco nos Diários": {"url": "https://verificarnotasembranconosdiarios.streamlit.app/", "icon": ICONS["file-text"]},
}

# --- Ordenação alfabética em coluna ---
itens_ordenados = sorted(apps.items())
meio = (len(itens_ordenados) + 1) // 2

coluna_1 = itens_ordenados[:meio]
coluna_2 = itens_ordenados[meio:]

col_esq, col_dir = st.columns(2)

def render_card(nome, info):
    """Renderiza um card usando colunas do Streamlit."""
    col_texto, col_icone = st.columns([5, 1])
    
    with col_texto:
        st.markdown(
            f'<a href="{info["url"]}" target="_blank" rel="noopener noreferrer" class="app-name">{nome}</a>',
            unsafe_allow_html=True
        )
    
    with col_icone:
        st.image(info["icon"], width=22)

with col_esq:
    for nome, info in coluna_1:
        render_card(nome, info)

with col_dir:
    for nome, info in coluna_2:
        render_card(nome, info)

# --- Rodapé ---
st.markdown("""
<p class='rodape-minimo'>
Aplicativos desenvolvidos por <strong>André Torres</strong> · Gestão escolar eficiente, organizada e prática<br>
© 2026 · Todos os direitos reservados · andretorres.adm@gmail.com
</p>
""", unsafe_allow_html=True)
