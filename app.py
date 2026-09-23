import streamlit as st
import base64

# Configuração da página (Layout wide)
st.set_page_config(page_title="Painel de Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

# --- Função para carregar a imagem de fundo em Base64 ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- Aplica o fundo personalizado com sobreposição ---
def set_background(png_file):
    try:
        bin_str = get_base64(png_file)
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
    except FileNotFoundError:
        return False

if not set_background('fundo.jpg'):
    if not set_background('fundo.png'):
        st.warning("⚠️ Imagem de fundo não encontrada! Verifique se 'fundo.jpg' ou 'fundo.png' está na pasta do projeto.")

# --- CSS Personalizado Adaptado para Tema Cinza/Grafite ---
st.markdown("""
<style>
    /* ===== FONTE RAWLINE ===== */
    @import url('https://cdntgr.servicos.gov.br/fonts/rawline/rawline.css');

    html, body, .stApp,
    .stApp p, .stApp span, .stApp div, .stApp a, .stApp li,
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp button, .stApp input, .stApp textarea, .stApp select,
    .stApp label, .stApp table, .stApp th, .stApp td,
    [data-testid="stMarkdownContainer"],
    [data-testid="stWidgetLabel"] {
        font-family: 'Rawline', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        color: #FFFFFF !important;
    }

    [data-testid="stIconMaterial"],
    .material-symbols-rounded,
    span[class*="material-symbols"] {
        font-family: 'Material Symbols Rounded' !important;
    }

    /* Container principal */
    .block-container {
        max-width: 1400px;
        padding-top: 2.5rem;
        padding-bottom: 2.5rem;
    }

    /* ===== TÍTULO E SUBTÍTULO ===== */
    .titulo-central {
        text-align: center !important;
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 2.5rem;
        line-height: 1.25;
        margin: 0 0 0.4rem 0;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.9);
    }

    .subtitulo-central {
        text-align: center !important;
        color: #CBD5E1 !important;
        font-weight: 500;
        font-size: 1.1rem;
        margin: 0 0 1.2rem 0;
        text-shadow: 0 2px 6px rgba(0, 0, 0, 0.9);
    }

    /* Linha divisória em cinza prateado */
    hr {
        border-color: #64748B !important;
        box-shadow: 0 0 8px rgba(255, 255, 255, 0.2);
        opacity: 0.8;
    }

    /* ===== CARD-LINK (substitui o botão) ===== */
    a.app-card {
        display: flex !important;
        align-items: center !important;
        gap: 1rem !important;

        width: 100% !important;
        min-height: 90px !important;
        padding: 1.2rem 1.5rem !important;
        margin-bottom: 1rem !important;

        background: rgba(24, 28, 36, 0.88) !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(148, 163, 184, 0.35) !important;
        border-radius: 12px !important;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.6) !important;

        color: #FFFFFF !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
    }

    a.app-card:hover {
        transform: translateY(-4px) !important;
        border-color: #CBD5E1 !important;
        background: rgba(38, 45, 56, 0.95) !important;
        box-shadow: 0 12px 24px rgba(255, 255, 255, 0.15) !important;
        text-decoration: none !important;
    }

    a.app-card .check-icon {
        font-size: 1.8rem !important;
        color: #22C55E !important;               /* ✔ verde */
        flex-shrink: 0 !important;
        text-shadow: 0 0 8px rgba(34, 197, 94, 0.6) !important;
        transition: transform 0.3s ease !important;
    }

    a.app-card:hover .check-icon {
        transform: scale(1.15) !important;
    }

    a.app-card .app-name {
        font-size: 1.35rem !important;           /* fonte maior */
        font-weight: 700 !important;
        color: #FFFFFF !important;
        line-height: 1.3 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8) !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }

    /* Rodapé */
    .rodape-custom {
        text-align: center;
        color: #94A3B8 !important;
        font-size: 14px;
        margin-top: 2.5rem;
        font-weight: 500;
        line-height: 1.6;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.9);
    }
</style>
""", unsafe_allow_html=True)

# --- Título e Subtítulo ---
st.markdown(
    '<h1 class="titulo-central">🏫 Sistema de Gerenciamento Escolar</h1>',
    unsafe_allow_html=True
)
st.markdown(
    '<p class="subtitulo-central">Clique em um aplicativo para abrir em nova aba:</p>',
    unsafe_allow_html=True
)
st.markdown("---")

# --- Dicionário de Aplicativos ---
apps = {
    "Aulas no Siea": {"url": "https://contagemdeaulasnosiea.streamlit.app/", "icone": "📚"},
    "Avaliação Especial": {"url": "https://avaliacaoespecialcontagem.streamlit.app/", "icone": "📝"},
    "Bolsa Família": {"url": "https://bolsafamilia.streamlit.app/", "icone": "💰"},
    "Pontuação no SGE": {"url": "https://conceitosnosge.streamlit.app/", "icone": "📊"},
    "Verificar Notas nos Diários": {"url": "https://verificarnotasembranconosdiarios.streamlit.app/", "icone": "📓"},
    "Verificar Aulas Faltantes no Diário": {"url": "https://aulasprevistasxaulasrealizadas.streamlit.app/", "icone": "🔎"},
    "Apuração do Resultado Final": {"url": "https://apura-resultado-final.streamlit.app/", "icone": "🏆"},
    "Solicitação de Vagas - Secretaria": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html", "icone": "🏢"},
    "Solicitação de Vagas - Participante": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html", "icone": "👤"},
    "Solicitação de Vagas - QR Code": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html", "icone": "📱"},
}

# --- Layout em 2 colunas com cards-link clicáveis ---
cols = st.columns(2)

for i, (nome, info) in enumerate(apps.items()):
    with cols[i % 2]:
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
Aplicativos desenvolvidos para tornar a gestão escolar mais eficiente, organizada e prática. 🏫👨‍🎓🗃️📅🔎💻📱⚙️🔧🛠️🚀✅<br>
   © ® 2026 e-mail: andretorres.adm@gmail.com<br>    
</p>
""", unsafe_allow_html=True)