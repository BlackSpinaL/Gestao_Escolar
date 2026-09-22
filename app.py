import streamlit as st
import base64

# Configuração da página (Layout wide)
st.set_page_config(page_title="Painel de Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

# --- Função para carregar a imagem de fundo em Base64 ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- Aplica o fundo personalizado (Imagem de fundo mais visível) ---
def set_background(png_file):
    try:
        bin_str = get_base64(png_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            /* Reduzido de 0.88 para 0.35 para a imagem aparecer bem mais */
            background-image: linear-gradient(rgba(250, 246, 239, 0.35), rgba(250, 246, 239, 0.35)), url("data:image/jpeg;base64,{bin_str}");
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

    /* Preserva a fonte dos ícones nativos do Streamlit */
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

    /* 2. ALTURA FIXA para todos os cartões ficarem perfeitamente alinhados */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        height: 230px !important;          /* Altura fixa — todos iguais */
        display: flex;
        flex-direction: column;
        justify-content: space-between;

        background-color: #ffffff;
        border-radius: 12px;
        border: 1px solid #E6DCCF;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        padding: 1.2rem 1rem;
    }

    /* Efeito ao passar o mouse no cartão */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 20px -3px rgba(30, 58, 138, 0.2);
        border-color: #1E3A8A;
    }

    /* 3. Bloco interno com altura 100% e distribuição equilibrada */
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        display: flex;
        flex-direction: column;
        height: 100%;
        justify-content: space-between;
    }

    /* 4. Título dos cartões — área com altura fixa para não desalinhar */
    .card-titulo {
        min-height: 80px;              /* Garante alinhamento mesmo com 1 ou 2 linhas */
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: #1E3A8A !important;
        font-size: 1.15rem;
        font-weight: 700;
        line-height: 1.3;
        margin: 0 0 0.8rem 0;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }

    /* 5. Empurra o botão para a base do cartão */
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
        padding: 0.5rem 1rem !important;
    }

    .stLinkButton > a:hover {
        background-color: #3B82F6 !important;
        color: white !important;
    }

    /* Títulos em Azul Escuro */
    h1, h2, h3, h4, h5, h6 {
        color: #1E3A8A !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }

    /* 6. Estilo do Rodapé */
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

# Cria as colunas para os botões (3 colunas = 3x3 perfeito para 9 apps)
cols = st.columns(3)

for i, (nome, info) in enumerate(apps.items()):
    with cols[i % 3]:
        with st.container(border=True):
            # Título dentro de um div com altura mínima fixa (evita desalinhamento)
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