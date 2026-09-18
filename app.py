import streamlit as st
import base64

# Configuração da página (Layout wide para aproveitar melhor a tela)
st.set_page_config(page_title="Painel de Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

# --- Função para carregar a imagem de forma segura ---
def carregar_banner(caminho_imagem):
    try:
        with open(caminho_imagem, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode()
        # Descobre se é jpg ou png para o tipo correto
        tipo = "jpeg" if caminho_imagem.endswith(".jpg") else "png"
        return f'''
        <div style="display: flex; justify-content: center; margin-bottom: 2rem;">
            <img src="data:image/{tipo};base64,{img_base64}" style="width: 100%; max-width: 1100px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
        </div>
        '''
    except FileNotFoundError:
        return None

# --- CSS Personalizado (Cores extraídas da imagem) ---
st.markdown("""
<style>
    /* 1. Fundo do painel em bege bem clarinho (combina com a imagem) */
    .stApp {
        background-color: #FAF6EF;
    }
    
    /* 2. Ajuste do container principal */
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    
    /* 3. Estilo dos Cartões */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff;
        border-radius: 12px;
        border: 1px solid #E6DCCF; /* Borda bege sutil */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        padding: 1rem;
    }
    
    /* Efeito ao passar o mouse no cartão */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 20px -3px rgba(30, 58, 138, 0.15); /* Sombra azulada */
        border-color: #1E3A8A;
    }
    
    /* 4. Estilo dos Botões (Azul escuro igual ao texto da imagem) */
    .stLinkButton > a {
        background-color: #1E3A8A !important; 
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
        transition: background-color 0.2s !important;
    }
    
    /* Efeito ao passar o mouse no botão */
    .stLinkButton > a:hover {
        background-color: #3B82F6 !important; /* Azul mais claro */
        color: white !important;
    }
    
    /* 5. Títulos em Azul Escuro */
    h1, h2, h3 {
        color: #1E3A8A !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Banner no Topo ---
# Tenta carregar 'fundo.jpg', se não achar tenta 'fundo.png'
banner_html = carregar_banner("fundo.jpg")
if not banner_html:
    banner_html = carregar_banner("fundo.png")

if banner_html:
    st.markdown(banner_html, unsafe_allow_html=True)
else:
    st.warning("⚠️ Imagem de banner não encontrada! Verifique se o arquivo 'fundo.jpg' ou 'fundo.png' foi enviado para o GitHub com o nome exato.")

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

# Cria as colunas para os botões (3 colunas)
cols = st.columns(3)

for i, (nome, info) in enumerate(apps.items()):
    with cols[i % 3]:
        with st.container(border=True):
            st.subheader(f"{info['icone']} {nome}")
            st.link_button("Acessar Aplicativo", info['url'], use_container_width=True)

# --- Rodapé ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8C7A6B;'>Desenvolvido para otimizar a gestão escolar.</p>", unsafe_allow_html=True)
