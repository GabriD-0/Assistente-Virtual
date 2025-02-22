import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Por favor, fale algo (aguardando 10 segundos)...")
    try:
        audio = r.listen(source, timeout=10, phrase_time_limit=10)
        print("Áudio capturado, processando...")
        texto = r.recognize_google(audio, language="pt-BR")
        print("Você disse:", texto)
    except sr.WaitTimeoutError:
        print("Tempo de espera excedido. Nenhuma fala detectada.")
    except sr.UnknownValueError:
        print("Não foi possível entender o que você disse!")
    except sr.RequestError as e:
        print("Erro ao se conectar com o serviço de reconhecimento; {0}".format(e))
