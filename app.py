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
        css += f"""
        @font-face {{
            font-family: 'Rawline';
            src: url('data:font/ttf;base64,{font_300}') format('truetype');
            font-weight: 300;
            font-style: normal;
        }}
        """
    if font_400:
        css += f"""
        @font-face {{
            font-family: 'Rawline';
            src: url('data:font/ttf;base64,{font_400}') format('truetype');
            font-weight: 400;
            font-style: normal;
        }}
        """
    if font_700:
        css += f"""
        @font-face {{
            font-family: 'Rawline';
            src: url('data:font/ttf;base64,{font_700}') format('truetype');
            font-weight: 700;
            font-style: normal;
        }}
        """
    
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
            background-image: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)), url("data:image/jpeg;base64,{bin_str}");
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
        st.warning("⚠️ Imagem de fundo não encontrada! Verifique se 'fundo.jpg' ou 'fundo.png' está na pasta do projeto.")

# --- Carrega o CSS da fonte ---
font_css = get_font_face_css()

# --- CSS Personalizado Adaptado para Tema Cinza/Grafite ---
st.markdown(f"""
<style>
    /* ===== FONTE RAWLINE ===== */
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

    /* Container principal - alinhado à esquerda e com largura controlada */
    .block-container {{
        max-width: 900px !important;
        margin-left: 0 !important;
        margin-right: auto !important;
        padding-top: 2.5rem;
        padding-bottom: 2.5rem;
        padding-left: 2rem;
    }}

    /* ===== TÍTULO E SUBTÍTULO ===== */
    .titulo-central {{
        text-align: center !important;
        color: #FFFFFF !important;
        font-weight: 700;
        font-size: 2.5rem;
        line-height: 1.25;
        margin: 0 0 0.4rem 0;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.9);
    }}

    .subtitulo-central {{
        text-align: center !important;
        color: #CBD5E1 !important;
        font-weight: 400;
        font-size: 1.1rem;
        margin: 0 0 1.2rem 0;
        text-shadow: 0 2px 6px rgba(0, 0, 0, 0.9);
    }}

    hr {{
        border-color: #64748B !important;
        box-shadow: 0 0 8px rgba(255, 255, 255, 0.2);
        opacity: 0.8;
    }}

    /* ===== CARD-LINK (Lista vertical, alinhado à esquerda) ===== */
    a.app-card {{
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        gap: 0.8rem !important;

        width: 100% !important;
        min-height: 50px !important;
        padding: 0.8rem 1.2rem !important;
        margin-bottom: 0.5rem !important;

        background: rgba(24, 28, 36, 0.88) !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(148, 163, 184, 0.35) !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4) !important;

        color: #FFFFFF !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
    }}

    a.app-card:hover {{
        transform: translateX(5px) !important;
        border-color: #CBD5E1 !important;
        background: rgba(38, 45, 56, 0.95) !important;
        box-shadow: 0 8px 16px rgba(255, 255, 255, 0.15) !important;
        text-decoration: none !important;
    }}

    a.app-card .check-icon {{
        font-size: 1.2rem !important;
        color: #22C55E !important;
        flex-shrink: 0 !important;
        text-shadow: 0 0 8px rgba(34, 197, 94, 0.6) !important;
        transition: transform 0.3s ease !important;
    }}

    a.app-card:hover .check-icon {{
        transform: scale(1.15) !important;
    }}

    a.app-card .app-name {{
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        line-height: 1.3 !important;
        text-align: left !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8) !important;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: #FFFFFF !important;
    }}

    /* Rodapé */
    .rodape-custom {{
        text-align: center;
        color: #94A3B8 !important;
        font-size: 14px;
        margin-top: 2.5rem;
        font-weight: 400;
        line-height: 1.6;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.9);
    }}
</style>
""", unsafe_allow_html=True)

# --- Título e Subtítulo ---
st.markdown(
    '<h1 class="titulo-central">🏫 Sistema de Gerenciamento Escolar 🏫</h1>',
    unsafe_allow_html=True
)
st.markdown(
    '<p class="subtitulo-central">Clique em um aplicativo para abri-lo em uma nova aba: ✅</p>',
    unsafe_allow_html=True
)
st.markdown("---")

# --- Dicionário de Aplicativos ---
apps = {
    "Apura Resultado": {"url": "https://apura-resultado-final.streamlit.app/", "icone": "🏆"},
    "Avaliação Especial": {"url": "https://avaliacaoespecialcontagem.streamlit.app/", "icone": "📝"},
    "Bolsa Família": {"url": "https://bolsafamilia2.streamlit.app/", "icone": "💰"},
    "Contagem de Aulas no Siea": {"url": "https://contagemdeaulasnosiea.streamlit.app/", "icone": "📚"},
    "Criação de Horário Escolar": {"url": "https://sistemadecriacaodehorarioescolar.streamlit.app/", "icone": "📅"},
    "Pontuação no SGE": {"url": "https://conceitosnosge.streamlit.app/", "icone": "📊"},
    "Solicitação de Vagas - Participante": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html", "icone": "👤"},
    "Solicitação de Vagas - QR Code": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html", "icone": "📱"},
    "Solicitação de Vagas - Secretaria": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html", "icone": "🏢"},
    "Verificar Aulas que Faltam nos Diários": {"url": "https://aulasprevistasxaulasrealizadas.streamlit.app/", "icone": "🔎"},
    "Verificar Notas em Branco nos Diários": {"url": "https://verificarnotasembranconosdiarios.streamlit.app/", "icone": "📓"}, 
}

# --- Layout em 1 coluna (Lista Vertical) ---
for nome, info in sorted(apps.items()):
    st.markdown(
        f'''
        <a class="app-card" href="{info['url']}" target="_blank" rel="noopener noreferrer">
            <span class="check-icon">✔</span>
            <span class="app-name">{info['icone']} {nome}</span>
        </a>
        ''',
        unsafe_allow_html=True
    )

# --- Rodapé ---
st.markdown("""
<p class='rodape-custom'>
<br>
Aplicativos desenvolvidos por André Torres • Gestão escolar eficiente, organizada e prática. 🏫💻⚙️🚀<br>
© 2026 • Todos os direitos reservados • 📧 andretorres.adm@gmail.com <br>    
</p>
""", unsafe_allow_html=True)