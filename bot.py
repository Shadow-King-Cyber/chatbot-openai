"""Bot de chat simple por consola usando la API de OpenAI."""
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# Carga el .env que está junto a este archivo (no depende del directorio actual)
load_dotenv(Path(__file__).resolve().parent / ".env")

# Modelo a usar. Puedes cambiarlo por uno más nuevo o más barato (ver el README).
MODEL = "gpt-4o-mini"

# Define cómo se comporta el bot
SYSTEM_PROMPT = "Eres un asistente útil. Respondes de forma clara y breve, en español."


def main() -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Falta OPENAI_API_KEY. Copia .env.example a .env, pon tu clave y vuelve a intentar.")
        return

    client = OpenAI(api_key=api_key)

    # Historial de la conversación, para que el bot recuerde el contexto de la sesión
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("Bot listo. Escribe tu mensaje (o 'salir' para terminar).\n")

    while True:
        try:
            user_input = input("Tú: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n¡Hasta luego!")
            break

        if not user_input:
            continue
        if user_input.lower() in {"salir", "exit", "quit"}:
            print("¡Hasta luego!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
            )
        except OpenAIError as error:
            print(f"Error al llamar a la API: {error}\n")
            messages.pop()  # descarta el mensaje que no se pudo responder
            continue

        answer = response.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})
        print(f"Bot: {answer}\n")


if __name__ == "__main__":
    main()
