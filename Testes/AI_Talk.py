from gtts import gTTS
from playsound import playsound

portugues_text = "Como você está?"
portugues_language = "pt-br"

# Cria o objeto gTTS e salva o arquivo de áudio
portugues_gtts_object = gTTS(
    text=portugues_text, 
    lang=portugues_language, 
    slow=False
    )

arquivo_audio = "Portugues.mp3"
portugues_gtts_object.save(arquivo_audio)

# Reproduz o áudio automaticamente
playsound(arquivo_audio)
