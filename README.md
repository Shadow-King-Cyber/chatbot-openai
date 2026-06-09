# chatbot-openai

Bot de chat simple por consola que se conecta a la API de OpenAI y responde a lo que escribas. Mantiene el contexto durante la sesión, así que recuerda lo que se habló antes.

## Requisitos

- Python 3.10 o superior
- Una cuenta de OpenAI con una API key ([platform.openai.com](https://platform.openai.com/api-keys))

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Shadow-King-Cyber/chatbot-openai.git
cd chatbot-openai

# 2. Crear y activar un entorno virtual
python -m venv .venv

# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

## Configuración

Copia la plantilla de variables de entorno y pon tu clave de OpenAI:

```bash
# Windows:
copy .env.example .env
# Linux / macOS:
cp .env.example .env
```

Luego abre el archivo `.env` y pega tu clave:

```
OPENAI_API_KEY=sk-...tu-clave...
```

## Uso

```bash
python bot.py
```

Escribe tu mensaje y el bot responde. Para terminar, escribe `salir` (o presiona `Ctrl+C`).

```
Bot listo. Escribe tu mensaje (o 'salir' para terminar).

Tú: hola, ¿qué puedes hacer?
Bot: Puedo responder preguntas, explicar temas y ayudarte con texto. ¿Qué necesitas?

Tú: salir
¡Hasta luego!
```

## Personalización

Todo se configura en las primeras líneas de `bot.py`:

- **Modelo** — cambia la línea `MODEL = "gpt-4o-mini"`. El modelo por defecto es barato y suficiente para respuestas simples. Si quieres uno más nuevo o más económico, consulta los nombres exactos en [platform.openai.com/docs/models](https://platform.openai.com/docs/models) (por ejemplo, los modelos *nano* de OpenAI son los más baratos).
- **Personalidad** — edita `SYSTEM_PROMPT` para cambiar el tono, el idioma o el estilo de las respuestas.

## Estructura

```
chatbot-openai/
├── bot.py             # El bot
├── requirements.txt   # Dependencias
├── .env.example       # Plantilla de variables de entorno
├── .gitignore
└── README.md
```

## Licencia

MIT — puedes usar y modificar este código libremente.
