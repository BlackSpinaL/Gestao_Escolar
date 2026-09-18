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
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    /* Deixa o conteúdo mais legível sobre a imagem */
    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Chame a função passando o nome da sua imagem
# Certifique-se de que a imagem 'fundo.png' está na mesma pasta
try:
    set_background('fundo.png')
except:
    st.warning("Imagem de fundo 'fundo.png' não encontrada. Usando fundo padrão.")

# --- Dicionário de Aplicativos ---
# Aqui você organiza seus apps. 
# 'tipo': 'streamlit' para apps do streamlit, 'html' para os links do GitHub Pages
apps = {
    "Aulas no Siea": {"url": "https://aulasnosiea.streamlit.app/", "tipo": "streamlit", "icone": "📚"},
    "Avaliação Especial": {"url": "https://avaliacaoespecial.streamlit.app/", "tipo": "streamlit", "icone": "📝"},
    "Bolsa Família": {"url": "https://bolsa-familia.streamlit.app/", "tipo": "streamlit", "icone": "💰"},
    "Pontuação no SGE": {"url": "https://pontuacaonosge.streamlit.app/", "tipo": "streamlit", "icone": "📊"},
    "Verificar Notas nos Diários": {"url": "https://verificarnotasnosdiarios.streamlit.app/", "tipo": "streamlit", "icone": "📓"},
    "Solicitação de Vagas - Secretaria": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html", "tipo": "html", "icone": "🏢"},
    "Solicitação de Vagas - Participante": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html", "tipo": "html", "icone": "👤"},
    "Solicitação de Vagas - QR Code": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html", "tipo": "html", "icone": "📱"},
}

# Inicializa o estado da sessão para controlar qual app está aberto
if 'app_atual' not in st.session_state:
    st.session_state.app_atual = None

# --- TELA INICIAL (MENU) ---
if st.session_state.app_atual is None:
    st.title("🏫 Sistema de Gerenciamento Escolar")
    st.markdown("### Selecione uma ferramenta para começar:")
    st.markdown("---")

    # Cria as colunas para os botões (3 colunas)
    cols = st.columns(3)
    
    for i, (nome, info) in enumerate(apps.items()):
        with cols[i % 3]:
            # Cria um container visual para cada botão
            with st.container(border=True):
                st.subheader(f"{info['icone']} {nome}")
                if st.button(f"Acessar {nome}", use_container_width=True, key=f"btn_{nome}"):
                    st.session_state.app_atual = nome
                    st.rerun()

# --- TELA DO APLICATIVO ABERTO ---
else:
    nome_app = st.session_state.app_atual
    info_app = apps[nome_app]
    
    # Cabeçalho com botão de voltar
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("⬅️ Voltar ao Painel", use_container_width=True):
            st.session_state.app_atual = None
            st.rerun()
    with col2:
        st.subheader(f"{info_app['icone']} {nome_app}")

    st.markdown("---")

    # Renderiza o aplicativo escolhido
    if info_app['tipo'] == 'streamlit':
        # Para apps do Streamlit, usamos um iframe grande
        st.components.v1.iframe(info_app['url'], height=800, scrolling=True)
    else:
        # Para os links do GitHub Pages (HTML)
        st.components.v1.iframe(info_app['url'], height=800, scrolling=True)
        
    # Botão de voltar extra no final da página
    st.markdown("---")
    if st.button("⬅️ Voltar ao Painel Principal", use_container_width=True):
        st.session_state.app_atual = None
        st.rerun()