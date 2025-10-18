import streamlit as st
import requests

# --------------------------------------------------------------
# Configurações da página
# --------------------------------------------------------------
st.set_page_config(
    page_title="🤖 Chatbot estilizado",
    page_icon="🤖",
    layout="centered",
)

# --------------------------------------------------------------
# CSS customizado (bolhas, fontes, espaçamento)
# --------------------------------------------------------------
custom_css = """
<style>
body {font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;}

/* Bolha do usuário */
[data-testid="stChatMessageUser"] {
    background-color:#e0f7fa;
    border-radius:12px;
    padding:10px 14px;
    margin-bottom:8px;
}

/* Bolha do assistente */
[data-testid="stChatMessageAssistant"] {
    background-color:#fff3e0;
    border-radius:12px;
    padding:10px 14px;
    margin-bottom:8px;
}

/* Espaço acima da caixa de input */
.stChatInputContainer {margin-top:20px;}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --------------------------------------------------------------
# Estado da sessão – lista de mensagens
# --------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------------------
# Layout em colunas
# --------------------------------------------------------------
col_chat, col_sidebar = st.columns([3, 1])

# ---------- Sidebar ----------
with col_sidebar:
    st.image("https://proton.me/logo.png", width=120)
    st.markdown("**Dicas rápidas**")
    st.write("- Digite `oi` para iniciar a conversa")
    st.write("- Use emojis para deixar o chat mais leve")
    st.write("- Atualize a página para limpar o histórico")

# ---------- Área principal ----------
with col_chat:
    st.title("🤖 Chatbot com Streamlit")

    # Entrada do usuário
    user_input = st.chat_input("Digite sua mensagem…")

    if user_input and user_input.strip():
        # Guarda a mensagem do usuário
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        # Resposta simples do bot
        lower = user_input.lower()
        if "oi" in lower:
            bot_reply = "Olá! Como você está? 😃"
        elif "tchau" in lower:
            bot_reply = "Até logo! 👋"
        else:
            bot_reply = "Não entendi 🤔"

        # Guarda a resposta do bot
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

    # Exibição das mensagens
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").write(f"👤 {msg['content']}")
        else:
            st.chat_message("assistant").write(f"🤖 {msg['content']}")