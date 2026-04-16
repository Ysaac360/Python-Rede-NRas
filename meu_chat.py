import streamlit as st
from google import genai
from google.genai import types

# ==========================================
# 1. CONFIGURAÇÃO DA API
# ==========================================
# ATENÇÃO: Verifique se sua chave está correta (ela geralmente começa com "AIza")
CHAVE_API = "" 

# O SEGREDO AQUI: st.cache_resource impede que a conexão seja fechada a cada recarregamento
@st.cache_resource
def iniciar_cliente():
    return genai.Client(api_key=CHAVE_API)

cliente = iniciar_cliente()

instrucoes_sistema = """
Você é um assistente virtual altamente inteligente, educado e adaptável.
Você consegue ter conversas casuais de forma humana e empática, mas também 
pode mergulhar profundamente em temas técnicos, como programação (Python, C#, C++), 
banco de dados (SQL), sistemas operacionais e automação industrial (CLPs, sensores, SCADA).
Sempre responda no idioma em que o usuário falar com você.
"""

# ==========================================
# 2. CONFIGURAÇÃO DA INTERFACE (TELA)
# ==========================================
st.set_page_config(page_title="Meu Assistente Pessoal", page_icon="🤖")
st.title("🤖 ChatBot Inteligente")
st.caption("Um assistente com memória, pronto para diálogos complexos.")

# ==========================================
# 3. SISTEMA DE MEMÓRIA
# ==========================================
if "chat" not in st.session_state:
    st.session_state.chat = cliente.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            temperature=0.7,
            system_instruction=instrucoes_sistema,
        )
    )

for mensagem in st.session_state.chat.get_history():
    papel = "assistant" if mensagem.role == "model" else "user"
    with st.chat_message(papel):
        st.markdown(mensagem.parts[0].text)

# ==========================================
# 4. CAIXA DE TEXTO E RESPOSTA
# ==========================================
prompt = st.chat_input("Digite sua mensagem aqui...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        mensagem_carregando = st.empty()
        mensagem_carregando.markdown("⏳ *Pensando...*")
        
        try:
            resposta = st.session_state.chat.send_message(prompt)
            mensagem_carregando.markdown(resposta.text)
        except Exception as e:
            mensagem_carregando.markdown(f"**Erro na conexão:** {e}")
