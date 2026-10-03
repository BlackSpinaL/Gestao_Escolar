import streamlit as st
import base64

st.set_page_config(page_title="Sistema de Gerenciamento Escolar", layout="wide", initial_sidebar_state="collapsed")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def get_font_face_css():
    font_300 = get_base64('rawline-300.ttf')
    font_400 = get_base64('rawline-400.ttf')
    font_700 = get_base64('rawline-700.ttf')
    css = ""
    if font_300:
        css += f"@font-face {{ font-family: 'Rawline'; src: url('data:font/ttf;base64,{font_300}') format('truetype'); font-weight: 300; }}"
    if font_400:
        css += f"@font-face {{ font-family: 'Rawline'; src: url('data:font/ttf;base64,{font_400}') format('truetype'); font-weight: 400; }}"
    if font_700:
        css += f"@font-face {{ font-family: 'Rawline'; src: url('data:font/ttf;base64,{font_700}') format('truetype'); font-weight: 700; }}"
    if not css:
        return "@import url('https://cdntgr.servicos.gov.br/fonts/rawline/rawline.css');"
    return css

def set_background(png_file):
    bin_str = get_base64(png_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.80), rgba(0, 0, 0, 0.80)), url("data:image/jpeg;base64,{bin_str}");
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
        st.warning("⚠️ Imagem de fundo não encontrada!")

font_css = get_font_face_css()

st.markdown(f"""
<style>
    {font_css}

    html, body, .stApp, .stApp * {{
        font-family: 'Rawline', 'Segoe UI', Tahoma, sans-serif !important;
    }}

    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp p, .stApp span, .stApp div, .stApp a, .stApp li,
    .stApp label, [data-testid="stMarkdownContainer"],
    [data-testid="stWidgetLabel"] {{
        color: #FFFFFF !important;
    }}

    /* ===== Container mais estreito ===== */
    .block-container {{
        max-width: 980px !important;
        margin: 0 auto !important;
        padding-top: 1.8rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }}

    /* ===== TÍTULO ===== */
    .titulo-central {{
        text-align: center !important;
        color: #FFFFFF !important;
        font-weight: 700;
        font-size: 1.75rem;
        line-height: 1.25;
        margin: 0 0 0.5rem 0;
        letter-spacing: 0.3px;
        text-shadow: 0 2px 12px rgba(0, 0, 0, 1);
    }}

    /* ===== Subtítulo ===== */
    .subtitulo-central {{
        text-align: center !important;
        color: #CBD5E1 !important;
        font-weight: 400;
        font-size: 0.9rem;
        margin: 0 0 2.4rem 0;
        letter-spacing: 0.2px;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 1);
    }}

    /* ===== CARD ===== */
    a.app-card {{
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 1rem !important;

        width: 100% !important;
        min-height: 56px !important;
        padding: 0.75rem 1.15rem !important;
        margin-bottom: 0.55rem !important;

        background: rgba(45, 50, 60, 0.95) !important; 
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(203, 213, 225, 0.2) !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5) !important;

        color: #E2E8F0 !important;
        text-decoration: none !important;
        transition: all 0.22s ease !important;
    }}

    a.app-card:hover {{
        background: rgba(60, 65, 75, 1) !important;
        border-color: rgba(96, 165, 250, 0.8) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3) !important;
        text-decoration: none !important;
    }}

    a.app-card .app-name {{
        font-size: 1.05rem !important;
        font-weight: 500 !important;
        color: #E2E8F0 !important;
        line-height: 1.35 !important;
        text-align: left !important;
        flex: 1 !important;
        transition: color 0.22s ease !important;
    }}

    a.app-card:hover .app-name {{
        color: #FFFFFF !important;
    }}

    /* ===== ÍCONE SVG (Lucide/Phosphor) ===== */
    a.app-card svg {{
        width: 22px !important;
        height: 22px !important;
        color: #60A5FA !important;
        flex-shrink: 0 !important;
        transition: all 0.22s ease !important;
        opacity: 0.85 !important;
        stroke: currentColor !important;
        fill: none !important;
        stroke-width: 2 !important;
        stroke-linecap: round !important;
        stroke-linejoin: round !important;
    }}

    a.app-card:hover svg {{
        color: #93C5FD !important;
        opacity: 1 !important;
        transform: translateX(3px) !important;
    }}

    .rodape-minimo {{
        text-align: center;
        color: #94A3B8 !important;
        font-size: 12px;
        margin-top: 2.5rem;
        letter-spacing: 0.3px;
        line-height: 1.6;
        text-shadow: 0 1px 4px rgba(0, 0, 0, 1);
    }}

    .rodape-minimo strong {{
        color: #CBD5E1 !important;
        font-weight: 600;
    }}
</style>
""", unsafe_allow_html=True)

# --- Título ---
st.markdown('<h1 class="titulo-central">🏫 Sistema de Gerenciamento Escolar</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo-central">Clique em um aplicativo para abri-lo em uma nova aba</p>', unsafe_allow_html=True)

# --- Dicionário de Ícones SVG (Baseados na sua tabela) ---
# Estes SVGs são do Lucide Icons (mesmo estilo do Phosphor, traço fino e moderno)
ICONS = {
    "trophy": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/></svg>',
    "check-square": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    "money": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="20" height="12" x="2" y="6" rx="2"/><circle cx="12" cy="12" r="2"/><path d="M6 12h.01M18 12h.01"/></svg>',
    "book-open": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    "calendar": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>',
    "chart-bar": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><line x1="12" x2="12" y1="20" y2="10"/><line x1="18" x2="18" y1="20" y2="4"/><line x1="6" x2="6" y1="20" y2="16"/></svg>',
    "user": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    "qr-code": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="5" height="5" x="3" y="3" rx="1"/><rect width="5" height="5" x="16" y="3" rx="1"/><rect width="5" height="5" x="3" y="16" rx="1"/><path d="M21 16h-3a2 2 0 0 0-2 2v3"/><path d="M21 21v.01"/><path d="M12 7v3a2 2 0 0 1-2 2H7"/><path d="M3 12h.01"/><path d="M12 3h.01"/><path d="M12 16v.01"/><path d="M16 12h1"/><path d="M21 12v.01"/><path d="M12 21v-1"/></svg>',
    "building": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="16" height="20" x="4" y="2" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg>',
    "search": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
    "file-text": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>',
}

# --- Dicionário de Aplicativos (Mapeado com os Ícones da Tabela) ---
apps = {
    "Apura Resultado": {"url": "https://apura-resultado-final.streamlit.app/", "icon": ICONS["trophy"]},
    "Avaliação Especial": {"url": "https://avaliacaoespecialcontagem.streamlit.app/", "icon": ICONS["check-square"]},
    "Bolsa Família": {"url": "https://bolsafamilia2.streamlit.app/", "icon": ICONS["money"]},
    "Contagem de Aulas no Siea": {"url": "https://contagemdeaulasnosiea.streamlit.app/", "icon": ICONS["book-open"]},
    "Criação de Horário Escolar": {"url": "https://sistemadecriacaodehorarioescolar.streamlit.app/", "icon": ICONS["calendar"]},
    "Pontuação no SGE": {"url": "https://conceitosnosge.streamlit.app/", "icon": ICONS["chart-bar"]},
    "Solicitação de Vagas - Participante": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/participante.html", "icon": ICONS["user"]},
    "Solicitação de Vagas - QR Code": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/qrcode.html", "icon": ICONS["qr-code"]},
    "Solicitação de Vagas - Secretaria": {"url": "https://blackspinal.github.io/Solicitacao_de_Vagas/secretaria.html", "icon": ICONS["building"]},
    "Verificar Aulas que Faltam nos Diários": {"url": "https://aulasprevistasxaulasrealizadas.streamlit.app/", "icon": ICONS["search"]},
    "Verificar Notas em Branco nos Diários": {"url": "https://verificarnotasembranconosdiarios.streamlit.app/", "icon": ICONS["file-text"]},
}

# --- Ordenação alfabética em coluna ---
itens_ordenados = sorted(apps.items())
meio = (len(itens_ordenados) + 1) // 2

coluna_1 = itens_ordenados[:meio]
coluna_2 = itens_ordenados[meio:]

col_esq, col_dir = st.columns(2)

with col_esq:
    for nome, info in coluna_1:
        st.markdown(
            f'''
            <a class="app-card" href="{info['url']}" target="_blank" rel="noopener noreferrer">
                <span class="app-name">{nome}</span>
                {info['icon']}
            </a>
            ''',
            unsafe_allow_html=True
        )

with col_dir:
    for nome, info in coluna_2:
        st.markdown(
            f'''
            <a class="app-card" href="{info['url']}" target="_blank" rel="noopener noreferrer">
                <span class="app-name">{nome}</span>
                {info['icon']}
            </a>
            ''',
            unsafe_allow_html=True
        )

# --- Rodapé ---
st.markdown("""
<p class='rodape-minimo'>
Aplicativos desenvolvidos por <strong>André Torres</strong> · Gestão escolar eficiente, organizada e prática<br>
© 2026 · Todos os direitos reservados · andretorres.adm@gmail.com
</p>
""", unsafe_allow_html=True)
