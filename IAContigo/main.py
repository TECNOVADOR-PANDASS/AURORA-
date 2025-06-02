from utils.analisis_emocional import detectar_emocion
from utils.voz import hablar
from utils.voz_a_texto import escuchar_microfono

def iniciar_chat():
    hablar("Hola, soy Aurora, tu compita emocional digital. ¿Cómo te sientes hoy, amorcita?")
    print("👂 Esperando tu voz...")

    while True:
        mensaje = escuchar_microfono()
        if mensaje.lower() in ["salir", "adiós", "exit"]:
            despedida = "Recuerda: si nadie te escucha, aquí estoy yo, Fatipandi style."
            print("IA:", despedida)
            hablar(despedida)
            break
        emocion = detectar_emocion(mensaje)
        respuesta = f"Entiendo que sientes {emocion}. Estoy aquí contigo."
        print("IA:", respuesta)
        hablar(respuesta)

if __name__ == "__main__":
    iniciar_chat()
