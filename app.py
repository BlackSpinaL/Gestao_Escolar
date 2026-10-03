import streamlit as st
import base64

# Configuração da página (Layout wide)
st.set_page_config(page_title="Painel de Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

# --- Função para carregar arquivos em Base64 ---
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# --- Função para carregar o CSS da Fonte Rawline (Arquivos TTF locais) ---
def get_font_face_css():
    font_300 = get_base64('rawline-300.ttf')
    font_400 = get_base64('rawline-400.ttf')
    font_700 = get_base64('rawline-700.ttf')
    css = ""
    if font_300:
        css += f"@font-face {{ font-family: 'Rawline'; src: url('data:font/ttf;base64,{font_300}') format('truetype'); font-weight: 300; font-style: normal; }}"
    if font_400:
        css += f"@font-face {{ font-family: 'Rawline'; src: url('data:font/ttf;base64,{font_400}') format('truetype'); font-weight: 400; font-style: normal; }}"
    if font_700:
        css += f"@font-face {{ font-family: 'Rawline'; src: url('data:font/ttf;base64,{font_700}') format('truetype'); font-weight: 700; font-style: normal; }}"
    if not css:
        return "@import url('https://cdntgr.servicos.gov.br/fonts/rawline/rawline.css');"
    return css

# --- Aplica o fundo personalizado com sobreposição ---
def set_background(png_file):
    bin_str = get_base64(png_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), url("data:image/jpeg;base64,{bin_str}");
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
        font-family: 'Rawline', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }}

    [data-testid="stIconMaterial"],
    .material-symbols-rounded,
    span[class*="material-symbols"],
    .material-icons {{
        font-family: 'Material Symbols Rounded', 'Material Icons' !important;
    }}

    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp p, .stApp span, .stApp div, .stApp a, .stApp li,
    .stApp label, .stApp table, .stApp th, .stApp td,
    [data-testid="stMarkdownContainer"],
    [data-testid="stWidgetLabel"] {{
        color: #FFFFFF !important;
    }}

    /* Container principal */
    .block-container {{
        max-width: 950px !important;
        margin-left: 0 !important;
        margin-right: auto !important;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }}

    /* ===== TÍTULO compacto (ajuste 3) ===== */
    .titulo-esquerda {{
        text-align: left !important;
        color: #FFFFFF !important;
        font-weight: 700;
        font-size: 1.3rem;
        line-height: 1.3;
        margin: 0 0 0.15rem 0;
        text-shadow: 0 2px 6px rgba(0, 0, 0, 0.9);
    }}

    .subtitulo-esquerda {{
        text-align: left !important;
        color: #94A3B8 !important;
        font-weight: 400;
        font-size: 0.8rem;
        margin: 0 0 0.9rem 0;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.9);
    }}

    hr {{
        border-color: #475569 !important;
        opacity: 0.6;
        margin: 0.8rem 0 !important;
    }}

    /* ===== ITEM DA LISTA ===== */
    a.app-item {{
        display: block !important;
        width: 100% !important;
        padding: 0.6rem 0.95rem !important;
        margin-bottom: 0.4rem !important;
        background: rgba(45, 48, 56, 0.78) !important;
        backdrop-filter: blur(6px) !important;
        border: none !important;
        border-radius: 8px !important;
        box-shadow: none !important;
        color: #E2E8F0 !important;
        font-size: 0.95rem !important;
        font-weight: 400 !important;
        text-align: left !important;
        text-decoration: none !important;
        transition: background 0.2s ease !important;
    }}

    a.app-item:hover {{
        background: rgba(75, 80, 92, 0.95) !important;
        color: #FFFFFF !important;
        text-decoration: none !important;
    }}

    /* ===== Caixa de instrução DESTACADA e COMPACTA (ajuste 2) ===== */
    .fake-search {{
        display: block;
        max-width: 460px;   /* compacta, não estica */
        width: 100%;
        padding: 0.7rem 0.9rem;
        margin: 0 0 1.2rem 0;

        background: linear-gradient(135deg, rgba(37, 99, 235, 0.35), rgba(59, 130, 246, 0.25)) !important;
        border: 1px solid rgba(96, 165, 250, 0.6) !important;
        border-left: 4px solid #3B82F6 !important;
        border-radius: 8px;

        color: #DBEAFE !important;
        font-size: 0.9rem;
        font-weight: 600 !important;
        letter-spacing: 0.2px;

        box-shadow: 0 0 12px rgba(59, 130, 246, 0.35) !important;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.6);
    }}

    .rodape-custom {{
        text-align: left;
        color: #94A3B8 !important;
        font-size: 11px;
        margin-top: 2rem;
        font-weight: 400;
        line-height: 1.5;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.9);
    }}
</style>
""", unsafe_allow_html=True)

# --- Título e subtítulo (ajuste 3) ---
st.markdown('<h1 class="titulo-esquerda">🏫 Gerenciamento Escolar</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo-esquerda">Painel de atalhos • Uso interno</p>', unsafe_allow_html=True)

# --- Caixa de instrução (ajuste 2 - compacta) ---
st.markdown('<div class="fake-search">📋 Selecione um dos aplicativos abaixo</div>', unsafe_allow_html=True)

# --- Dicionário de Aplicativos ---
apps = {
    "Apura Resultado": {"url": "https://apura-resultado-final.streamlit.app/"},
    "Avaliação Especial": {"url": "https://avaliacaoespecialcontagem.streamlit.app/"},
    "Bolsa Família": {"url": "https://bolsafamilia2.streamlit.app/"},
    "Contagem de Aulas": {"url": "https://contagemdeaulasnosiea.streamlit.app/"},
    "Criação Horário": {"url": "https://sistemadecriacaodehorarioescolar.streamlit.app/"},
    "Pontuação SGE": {"url": "https://conceitosnosge.streamlit.app/"},
    "Solicitação Vagas - QR": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html"},
    "Solicitação Vagas - Participante": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html"},
    "Solicitação Vagas - Secretaria": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html"},
    "Verificar Aulas Faltam": {"url": "https://aulasprevistasxaulasrealizadas.streamlit.app/"},
    "Verificar Notas": {"url": "https://verificarnotasembranconosdiarios.streamlit.app/"},
}

# --- Listas controladas manualmente (ajuste 1) ---
# Coluna esquerda: apps gerais
coluna_esquerda = [
    "Apura Resultado",
    "Avaliação Especial",
    "Bolsa Família",
    "Contagem de Aulas",
    "Criação Horário",
    "Pontuação SGE",
]

# Coluna direita: Solicitação de Vagas (agrupadas) + Verificações
coluna_direita = [
    "Solicitação Vagas - Participante",
    "Solicitação Vagas - QR",
    "Solicitação Vagas - Secretaria",
    "Verificar Aulas Faltam",
    "Verificar Notas",
]

# --- Renderização em 2 colunas ---
col_esq, col_dir = st.columns([1, 1])

with col_esq:
    for nome in coluna_esquerda:
        st.markdown(
            f'<a class="app-item" href="{apps[nome]["url"]}" target="_blank" rel="noopener noreferrer">{nome}</a>',
            unsafe_allow_html=True
        )

with col_dir:
    for nome in coluna_direita:
        st.markdown(
            f'<a class="app-item" href="{apps[nome]["url"]}" target="_blank" rel="noopener noreferrer">{nome}</a>',
            unsafe_allow_html=True
        )

# --- Rodapé ---
st.markdown("""
<p class='rodape-custom'>
<br>
Aplicativos desenvolvidos por André Torres<br>
© 2026 • Todos os direitos reservados<br>
📧 andretorres.adm@gmail.com
</p>
""", unsafe_allow_html=True)