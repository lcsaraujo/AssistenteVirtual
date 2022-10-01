"""
import azure.cognitiveservices.speech as speechsdk


def recognize_from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="4746d9ed1b814a64932f3d6113827a6e", region="brazilsouth")
    speech_config.speech_recognition_language = "pt-BR"
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)


recognize_from_mic()
"""

import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig


def synthesize_to_speaker():
    speech_config = speechsdk.SpeechConfig(subscription="4746d9ed1b814a64932f3d6113827a6e", region="brazilsouth")
    speech_config.speech_synthesis_voice_name = "pt-BR-FranciscaNeural"

    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async("Olá, estou fazendo um teste")


synthesize_to_speaker()
