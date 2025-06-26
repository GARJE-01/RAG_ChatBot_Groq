
import streamlit as st
import os

# === PHASE 2: CONNECT TO LLM ===
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# === PHASE 3: RAG INTEGRATION ===
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA

# ===================
# === PHASE 1: UI SETUP FOR CHATBOT ===
# ===================
# Configure the page
st.set_page_config(
    page_title="RAG ChatBot",
    page_icon="🤖",
    layout="centered"
)

# Add cool glassmorphism styles
st.markdown(
    """
    <style>
    body {
        background: radial-gradient(circle at top, #2c2c54, #1e1e2f);
        color: #ecf0f1;
    }
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        color: #00cec9;
        margin: 0.5rem 0 1rem 0;
        text-shadow: 0 0 10px #00cec9;
    }
    .glass-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 1rem;
        padding: 1rem;
        margin-bottom: 1rem;
        backdrop-filter: blur(8px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    .file-upload {
        padding: 1rem;
    }
    .user-msg, .assistant-msg {
        padding: 0.8rem 1rem;
        border-radius: 1.2rem;
        margin: 0.3rem 0;
        width: fit-content;
        max-width: 70%;
        word-wrap: break-word;
    }
    .user-msg {
        background: #0984e3;
        color: white;
        align-self: flex-end;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    .assistant-msg {
        background: #2d3436;
        color: white;
        align-self: flex-start;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    .message-container {
        display: flex;
        flex-direction: column;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>🤖 RAG ChatBot</h1>", unsafe_allow_html=True)

# ----------------- SESSION STATE FOR CHAT UI -----------------
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None
if 'messages' not in st.session_state:
    st.session_state.messages = []


# ===================
# === PHASE 3: RAG INTEGRATION (UPLOAD DOCUMENT) ===
# ===================
with st.container():
    st.markdown("<div class='glass-box file-upload'>", unsafe_allow_html=True)
    if st.session_state.uploaded_file is None:
        uploaded_file = st.file_uploader(
            "Upload your PDF file 📂",
            type=['pdf'],
            help="Drop your PDF file here to begin!"
        )
        if uploaded_file:
            st.session_state.uploaded_file = uploaded_file
    else:
        st.success(f"✅ Uploaded: {st.session_state.uploaded_file.name}")
    st.markdown("</div>", unsafe_allow_html=True)


# ===================
# === PHASE 3: RAG INTEGRATION (VECTOR EMBEDDING) ===
# ===================
@st.cache_resource
def build_vectorstore(file_path: str):
    loaders = [PyPDFLoader(file_path)]
    index = VectorstoreIndexCreator(
        embedding=HuggingFaceEmbeddings(model='all-MiniLM-L12-v2'),
        text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100
        )
    ).from_loaders(loaders)
    return index.vectorstore


if st.session_state.uploaded_file and st.session_state.vectorstore is None:
    temp_path = os.path.join(".", st.session_state.uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(st.session_state.uploaded_file.getbuffer())
    with st.spinner("Indexing your document... 🧠"):
        st.session_state.vectorstore = build_vectorstore(temp_path)
    st.success("✅ Document indexed successfully!")

# ===================
# === PHASE 1: UI — SHOW CHAT HISTORY ===
# ===================
st.markdown("<div class='message-container'>", unsafe_allow_html=True)
for message in st.session_state.messages:
    cls = "assistant-msg" if message['role'] == 'assistant' else "user-msg"
    st.markdown(
        f"<div class='{cls}'>{message['content']}</div>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)


# ===================
# === PHASE 2: CONNECT TO LLM & PHASE 3: RAG INTEGRATION (QUERYING) ===
# ===================
if st.session_state.vectorstore:
    prompt = st.chat_input("💬 Ask me anything about the file...")
    if prompt:
        # Show user message in chat
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        st.markdown(
            f"<div class='user-msg'>{prompt}</div>",
            unsafe_allow_html=True
        )

        # Prepare system prompt
        groq_sys_prompt = ChatPromptTemplate.from_template(
            """you are very smart at everything, always give the best and most accurate answer.
               Answer this question: {user_prompt}. Start the answer directly no small talk"""
        )
        model = "llama3-8b-8192"
        groq_chat = ChatGroq(
            groq_api_key=os.environ.get('GROQ_API_KEY'),
            model_name=model
        )

        # RAG chain
        try:
            chain = RetrievalQA.from_chain_type(
                llm=groq_chat,
                chain_type='stuff',
                retriever=st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3}),
                return_source_documents=True
            )
            result = chain({"query": prompt})
            response = result["result"]

            # Show assistant message
            st.session_state.messages.append({'role': 'assistant', 'content': response})
            st.markdown(
                f"<div class='assistant-msg'>{response}</div>",
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Error: [{str(e)}]")

# ===================
# === PHASE 1: RESET CHAT / UPLOAD NEW DOCUMENT ===
# ===================
if st.button("🔄 Reset Chat and Upload a new file"):
    st.session_state.uploaded_file = None
    st.session_state.vectorstore = None
    st.session_state.messages = []
    st.rerun()
