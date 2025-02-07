# Requirements
- `Python 3.12`
- `Ollama` & `Llama3.2:1b`

# How to install
- Open Command Prompt
- `python -m venv ragenv`
- `ragenv\Scripts\activate`
- `pip install -r requirements.txt`

# Ollama
- `ollama run llama3.2:1b`
- `ollama help`

# LangChain Retrieval
![alt](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kPSgqK4oCq9beeijmVRK7g.jpeg)

# 5 Levels Of Text Splitting
- Level 1: `Character Splitting` - Simple static character chunks of data
- Level 2: `Recursive Character Text Splitting` - Recursize chunking based on a list of separators
- Level 3: `Document Specific Splitting` - Various chunking methods for different document types (PDF, Python, Markdown)
- Level 4: `Semantic Splitting` - Embedding walk based chunking
- Level 5: `Agentic Splitting` - Experimental method of splitting text with an agent-like system. 

# 🚀 Need to update
- `No semantic chunking` → Your text splitting is purely based on characters, without considering meaning or logical sentence structures.
- `No embedding refinement` → You don’t fine-tune or optimize embeddings to enhance retrieval quality.
- `No reranking` → After retrieving chunks, you don’t re-rank them to prioritize the most relevant information.
- `No context grouping or aggregation` → If related chunks are split apart, the model might miss crucial context.

# Install Python on Windows 11
- Download python from `https://www.python.org/downloads/`
- Add folder contains `python.exe` (Ex: `D:\Tyan\Apps\Python313`) to `system environment variables`
- Run `python -m venv myenv` in cmd for get .env. This will only install packages on this env, not global-env
- `myenv\Scripts\activate` for `pip install`
- Remove cache pip: `pip cache purge`
- Example: `pip install numpy`
- Install LangChain Chroma without update numpy: `pip install langchain-chroma --no-deps`
- Version `Python 3.13` error with `pip install streamlit==3.14.0` & `pip install langchain-chroma` => use `Python 3.12`

# References
- LangChain Retrieval: https://medium.com/@sushmithabhanu24/retrieval-in-langchain-part-2-text-splitters-2d8c9d595cc9