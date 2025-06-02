from textblob import TextBlob

def detectar_emocion(texto):
    texto = texto.lower()
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity

    emocion_extra = {
        "emocionad": "felicidad",
        "triste": "tristeza",
        "enojad": "enojo",
        "estres": "miedo",
        "ansios": "miedo",
        "feliz": "felicidad",
        "sola": "tristeza",
        "llorar": "tristeza",
        "abraz": "amor"
    }

    for palabra, emocion in emocion_extra.items():
        if palabra in texto:
            return emocion

    if polaridad > 0.3:
        return "felicidad"
    elif polaridad < -0.3:
        return "tristeza"
    else:
        return "neutral"
