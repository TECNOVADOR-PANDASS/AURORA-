from utils.analisis_emocional import detectar_emocion
from utils.voz import hablar
from utils.voz_a_texto import escuchar_microfono

def iniciar_chat():
    print("👋 Hola, soy tu IA compañera. Cuéntame cómo te sientes.")
    while True:
        mensaje = escuchar_microfono()
        if mensaje.lower() in ["salir", "adiós", "exit"]:
            print("IA: Gracias por compartir conmigo. Aquí estaré cuando me necesites 💙")
            hablar("Gracias por compartir conmigo. Aquí estaré cuando me necesites.")
            break
        emocion = detectar_emocion(mensaje)
        respuesta = f"Entiendo que sientes {emocion}. Estoy aquí contigo."
        print("IA:", respuesta)
        hablar(respuesta)
