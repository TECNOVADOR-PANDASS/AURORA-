import speech_recognition as sr

def escuchar_microfono():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Escuchando... (di algo o respira profundo)")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="es-MX")
        print(f"Tú dijiste: {texto}")
        return texto
    except sr.UnknownValueError:
        return "No te entendí, repite por favor."
    except sr.RequestError:
        return "Error al conectar con el servicio de voz."
