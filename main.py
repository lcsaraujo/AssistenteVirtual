import webbrowser

from testassist import *
def conversando_com_kira():

    if resultfala == "Olá, kira.":
        synthesizer.speak_text_async("Olá Lucas, como você está ? O dia está lindo!")

    elif resultfala == "Abra o Google.":
        webbrowser.open("www.google.com")
        synthesizer.speak_text_async("Pra já ! Abrindo o Google !")
    else:
        synthesizer.speak_text_async("Desculpe, eu não entendi!")

conversando_com_kira()
