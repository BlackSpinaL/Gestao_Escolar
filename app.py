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
        # O truque está aqui: um gradiente bege semi-transparente (0.88) sobre a imagem
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

# Tenta carregar a imagem (fundo.jpg ou fundo.png)
if not set_background('fundo.jpg'):
    if not set_background('fundo.png'):
        st.warning("⚠️ Imagem de fundo não encontrada! Verifique se o arquivo 'fundo.jpg' ou 'fundo.png' está no GitHub com o nome exato.")

# --- CSS Personalizado para os Cartões, Botões e Rodapé ---
st.markdown("""
<style>
    /* Importa a fonte cursiva do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&display=swap');

    /* Ajuste do container principal */
    .block-container {
        max-width: 1400px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    /* Estilo dos Cartões (Fundo branco, altura igual e alinhamento flexível) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff;
        border-radius: 12px;
        border: 1px solid #E6DCCF;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        padding: 1.5rem 1rem;
        
        /* A MÁGICA ACONTECE AQUI: */
        min-height: 240px; /* Força todos os cartões a terem a mesma altura mínima */
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* Empurra o título para cima e o botão para baixo */
    }
    
    /* Efeito ao passar o mouse no cartão */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 20px -3px rgba(30, 58, 138, 0.2);
        border-color: #1E3A8A;
    }
    
    /* Garante que o botão fique sempre no final do cartão */
    div[data-testid="stLinkButton"] {
        margin-top: auto; 
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
    
    /* Títulos em Azul Escuro */
    h1, h2, h3 {
        color: #1E3A8A !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }

    /* Estilo do Rodapé Cursivo */
    .rodape-cursivo {
        text-align: center; 
        color: #1E3A8A; 
        font-family: 'Dancing Script', cursive; 
        font-size: 1.6rem; 
        margin-top: 2rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --- Título e Instruções ---
st.title("🏫 Sistema de Gerenciamento Escolar")
st.markdown("##### Selecione uma ferramenta para começar (abrirá em nova aba):")
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
<p class='rodape-cursivo'>
    Desenvolvido por André Torres<br>
    e-mail: andretorres.adm@gmail.com<br>
    para otimizar a gestão escolar.
</p>
""", unsafe_allow_html=True)
