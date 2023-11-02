import speech_recognition as sr
import pyttsx3
import webbrowser
from playsound import playsound

# DATAS THAT CAN BE CHANGED -
ai_name = "Olga"
master_name = "Djimi" # your name [ex: Jimmy = Djimi (in fr_FR language sound)]
# DATAS THAT CAN BE CHANGED -end-

def detect():
 r = sr.Recognizer()
 with sr.Microphone() as source:
    print("Parlez...")
    audio = r.listen(source)

 try:
    if r.recognize_google(audio, language="fr-FR") == ai_name:
      engine = pyttsx3.init()
      engine.say("Oui ? Je vous écoute, " + master_name + "...")
      print(ai_name + ": Oui ?")
      engine.runAndWait()
      main()
    else:
      detect()
 except sr.UnknownValueError:
    detect()
 except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



def main():
 r = sr.Recognizer()
 with sr.Microphone() as source:
    print(ai_name + ": Je vous écoute, " + master_name + "...")
    audio = r.listen(source)

 try:
    if r.recognize_google(audio, language="fr-FR") == "fermeture": #CLOSE_THIS_APP
      print("[Fermeture de l'application demandée]")
      engine = pyttsx3.init()
      engine.say("Aurevoir, à bientôt " + master_name + " !")
      print(ai_name + ": Aurevoir, à bientôt " + master_name + " !")
      engine.runAndWait()

      exit()
    elif r.recognize_google(audio, language="fr-FR") == "éteins-toi": #CLOSE_THIS_APP
      print("[Fermeture de l'application demandée]")
      engine = pyttsx3.init()
      engine.say("Aurevoir, à bientôt " + master_name + " !")
      print(ai_name + ": Aurevoir, à bientôt " + master_name + " !")
      engine.runAndWait()

      exit()


 # DATAS THAT CAN BE CHANGED -     
    elif r.recognize_google(audio, language="fr-FR") == "ouvre YouTube":
      print("[Ouverture de Youtube demandée]")
      engine = pyttsx3.init()
      engine.say("D'accord")
      engine.runAndWait()
      webbrowser.open('http://youtube.com') #COMMAND TO EXECUTE ---
    
      detect()
    elif r.recognize_google(audio, language="fr-FR") == "ouvre Facebook":
      print("[Ouverture de Facebook demandée]")
      engine = pyttsx3.init()
      engine.say("D'accord")
      engine.runAndWait()
      webbrowser.open('http://facebook.com') #COMMAND TO EXECUTE ---
    
      detect()
# DATAS THAT CAN BE CHANGED -end-


    else:
      engine = pyttsx3.init() #NO_RULES | FREE MESSAGE
      engine.say("Vous avez dit: " + r.recognize_google(audio, language="fr-FR"))
      engine.runAndWait()

      detect()
 except sr.UnknownValueError:
    engine = pyttsx3.init()
    engine.say("Désolé, mais c'est incompréhensible... recommencez !")
    print(ai_name + ": Désolé, mais c'est incompréhensible... recommencez !")
    engine.runAndWait()

    detect()
 except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

detect()
