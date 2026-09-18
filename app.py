import streamlit as st
import base64

# Configuração da página
st.set_page_config(page_title="Painel de Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

# Função para carregar a imagem de fundo
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Aplica o fundo personalizado
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-position: center top;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    /* Deixa o conteúdo mais legível sobre a imagem */
    .block-container {
        background-color: rgba(255, 255, 255, 0.90);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Tenta carregar a imagem de fundo
try:
    set_background('fundo.jpg') # Mude para .jpg se você converter a imagem
except:
    try:
        set_background('fundo.png') # Mantém o png caso não tenha convertido ainda
    except:
        st.warning("Imagem de fundo não encontrada. Usando fundo padrão.")

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

# --- TELA DO PAINEL (MENU) ---
st.title("🏫 Sistema de Gerenciamento Escolar")
st.markdown("### Selecione uma ferramenta para começar (abrirá em nova aba):")
st.markdown("---")

# Cria as colunas para os botões (3 colunas)
cols = st.columns(3)

for i, (nome, info) in enumerate(apps.items()):
    with cols[i % 3]:
        # Cria um container visual para cada botão
        with st.container(border=True):
            st.subheader(f"{info['icone']} {nome}")
            # st.link_button abre o link em uma nova aba automaticamente
            st.link_button("Acessar Aplicativo", info['url'], use_container_width=True)
