import streamlit as st
import base64

# Configuração da página (Layout wide)
st.set_page_config(page_title="Painel de Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

# --- Função para carregar a imagem de fundo em Base64 ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- Aplica o fundo personalizado com sobreposição (Overlay) ---
def set_background(png_file):
    try:
        bin_str = get_base64(png_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(250, 246, 239, 0.88), rgba(250, 246, 239, 0.88)), url("data:image/jpeg;base64,{bin_str}");
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

# --- CSS Personalizado ---
st.markdown("""
<style>
    /* ===== FONTE RAWLINE (CDN do Design System gov.br) ===== */
    @import url('https://cdntgr.servicos.gov.br/fonts/rawline/rawline.css');

    /* Aplica Rawline em TODOS os textos do app */
    html, body, .stApp,
    .stApp p, .stApp span, .stApp div, .stApp a, .stApp li,
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp button, .stApp input, .stApp textarea, .stApp select,
    .stApp label, .stApp table, .stApp th, .stApp td,
    [data-testid="stMarkdownContainer"],
    [data-testid="stWidgetLabel"],
    [data-testid="stLinkButton"] a {
        font-family: 'Rawline', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* Preserva a fonte dos ícones nativos do Streamlit (não remover!) */
    [data-testid="stIconMaterial"],
    .material-symbols-rounded,
    span[class*="material-symbols"] {
        font-family: 'Material Symbols Rounded' !important;
    }

    /* Ajuste do container principal */
    .block-container {
        max-width: 1400px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* ===== TÍTULO E SUBTÍTULO CENTRALIZADOS ===== */
    .titulo-central {
        text-align: center !important;
        color: #1E3A8A !important;
        font-family: 'Rawline', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-weight: 700;
        font-size: 2.4rem;
        line-height: 1.25;
        margin: 0 0 0.4rem 0;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
    }

    .subtitulo-central {
        text-align: center !important;
        color: #1E3A8A !important;
        font-family: 'Rawline', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-weight: 500;
        font-size: 1.1rem;
        margin: 0 0 1.2rem 0;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
    }

    /* 1. Força a coluna a se esticar para ocupar toda a altura disponível */
    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
    }

    /* 2. Força o cartão (com borda) a preencher todo o espaço da coluna */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* Empurra o conteúdo para cima e o botão para baixo */

        background-color: #ffffff;
        border-radius: 12px;
        border: 1px solid #E6DCCF;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        padding: 1.5rem 1rem;
        min-height: 200px; /* Altura mínima para manter o padrão visual */
    }

    /* Efeito ao passar o mouse no cartão */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 20px -3px rgba(30, 58, 138, 0.2);
        border-color: #1E3A8A;
    }

    /* 3. Garante que o bloco interno do Streamlit ocupe 100% da altura */
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        display: flex;
        flex-direction: column;
        height: 100%;
        justify-content: space-between;
    }

    /* 4. Empurra o botão para a base do cartão */
    .stLinkButton {
        margin-top: auto !important;
    }

    /* Estilo dos Botões (Azul escuro) */
    .stLinkButton > a {
        background-color: #1E3A8A !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
        transition: background-color 0.2s !important;
    }

    .stLinkButton > a:hover {
        background-color: #3B82F6 !important;
        color: white !important;
    }

    /* Títulos em Azul Escuro (cabeçalhos dos cartões) */
    h1, h2, h3, h4, h5, h6 {
        color: #1E3A8A !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }

    /* 5. Estilo do Rodapé */
    .rodape-custom {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Rawline', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 14px;
        margin-top: 2rem;
        font-weight: normal;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# --- Título e Instruções (CENTRALIZADOS) ---
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
    "Aulas no Siea": {"url": "https://aulasnosiea.streamlit.app/", "icone": "📚"},
    "Avaliação Especial": {"url": "https://avaliacaoespecial.streamlit.app/", "icone": "📝"},
    "Bolsa Família": {"url": "https://bolsa-familia.streamlit.app/", "icone": "💰"},
    "Pontuação no SGE": {"url": "https://pontuacaonosge.streamlit.app/", "icone": "📊"},
    "Verificar Notas nos Diários": {"url": "https://verificarnotasnosdiarios.streamlit.app/", "icone": "📓"},
    "Solicitação de Vagas - Secretaria": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html", "icone": "🏢"},
    "Solicitação de Vagas - Participante": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html", "icone": "👤"},
    "Solicitação de Vagas - QR Code": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html", "icone": "📱"},
}

# Cria as colunas para os botões (4 colunas)
cols = st.columns(4)

for i, (nome, info) in enumerate(apps.items()):
    with cols[i % 4]:
        with st.container(border=True):
            st.subheader(f"{info['icone']} {nome}")
            st.link_button("Acessar Aplicativo", info['url'], use_container_width=True)

# --- Rodapé ---
st.markdown("""
<p class='rodape-custom'>
    Desenvolvido por André Torres<br>
    e-mail: andretorres.adm@gmail.com<br>
    para otimizar a gestão escolar.
</p>
""", unsafe_allow_html=True)
