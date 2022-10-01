from variaveis import *


class Virtual_assist():
    def __int__(self, assist_name, person):
        self.person = person
        self.assist_name = assist_name

        self.engine = synthesizer.speak_text_async()
        self.r = speech_recognizer.recognize_once_async().get()

        self.voice_data = ''

    def engine_speak(self, text):
        # fala da assistente virtual

        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def record_audio(self, ask=""):
        with self.r as source:
            if ask:
                print("Recording")
                self.engine_speak(ask)

            audio = self.r.listen(source, 5, 5)
            print('Olhando a base de dados')

            try:
                self.voice_data = self.r(audio)
            except speech_recognizer.UnknownValueError:
                self.engine_speak(f"Desculpe {self.person,} não entendi, pode repetir ?")
            except speech_recognizer.RequestError:
                self.engine_speak("Desculpe senhor, o servidor caiu")

            print(">>", self.voice_data.lower())
            self.voice_data = self.voice_data.lower()

            return self.voice_data.lower()

    def engine_speak(self, audio_string):
        audio_string = str(audio_string)
        tts = speech_recognizer(text=audio_string)
        r = random.randint(1, 2000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assist_name + ':', audio_string)
        os.remove(audio_file)

    def there_exists(self, terms):
        # Função para identificar se o termo existe

        for term in terms:
            if term in self.voice_data:
                return True

    def respond(self, voice_data):
        if self.there_exists(['hey', 'hi', 'olá', 'holla', 'oi']):
            greetings = [f'Olá {self.person}, o que vamos fazer hoje?',
                         f'Olá {self.person}, como posso te ajudar?'
                         f'Olá {self.person}, o que você precisa?']
            greet = greetings[random.randint(0, len(greetings) - 1)]
            self.engine_speak(greet)

        if self.there_exists(['search for']) and 'youtube' not in voice_data:
            search_term = voice_data.split("for")[-1]
            url = "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak('aqui está o que eu encontrei sobre' + search_term + 'no google')

        if self.there_exists(['search youtube for']):
            search_term = voice_data.split("for")[-1]
            url = "http://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak('aqui está o que eu encontrei sobre' + search_term + 'no google')

        assistent = Virtual_assist("Kira", "Lucas")

        while True:

            voice_data = assistent.record_audio('Ouvindo...')
            assistent.respond(voice_data)

            if assistent.there_exists(['tchau', 'bye', 'goodbye', 'até mais tarde']):
                assistent.engine_speak("Tenha um otimo dia, tchau !")
