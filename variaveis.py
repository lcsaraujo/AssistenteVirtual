import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import webbrowser
import os
import random
import pyttsx3
import playsound
from gtts import gTTS

token = "4746d9ed1b814a64932f3d6113827a6e"
region = "brazilsouth"

speech_config = speechsdk.SpeechConfig(subscription=token, region=region)

speech_config.speech_recognition_language = "pt-BR"
speech_config.speech_synthesis_voice_name = "pt-BR-FranciscaNeural"

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

audio_config = AudioOutputConfig(use_default_speaker=True)
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

result = speech_recognizer.recognize_once_async().get()
