# Requirements
- `Python 3.12`
- `Ollama` & `Llama3.2:1b`

# Ollama
- `ollama run llama3.2:1b`
- `ollama help`

# Install Python on Windows 11
- Download python from `https://www.python.org/downloads/`
- Add folder contains `python.exe` (Ex: `D:\Tyan\Apps\Python313`) to `system environment variables`
- Run `python -m venv myenv` in cmd for get .env. This will only install packages on this env, not global-env
- `myenv\Scripts\activate` for `pip install`
- Remove cache pip: `pip cache purge`
- Example: `pip install numpy`
- Install LangChain Chroma without update numpy: `pip install langchain-chroma --no-deps`
- Version `Python 3.13` error with `pip install streamlit==3.14.0` & `pip install langchain-chroma` => use `Python 3.12`