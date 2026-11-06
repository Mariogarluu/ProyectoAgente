# 🤖 Proyecto Agentes con LangChain & Ollama

Repositorio dedicado a la arquitectura y desarrollo de **Agentes de Inteligencia Artificial locales** utilizando **LangChain** y **Ollama** para la ejecución de modelos de lenguaje sin dependencia de APIs de pago externas.

---

## 📁 Contenido del Proyecto

- **[`langchain-llm.py`](langchain-llm.py)**: Configuración y consumo básico de un modelo local de Ollama (`qwen3:8b` u otros) mediante `ChatOllama` en LangChain.
- **[`primer_agente.py`](primer_agente.py)**: Implementación de un agente inteligente con uso de herramientas (*Tool Calling*).
  - Incluye la herramienta personalizada `@tool get_current_time()` que proporciona la fecha y hora actual en tiempo de ejecución.
  - El agente evalúa la intención del usuario y decide de forma autónoma cuándo disparar la herramienta para responder con precisión temporal.

---

## 🛠️ Requisitos Previos

1. **Python**: 3.10 o superior.
2. **Ollama instalado y en ejecución**:
   - Descarga Ollama desde [ollama.ai](https://ollama.ai).
   - Asegúrate de tener descargado el modelo configurado:
     ```bash
     ollama run qwen3:8b
     ```

---

## 📦 Instalación

1. Clona el repositorio y activa tu entorno virtual:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requiraments.txt
   ```
   *(Dependencias clave: `langchain`, `langchain-ollama`, `langchain-core`)*

---

## 🚀 Uso y Ejecución

- Probar interacción directa con el LLM:
  ```bash
  python langchain-llm.py
  ```

- Ejecutar el agente con herramientas:
  ```bash
  python primer_agente.py
  ```
