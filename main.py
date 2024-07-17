import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
   engine.say(text)
   engine.runAndWait()

def take_command():
   try:
       with  sr.Microphone() as source:
             print('listening.......')
             voice = listener.listen(source)
             command= listener.recognize_google(voice)
             command = command.lower()
             if 'mini' in command:
                 command = command.replace('mini','')
                 print(command)

   except:
        pass
   return command


def run_mini():
     command = take_command()
     print(command)
     if 'play' in command:
         song = command.replace('play','')
         talk('playing' + song)
         pywhatkit.playonyt('song')

     elif 'time' in command:
         time = datetime.datetime.now().strftime('%I:%M %p')
         print(time)
         talk('current time is ' + time)

     elif 'who the heck is' in command:
         person = command.replace('who the heck is','')
         info = wikipedia.summary(person,1)
         print(info)
         talk(info)

     elif 'date' in command:
         talk(' i have a boyfriend guys ')

     elif 'are you single ' in command:
         talk(' iam in a relationship with wifi ')

     elif 'joke' in command:
         talk (pyjokes.get_joke())







run_mini()
#this code written by tanmoy 
#you can add your code....