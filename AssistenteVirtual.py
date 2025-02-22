import os
import dotenv
import spotipy
import pyaudio
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from spotipy.oauth2 import SpotifyOAuth

dotenv.load_dotenv()

# Configurar o Spotipy com as credenciais e escopos
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET'),
    redirect_uri=os.environ.get('URI'),
    scope="user-read-playback-state user-modify-playback-state"
))

def speak(text):
    tts = gTTS(text=text, lang='pt')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound(filename)


def spotify_play(query):
    busca = sp.search(q=query, limit=1, type="track")
    if busca["tracks"]["items"]:
        track = busca["tracks"]["items"][0]
        track_uri = track["uri"]
        track_name = track["name"]
        speak(f"Tocando {track_name}")
        print("Tocando a música:", track_name)
        try:
            sp.start_playback(uris=[track_uri])
        except Exception as e:
            print("Erro ao iniciar a reprodução:", e)
            speak("Desculpe, não foi possível iniciar a reprodução no Spotify.")
    else:
        print("Música não encontrada.")
        speak("Desculpe, não encontrei essa música no Spotify.")

def spotify_next():
    try:
        sp.next_track()
        speak("Avançando para a próxima música")
        print("Próxima música")
    except Exception as e:
        print("Erro ao pular para a próxima música:", e)
        speak("Desculpe, não foi possível pular para a próxima música.")

def spotify_previous():
    try:
        sp.previous_track()
        speak("Voltando para a música anterior")
        print("Música anterior")
    except Exception as e:
        print("Erro ao voltar para a música anterior:", e)
        speak("Desculpe, não foi possível voltar para a música anterior.")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("Ouvindo...")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="pt-BR")
            print("Você disse:", said)
        except sr.UnknownValueError:
            speak("Desculpe, não entendi.")
        except sr.RequestError:
            speak("Desculpe, o serviço não está disponível.")
    return said.lower()



def respond(text):
    print("Processando comando:", text)
    
    if 'tocar música' in text or 'spotify' in text:
        speak("Qual música você quer ouvir?")
        musica = get_audio()  # Captura o nome da música desejada
        if musica:
            spotify_play(musica)
        else:
            speak("Não consegui identificar o nome da música.")
            
    elif 'próxima' in text or 'próximo' in text:
        spotify_next()
        
    elif 'volta' in text:
        spotify_previous()
        
    elif 'parar música' in text or 'pare' in text:
        try:
            sp.pause_playback()
            speak("Música pausada.")
        except Exception as e:
            print("Erro ao pausar a reprodução:", e)
            speak("Desculpe, não foi possível pausar a reprodução.")
            
    elif 'tchau' in text or 'sair' in text:
        speak("Tchau amorzinho!")
        exit()
        
    else:
        speak("Comando não reconhecido. Por favor, tente novamente.")



# Saudação inicial
portugues_text = "Olá, como você está?"
portugues_gtts_object = gTTS(text=portugues_text, lang="pt", slow=False)
arquivo_audio = "Portugues.mp3"
portugues_gtts_object.save(arquivo_audio)
playsound(arquivo_audio)



# Loop principal do assistente
while True:
    print("Aguardando comando...")
    comando = get_audio()
    if comando:
        respond(comando)
