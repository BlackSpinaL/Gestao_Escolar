import streamlit as st

# Configuração da página
st.set_page_config(page_title="Painel de Gerenciamento Escolar", layout="centered", initial_sidebar_state="collapsed")

# --- CSS Personalizado (O segredo do visual) ---
st.markdown("""
<style>
    /* 1. Fundo em degradê azul suave (combina com a imagem) */
    .stApp {
        background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%);
    }
    
    /* 2. Ajuste do container principal */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }
    
    /* 3. Estilo dos Cartões (onde ficam os botões) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff;
        border-radius: 12px;
        border: 1px solid #bcccdc; /* Borda azul clara */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
    }
    
    /* Efeito ao passar o mouse no cartão */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border-color: #1E3A8A; /* Borda azul escura ao passar o mouse */
    }
    
    /* 4. Estilo dos Botões (Azul escuro combinando com a imagem) */
    .stLinkButton > a {
        background-color: #1E3A8A !important; /* Azul escuro */
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
    
    /* 5. Título principal */
    h1 {
        color: #1E3A8A !important;
        font-weight: 700 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Banner no Topo ---
# Certifique-se de que a imagem está no repositório com o nome 'fundo.jpg' ou 'fundo.png'
try:
    # Tenta carregar a imagem e aplica uma borda arredondada nela via HTML
    st.image("fundo.jpg", use_container_width=True)
except:
    try:
        st.image("fundo.png", use_container_width=True)
    except:
        st.warning("Imagem de banner não encontrada. Verifique se o arquivo 'fundo.jpg' está no repositório.")

st.markdown("<br>", unsafe_allow_html=True)

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
        # Cria um container visual para cada botão
        with st.container(border=True):
            st.subheader(f"{info['icone']} {nome}")
            # st.link_button abre o link em uma nova aba automaticamente
            st.link_button("Acessar Aplicativo", info['url'], use_container_width=True)

# --- Rodapé ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B;'>Desenvolvido para otimizar a gestão escolar.</p>", unsafe_allow_html=True)
