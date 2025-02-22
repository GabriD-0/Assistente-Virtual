# Assistente de Voz com Integração ao Spotify

Este projeto é um assistente de voz que permite controlar a reprodução de músicas no Spotify por meio de comandos de voz. Utiliza diversas bibliotecas, como `spotipy` para integração com a API do Spotify, `speech_recognition` para reconhecimento de voz, `gTTS` para síntese de fala e `playsound` para reprodução de áudio.

## Funcionalidades

- **Reprodução de Músicas:** Busque e reproduza uma música específica no Spotify usando comandos como "tocar música" ou "spotify".
- **Controle de Playback:** Avance para a próxima música, volte para a música anterior ou pause a reprodução.
- **Interação por Voz:** O assistente utiliza o microfone para captar comandos de voz e responde com áudio.

## Pré-requisitos

- **Conta Spotify Premium:** Necessária para utilizar a API de controle de reprodução do Spotify.
- **Python 3.6+**
- **Dispositivo Ativo:** O aplicativo Spotify deve estar aberto e logado na mesma conta usada na API.
- **Microfone:** Para captar os comandos de voz.

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
CLIENT_ID=seu_client_id_do_spotify
CLIENT_SECRET=seu_client_secret_do_spotify
URI=http://localhost:8888/callback
```

*Obs.: Certifique-se de registrar o `redirect_uri`  no [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).*

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No macOS/Linux:
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

   *Caso não possua um arquivo `requirements.txt`, instale as seguintes bibliotecas:*

   ```bash
   pip install python-dotenv spotipy pyaudio SpeechRecognition gTTS playsound
   ```

   *Obs.: No Windows, a instalação do `pyaudio` pode requerer binários pré-compilados se ocorrerem erros.*

## Uso

1. **Configure as variáveis de ambiente:**  
   Crie e edite o arquivo `.env` conforme as instruções acima.

2. **Execute o script:**

   ```bash
   python seu_script.py
   ```

3. **Interaja com o Assistente:**  
   - O assistente começará com uma saudação: "Olá, como você está?"  
   - Para reproduzir uma música, diga: "tocar música" ou "spotify". O assistente perguntará qual música você deseja ouvir.  
   - Use comandos como "próxima" ou "volta" para avançar ou retroceder nas faixas.  
   - Para pausar a música, diga "parar música" ou "pare".  
   - Para encerrar, diga "tchau" ou "sair".


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
