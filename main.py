import streamlit as st

# -------------------------------------------------
# 1️⃣ Configurações da página
# -------------------------------------------------
st.set_page_config(
    page_title="Bot com Streamlit",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# 2️⃣ CSS customizado
# -------------------------------------------------
custom_css = """
html, body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }

.stChatMessage {
    border-radius: 22px;
    padding: 12px 26px;
    text-align: left;
}

.bot-msg {
    background-color: #111112;
    color: white;
    text-align: left;
    margin-top: 6px;
}

.user-msg {
    background-color: #0a84ff;
    color: white;
    text-align: left;
    border-radius: 12px;
    margin-top: 6px;
}
"""
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# -------------------------------------------------
# 3️⃣ Título
# -------------------------------------------------
st.title("🤖 Interface de Bot com Streamlit")

# -------------------------------------------------
# 4️⃣ Histórico de chat
# -------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

for who, msg in st.session_state.history:
    if who == "bot":
        st.markdown(f'<div class="stChatMessage bot-msg"><strong>Júlia:</strong> {msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="stChatMessage user-msg"><strong>Você:</strong> {msg}</div>', unsafe_allow_html=True)

# -------------------------------------------------
# 5️⃣ Função para enviar mensagem ao pressionar Enter
# -------------------------------------------------
def send_message():
    user_input = st.session_state.input_box
    if user_input:
        st.session_state.history.append(("user", user_input))
        # Resposta fixa do bot
        bot_response = (
            "Lorem ipsum dolor sit amet consectetur adipiscing elit. "
            "Quisque faucibus ex sapien vitae pellentesque sem placerat. "
            "In id cursus mi pretium tellus duis convallis. "
            "Tempus leo eu aenean sed diam urna tempor. "
            "Pulvinar vivamus fringilla lacus nec metus bibendum egestas. "
            "Iaculis massa nisl malesuada lacinia integer nunc posuere. "
            "Ut hendrerit semper vel class aptent taciti sociosqu. "
            "Ad litora torquent per conubia nostra inceptos himenaeos."
        )
        st.session_state.history.append(("bot", bot_response))
        st.session_state.input_box = ""  # limpa o campo

# -------------------------------------------------
# 6️⃣ Campo de input (Enter envia mensagem)
# -------------------------------------------------
st.text_input(
    label="",
    placeholder="Digite algo para o bot responder...",
    key="input_box",
    on_change=send_message  # dispara a função ao pressionar Enter
)

# -------------------------------------------------
# 7️⃣ Mensagem inicial
# -------------------------------------------------
if not st.session_state.history:
    st.info("Digite uma mensagem acima e clique em **Enter** para conversar com o bot.")
