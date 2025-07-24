<h1>RAG ChatBot (Groq + LangChain)</h1>
<hr>
<p><strong>RAG ChatBot (Groq + LangChain)</strong></p>

<p><strong>Outline / Brief Description:</strong><br>
This project is a <strong>Retrieval-Augmented Generation (RAG)-based chatbot</strong> that enables interactive Q&A on uploaded PDF documents. It uses <strong>Streamlit</strong> for a stylish UI and <strong>LangChain</strong> for document chunking, vectorization with <strong>HuggingFace embeddings</strong>, and leveraging <strong>Groq’s ultra-fast LLaMA model</strong> for accurate responses. It’s deployed on <a href="https://streamlit.io/" target="_blank">Streamlit Cloud</a> and is designed to make document analysis faster and more accessible.</p>

<h2>📄 General Information</h2>
<hr>
<ul>
  <li>This project is a RAG-powered chatbot allowing queries on uploaded PDFs.</li>
  <li>It solves the problem of manually searching long documents, boosting efficiency.</li>
  <li>The goal is to streamline Q&A for students, professionals, and researchers.</li>
</ul>

<h2>🛠️ Technologies Used</h2>
<hr>
<h4>Programming Language:</h4>
<ul>
  <li>Python 3.11</li>
</ul>
<h4>Frameworks & Libraries:</h4>
<ul>
  <li>Streamlit — for building the web interface</li>
  <li>LangChain — for RAG pipeline and vectorstore management</li>
  <li>HuggingFace Embeddings — for embedding the document contents</li>
  <li>Groq API (LLaMA 3) — for super-fast LLM inference</li>
  <li>PyPDFLoader — for reading and splitting PDFs</li>
  <li>RecursiveCharacterTextSplitter — for efficient chunking of text content</li>
</ul>
<h4>Deployment & Version Control:</h4>
<ul>
  <li>Git & GitHub — version control and source code hosting</li>
  <li>Streamlit Cloud — one-click deployment & hosting</li>
</ul>
<h4>Configuration:</h4>
<ul>
  <li>.env files — for safe environment variable handling</li>
</ul>

<h2>✨ Features</h2>
<hr>
<ul>
  <li>📂 PDF Upload Support — Easily upload one or multiple PDFs.</li>
  <li>🧠 Context-Aware Answers — Answers derived directly from uploaded content.</li>
  <li>📝 Conversation History — Keep track of queries and responses.</li>
  <li>⚡ Groq LLaMA-powered Inference — Fast responses powered by Groq API.</li>
  <li>🎨 Stylish UI — Modern glassmorphism interface for a polished look.</li>
  <li>🔄 Reset Option — Quickly reset chat and upload new files.</li>
  <li>🆕 Source References — See excerpts of source text alongside answers.</li>
</ul>

<h2>⚙️ Setup</h2>
<hr>
<h4>Requirements:</h4>
<p>Check <code>requirements.txt</code> for dependencies:</p>
<pre><code>streamlit
langchain
langchain-groq
langchain-huggingface
pypdf
sentence-transformers
</code></pre>

<h4>Steps to Run Locally:</h4>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/YOUR_USERNAME/RAG_ChatBot_Groq.git
cd RAG_ChatBot_Groq</code></pre>
  </li>
  <li>(Optional) Create & activate a virtual environment:
    <pre><code>python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/MacOS</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Create a <code>.env</code> file for your Groq API key:
    <pre><code>GROQ_API_KEY=your-groq-api-key-here</code></pre>
  </li>
  <li>Run the app:
    <pre><code>streamlit run Chatbot.py</code></pre>
  </li>
</ol>

<h2>💡 Usage</h2>
<hr>
<p>Once up and running, you can:</p>
<ul>
  <li>📂 Upload a PDF file — via the upload section.</li>
  <li>🤖 Ask questions — and receive instant, accurate answers.</li>
  <li>🔄 Restart session — to clear data and upload new files.</li>
</ul>

<h2>📊 Project Status</h2>
<hr>
<p>✅ Completed and deployed on <a href="https://streamlit.io/cloud" target="_blank">Streamlit Cloud</a> — try the live app <a href="https://garje-rag-chatbot.streamlit.app/" target="_blank">here</a> 🎯</p>

<h2>🚀 Improvements</h2>
<hr>
<ol>
  <li>Multi-File Support — Query across multiple PDFs.</li>
  <li>Conversation Persistence — Save sessions for future use.</li>
  <li>Advanced Features — Voice-based querying and highlighted source excerpts.</li>
</ol>

<h2>🌟 Future Features</h2>
<hr>
<ol>
  <li>Multi-File Chat Support</li>
  <li>Voice Input & Output</li>
  <li>Contextual Highlighting of Source Text</li>
</ol>

<h2>🙏 Acknowledgements</h2>
<hr>
<ol>
  <li>This project was inspired by the need for smarter document Q&A tools.</li>
  <li>Based on tutorials and official docs from LangChain, Groq, HuggingFace, and Streamlit.</li>
  <li>Special thanks to the open-source community that made these tools accessible.</li>
</ol>

<h2>📬 Contact</h2>
<hr>
<p>
  <a href="https://www.linkedin.com/in/mayurgarjeofficial" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" style="width: 10%;" alt="LinkedIn">
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://github.com/GARJE-01" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" style="width: 10%;" alt="GitHub">
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.facebook.com/gaming.mayur.5" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/facebook/facebook-original.svg" style="width: 10%;" alt="Facebook">
  </a>
</p>
