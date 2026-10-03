import streamlit as st
import base64

st.set_page_config(page_title="Sistema de Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

# --- Função para carregar arquivos em Base64 ---
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# --- Fonte Rawline ---
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

# --- Fundo com overlay mais escuro ---
def set_background(png_file):
    bin_str = get_base64(png_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.78), rgba(0, 0, 0, 0.78)), url("data:image/jpeg;base64,{bin_str}");
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

# --- Importa Material Symbols Rounded (fonte de ícones moderna) ---
st.markdown("""
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0" />
""", unsafe_allow_html=True)

st.markdown(f"""
<style>
    {font_css}

    html, body, .stApp, .stApp * {{
        font-family: 'Rawline', 'Segoe UI', Tahoma, sans-serif !important;
    }}

    /* Preserva a fonte Material Symbols nos ícones */
    [data-testid="stIconMaterial"],
    .material-symbols-rounded,
    span[class*="material-symbols"],
    .material-icons,
    .msr {{
        font-family: 'Material Symbols Rounded', 'Material Icons' !important;
    }}

    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp p, .stApp span, .stApp div, .stApp a, .stApp li,
    .stApp label, [data-testid="stMarkdownContainer"],
    [data-testid="stWidgetLabel"] {{
        color: #FFFFFF !important;
    }}

    /* Container principal */
    .block-container {{
        max-width: 1100px !important;
        margin: 0 auto !important;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }}

    /* ===== TÍTULO CENTRALIZADO (como na imagem atual) ===== */
    .titulo-central {{
        text-align: center !important;
        color: #F1F5F9 !important;
        font-weight: 700;
        font-size: 1.9rem;
        line-height: 1.25;
        margin: 0 0 0.4rem 0;
        letter-spacing: 0.3px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.95);
    }}

    .subtitulo-central {{
        text-align: center !important;
        color: #94A3B8 !important;
        font-weight: 400;
        font-size: 0.85rem;
        margin: 0 0 1.8rem 0;
        letter-spacing: 0.2px;
        text-shadow: 0 2px 6px rgba(0, 0, 0, 0.9);
    }}

    /* ===== CARD (item da lista) ===== */
    a.app-card {{
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 1rem !important;

        width: 100% !important;
        min-height: 52px !important;
        padding: 0.7rem 1.1rem !important;
        margin-bottom: 0.55rem !important;

        /* Paleta moderna: cinza grafite com transparência */
        background: rgba(38, 41, 48, 0.82) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(203, 213, 225, 0.15) !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.35) !important;

        color: #E2E8F0 !important;
        text-decoration: none !important;
        transition: all 0.22s ease !important;
    }}

    a.app-card:hover {{
        background: rgba(51, 55, 64, 0.95) !important;
        border-color: rgba(96, 165, 250, 0.45) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(59, 130, 246, 0.18) !important;
        text-decoration: none !important;
    }}

    /* Nome do app */
    a.app-card .app-name {{
        font-size: 0.95rem !important;
        font-weight: 400 !important;
        color: #E2E8F0 !important;
        line-height: 1.35 !important;
        text-align: left !important;
        flex: 1 !important;
        transition: color 0.22s ease !important;
    }}

    a.app-card:hover .app-name {{
        color: #FFFFFF !important;
    }}

    /* Ícone moderno à direita */
    a.app-card .app-icon {{
        font-family: 'Material Symbols Rounded' !important;
        font-size: 20px !important;
        font-weight: 400 !important;
        color: #60A5FA !important;
        flex-shrink: 0 !important;
        transition: all 0.22s ease !important;
        opacity: 0.85 !important;
    }}

    a.app-card:hover .app-icon {{
        color: #93C5FD !important;
        opacity: 1 !important;
        transform: translateX(3px) !important;
    }}

    /* Rodapé discreto */
    .rodape-minimo {{
        text-align: center;
        color: #64748B !important;
        font-size: 10.5px;
        margin-top: 2.5rem;
        letter-spacing: 0.3px;
        line-height: 1.6;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.95);
    }}

    .rodape-minimo strong {{
        color: #94A3B8 !important;
        font-weight: 500;
    }}
</style>
""", unsafe_allow_html=True)

# --- Título e subtítulo centralizados ---
st.markdown('<h1 class="titulo-central">🏫 Sistema de Gerenciamento Escolar 🏫</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo-central">Clique em um aplicativo para abri-lo em uma nova aba</p>', unsafe_allow_html=True)

# --- Dicionário de Aplicativos (com ícones modernos Material Symbols) ---
# Referência de ícones: https://fonts.google.com/icons
apps = {
    "Apura Resultado": {
        "url": "https://apura-resultado-final.streamlit.app/",
        "icon": "emoji_events",       # troféu
    },
    "Avaliação Especial": {
        "url": "https://avaliacaoespecialcontagem.streamlit.app/",
        "icon": "fact_check",         # checklist
    },
    "Bolsa Família": {
        "url": "https://bolsafamilia2.streamlit.app/",
        "icon": "payments",           # pagamento
    },
    "Contagem de Aulas no Siea": {
        "url": "https://contagemdeaulasnosiea.streamlit.app/",
        "icon": "menu_book",          # livro aberto
    },
    "Criação de Horário Escolar": {
        "url": "https://sistemadecriacaodehorarioescolar.streamlit.app/",
        "icon": "calendar_month",     # calendário
    },
    "Pontuação no SGE": {
        "url": "https://conceitosnosge.streamlit.app/",
        "icon": "bar_chart",          # gráfico
    },
    "Solicitação de Vagas - Participante": {
        "url": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html",
        "icon": "person",             # pessoa
    },
    "Solicitação de Vagas - QR Code": {
        "url": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html",
        "icon": "qr_code_2",          # qrcode
    },
    "Solicitação de Vagas - Secretaria": {
        "url": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html",
        "icon": "apartment",          # prédio
    },
    "Verificar Aulas que Faltam nos Diários": {
        "url": "https://aulasprevistasxaulasrealizadas.streamlit.app/",
        "icon": "search",             # lupa
    },
    "Verificar Notas em Branco nos Diários": {
        "url": "https://verificarnotasembranconosdiarios.streamlit.app/",
        "icon": "description",        # documento
    },
}

# --- Layout em 2 colunas ---
cols = st.columns(2)
for i, (nome, info) in enumerate(sorted(apps.items())):
    with cols[i % 2]:
        st.markdown(
            f'''
            <a class="app-card" href="{info['url']}" target="_blank" rel="noopener noreferrer">
                <span class="app-name">{nome}</span>
                <span class="app-icon">{info['icon']}</span>
            </a>
            ''',
            unsafe_allow_html=True
        )

# --- Rodapé ---
st.markdown("""
<p class='rodape-minimo'>
Aplicativos desenvolvidos por <strong>André Torres</strong> · Gestão escolar eficiente, organizada e prática<br>
© 2026 · Todos os direitos reservados · andretorres.adm@gmail.com
</p>
""", unsafe_allow_html=True)