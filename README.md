<h1>Vocal_Command</h1>
<br>
<p>Vocal_Command est un script en Python qui vous permet de commander votre ordinateur avec votre voix.</p>
<br>
<p>Avant toutes choses il faut que vous installiez des plugins pour Python:</p>

- pip install SpeechRecognition

- pip install pyttsx3

- pip install playsound

<br>
<p>Executez l'exemple <b>main.py</b> <i>(vous pouvez le modifier pour choisir votre language, en l'occurance, ici, ce sera du français)</i>.</p>
<br>
<p>Dites <b>"Olga"</b> et attendez la réponse, puis dites <b>"ouvre Youtube"</b>.</p>
<br>
<p>Modifiez le script comme bon vous semble et en fonction de ce que vous avez besoin de faire.</p>
<br>
<p>Par exemple, ajoutez ceci dans le script sous 'def main(): try':</p>

<p>
  
      elif r.recognize_google(audio, language="fr-FR") == "ouvre Facebook": #TEXT TO RECOGNIZE ---
        print("[Ouverture de Facebook demandée]") #DEV CONSOLE TEXT ---
        engine = pyttsx3.init() #DON'T CHANGE IT!! ---
        engine.say("D'accord") #AI SPEAKING TEXT ---
        engine.runAndWait() #DON'T CHANGE IT!! ---
        webbrowser.open('http://facebook.com') #COMMAND TO EXECUTE ---
    
        detect()
</p>
