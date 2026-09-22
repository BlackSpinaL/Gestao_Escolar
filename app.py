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
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: top center;
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
        st.warning("⚠️ Imagem de fundo não encontrada! Verifique se o arquivo 'fundo.jpg' ou 'fundo.png' está no GitHub com o nome exato.")

# --- CSS Personalizado Adaptado para Tema Dourado ---
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
    [data-testid="stWidgetLabel"],
    [data-testid="stLinkButton"] a {
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
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* ===== TÍTULO E SUBTÍTULO CENTRALIZADOS COM GLOW DOURADO ===== */
    .titulo-central {
        text-align: center !important;
        color: #FFFFFF !important;
        font-family: 'Rawline', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-weight: 800;
        font-size: 2.5rem;
        line-height: 1.25;
        margin: 0 0 0.4rem 0;
        /* Efeito de contorno e brilho dourado */
        text-shadow: 
            -1px -1px 0 #D97706,  
             1px -1px 0 #D97706,
            -1px  1px 0 #D97706,
             1px  1px 0 #D97706,
             0 0 12px rgba(245, 158, 11, 0.8);
    }

    .subtitulo-central {
        text-align: center !important;
        color: #FEF3C7 !important;
        font-family: 'Rawline', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-weight: 500;
        font-size: 1.1rem;
        margin: 0 0 1.2rem 0;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.9);
    }

    /* Linha divisória em dourado brilhante */
    hr {
        border-color: #F59E0B !important;
        box-shadow: 0 0 8px rgba(245, 158, 11, 0.6);
        opacity: 0.9;
    }

    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
    }

    /* ===== CARTÕES COM DETALHES DOURADOS ===== */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        height: 230px !important;
        display: flex;
        flex-direction: column;
        justify-content: space-between;

        background-color: rgba(15, 15, 15, 0.75) !important;
        backdrop-filter: blur(10px);
        border-radius: 12px;
        border: 1px solid rgba(245, 158, 11, 0.4) !important;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.6);
        transition: all 0.3s ease;
        padding: 1.2rem 1rem;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(245, 158, 11, 0.4);
        border-color: #FBBF24 !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        display: flex;
        flex-direction: column;
        height: 100%;
        justify-content: space-between;
    }

    /* Título do cartão com contorno dourado */
    .card-titulo {
        min-height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: #FFFFFF !important;
        font-size: 1.15rem;
        font-weight: 700;
        line-height: 1.3;
        margin: 0 0 0.8rem 0;
        text-shadow: 
            -1px -1px 0 #B45309,  
             1px -1px 0 #B45309,
            -1px  1px 0 #B45309,
             1px  1px 0 #B45309,
             0 0 8px rgba(245, 158, 11, 0.6);
    }

    .stLinkButton {
        margin-top: auto !important;
    }

    /* ===== BOTÕES EM DOURADO ===== */
    .stLinkButton > a {
        background: linear-gradient(135deg, #D97706 0%, #B45309 100%) !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: 1px solid #FBBF24 !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        padding: 0.5rem 1rem !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.8) !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
    }

    .stLinkButton > a:hover {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        color: #FFFFFF !important;
        border-color: #FEF08A !important;
        box-shadow: 0 0 12px rgba(245, 158, 11, 0.8);
        transform: scale(1.02);
    }

    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }

    .rodape-custom {
        text-align: center;
        color: #FDE68A !important;
        font-family: 'Rawline', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 14px;
        margin-top: 2rem;
        font-weight: normal;
        line-height: 1.6;
        text-shadow: 0 1px 4px rgba(0, 0, 0, 0.9);
    }
</style>
""", unsafe_allow_html=True)

# --- Título e Instruções ---
st.markdown(
    '<h1 class="titulo-central">🏫 Sistema de Gerenciamento Escolar</h1>',
    unsafe_allow_html=True
)
st.markdown(
    '<p class="subtitulo-central">Selecione uma ferramenta para começar (abrirá em nova aba):</p>',
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
    "Solicitação de Vagas - Secretaria": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html", "icone": "🏢"},
    "Solicitação de Vagas - Participante": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html", "icone": "👤"},
    "Solicitação de Vagas - QR Code": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html", "icone": "📱"},
}

# Cria as colunas para os botões (3 colunas)
cols = st.columns(3)

for i, (nome, info) in enumerate(apps.items()):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(
                f'<div class="card-titulo">{info["icone"]} {nome}</div>',
                unsafe_allow_html=True
            )
            st.link_button("Acessar Aplicativo", info['url'], use_container_width=True)

# --- Rodapé ---
st.markdown("""
<p class='rodape-custom'>
    Desenvolvido por André Torres<br>
    e-mail: andretorres.adm@gmail.com<br>
    para otimizar a gestão escolar.
</p>
""", unsafe_allow_html=True)