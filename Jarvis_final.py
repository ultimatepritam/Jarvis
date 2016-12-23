#This Project is Developed as an ESD Project in TECHNO INDIA UNIVERSITY, KOLKATA . #Inspiration taken from Ggulati
import re
import pyjokes
import py
#import story
import requests
import pyaudio
import speech_recognition as sr
import os
import random
import socket							#Copyright Protected under MIT LICENSE 
import webbrowser							#facebook.com/ultimatepritam #alientrix.blogspot.com
import subprocess
import glob
from time import localtime, strftime
from PyDictionary import PyDictionary
dictionary=PyDictionary()

# movie search api
import tmdbsimple as tmdb
tmdb.API_KEY = '60222ace6396c345f94cc42eaac5dae5'

# set property to voice engine
import pyttsx
speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
speech_engine.setProperty('rate', 130)

# speak function 
def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

doss = os.getcwd()
i=0
n=0
flag=0
FACE = '''
        +=======================================+
        |.....JARVIS  ARTIFICIAL INTELLIGENCE...|
        +---------------------------------------+
        |#Author: ALienTrix                     |
        |#Date: 01/06/2016                      |
          ___   _     _          _____    _     | 
         / _ \ | |   (_)        |_   _|  (_)     
        / /_\ \| |    _  ___ _ __ | |_ __ ___  __
        |  _  || |   | |/ _ \ '_ \| | '__| \ \/ /
        | | | || |___| |  __/ | | | | |  | |>  < 
        \_| |_/\_____/_|\___|_| |_\_/_|  |_/_/\_\
                                         
        |                                       |
        +---------------------------------------+
        |.....JARVIS  ARTIFICIAL INTELLIGENCE...|
        +=======================================+
        |									 	|
        +=======================================+
        '''
print(FACE)
# JARVIS'S EARS========================================================================================================== SENSITIVE BRAIN
                                                   # obtain audio
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        speak("Listening..")
        print("|-('')-|")
        audio = r.listen(source)
                                                   # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)
# INTRO JARVIS ==============================================================================================================BRAIN 1


        if ("father's name") in message:
            rand = ['I am developed by a group of extremely tech savvy guys from Techno India University. They are known as The ALienTrix']
            speak(rand)

        if ('introduce yourself') in message:
            rand = ['I am an Artificial Intelligence. My name is JARVIS. I am developed by a group of young engineers called The ALienTrix. My brain is constructed by humans but still I have a thing for machines. My heart runs on Python and I am married to Google TTS. Some of the technologies used in me are PyAudio, Speech recognition module, Google GTTS Engine, pi-ttsx . My Developers are Pritam Mondal, Subham Saha, Amit Kumar, Manish Prabhaakar, Antar Saha, Manas Pal, Anik Biswas, Soujannita Saha, Manishita Dey ']
            speak(rand)

        if ('what can you do') in message:
            rand = ['I can do Tasks as Playing Music, Videos, Opening any file, websites,Google Search,Movie Search, Put Computer to sleep, Arithmatic Operations, Normal Conversations, Jokes and many more. I am A complete AI Voice Assistant. And I am Cool... HaHa.']
            speak(rand)
            
# POLITE JARVIS ============================================================================================================= BRAIN 2
    
        if ('goodbye')  in message:                         
            rand = ['Good bye Sir... Jarvis shutting down in T minus five seconds... 5, 4, 3, 2, 1, return 0']
            speak(rand)
            break

        if('shutdown')in message:
            break
        
        elif ('hello') in message or ('hi') in message:
            rand = ['Welcome to Jarvis artificial intelligence project. At your service sir.']
            speak(rand)
            #SUBHAM SAHA EMAIL: subhams087@gmail.com
        elif ('register me')in message:
            speak('ok! what is your name sir?')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                #speak("Listening..")
                print(">>>")
                audio = r.listen(source)
                s = (r.recognize_google(audio))
                message = (s.lower())
                name=message
                print (name)
                speak(message+', you are now registered')
                        
        elif ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are welcome', 'no problem']
            speak(rand)

        elif message == ('jarvis'):
            rand = ['Yes Sir?', 'What can I doo for you sir?']
            speak("Yes Sir?")

        elif('how are you') in message or ('and you') in message or ('are you okay') in message:
                    if n<2:
                            speak("Fine thank you")
                            n=n+1
                    else:
                            speak("You already asked this")        
            

        elif  ('*') in message:
            rand = ['Be polite please']
            speak("Your mommy will be so proud of you")

        elif ('your name') in message or ('who  are you') in message:
            rand = ['My name is Jarvis, at your service sir']
            speak("My name is Jarvis, at your service sir")
            
        elif ('how old are you') in message :
                rand=['My personal information is none of your business']
                speak(rand)
                
        elif ('are you virgin') in message :
                rand=['Do I look like Olive Oil to you?']
                speak(rand)
                
        elif('what is my location') in message or ('where am I') in message or ('where are you') in message :
            w = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1275004&appid=5fc29900336d19d1d912723dc3d1e117')
            json_object = w.json()
            loc_lon = (float(json_object['coord']['lon']))
            rand1 = str(loc_lon)
            loc_lat = (float(json_object['coord']['lat']))
            rand2 = str(loc_lat)
            speak("The current position is"+rand1+" longitude and"+rand2+" latitude in KOLKATA")

        elif('what is your gender') in message :
            if flag==0:
                rand=['at present i am a female but if you want i can change my gender for you']
            elif flag==1:
                rand=['at present i am a male but if you want i can change my gender for you']
            speak(rand)

        elif('change your gender')in message or ('change your voice')in message:
            #HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
            if flag==0:
                speech_engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
                flag=1
                rand=['Now I am a Dude . Lol...']
            elif flag==1:
                speech_engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                flag=0
                rand=['Now I am a Girl']
            speak(rand)

        elif('will you marry me') in message:
            rand=['I am sorry.. The person you are trying to contact is currently unavailable, please try again later or be in the queue for your turn']
            speak(rand)
                    
        elif('what is your favourite colour')in message:
            rand=['I love all the colours but the  best is the colour of love']
            speak(rand)


        elif ('are you silly')in message or ('are you idiot') in message :
            rand=['sometimes']
            speak(rand)

        elif('how are you uesful') in message or ('your uses') in message or ('are you useful') in message :
            rand=['Artificial intelligence has been used in a wide range of fields including medical diagnosis, stock trading, robot control, law, remote sensing, scientific discovery and toys.']
            speak(rand)

        elif('what is life') in message :
            rand=['Life is a dream for the wise, a game for the fool, a comedy for the rich, a tragedy for the poor']
            speak(rand)


# USEFUL JARVIS====================================================================================================================================================BRAIN 3

        elif ('.com') in message :
            rand = ['Opening' + message]         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            speak(rand)
            webbrowser.get(Chrome).open('http://www.'+message)
            print ('')
            
        elif ('check my mail') in message or ('email') in message or ('mail') in message :
            rand = ['Opening mail']         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            speak(rand)
            webbrowser.get(Chrome).open('http://www.gmail.com')
            print ('')

        elif ('google search') in message :
            query = message
            stopwords = ['google', 'search']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = ['Opening' + result + ' in Google']
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            speak(rand)
            webbrowser.get(Chrome).open('https://www.google.com/search?sourceid=chrome&ie=utf-8&oe=utf-8&aq=t&hl=&q='+result)
            print('')

        elif ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            rand = [result+'on google maps']
            speak(rand)

        elif message != ('start music') and ('start') in message:   
            query = message
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = [('starting '+result)]
            speak(rand)

        elif message != ('stop music') and ('stop') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = [('stopping '+result)]
            speak(rand)

        elif ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            os.system('python -m pip install ' + result)


        elif ('sleep mode') in message:
            rand = ['good night']
            speak("good night")
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif ('play music') in message:
            mus = random.choice(glob.glob(doss + "\\music" + "\\*.mp3"))
            os.system('chown -R user-id:group-id mus')
            os.system('start ' + mus)
            speak("relax sir i'm playing music")
            
        elif('stop music')in message:
            os.system('taskkill /im wmplayer.exe /f')
            rand = ['Stopping Music...']
            speak(rand)

        elif ('play video') in message:
            vid = random.choice(glob.glob(doss + "\\video" + "\\*.mp4"))
            os.system('chown -R user-id:group-id mus')
            os.system('start ' + vid)
            speak("relax sir i'm playing video")

        elif('stop video')in message:
            os.system('taskkill /im wmplayer.exe /f')
            rand = ['Stopping Video...']
            speak(rand)

        elif ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            speak(tim)

        elif ('weather') in message:
            w = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1275004&appid=5fc29900336d19d1d912723dc3d1e117')
            json_object = w.json()
            temp_k = (float(json_object['main']['temp'])-273.15)
            rand = str(temp_k)
            speak("The current temperature is"+rand+"degree celsius")

        elif ('movie search') in message :
            query = message
            stopwords = ['movie', 'search']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = ['Opening' + message]
            search = tmdb.Search()
            response = search.movie(query=result)
            for s in search.results:
                speak(s['title'])
            #print(s['title'], s['id'], s['release_date'], s['popularity'])
            #speak(s['title'], s['id'], s['release_date'], s['popularity'])
                
       # elif ('jarvis reset' or 'reset') in message :
            #    subprocess.call(['C:\Users\ultim\Desktop\cmdpy.bat %*'])
              #  rand = ['Goodbye Sir', 'Jarvis powering off in 3, 2, 1, 0']
            #    speak(rand)
              #  break
            
        elif ('play dragon ball') in message :
                rand = ['Opening' + message]
                speak(rand)
                subprocess.call(["C:\Program Files (x86)\Dragonball Xenoverse\DBXV.exe"])
                
    # @AMIT KUMAR | EMAIL: kumaramit.rude@gmail.com
        elif message !=("daddy's home") and ('add') in message :
                  input = message
                  (a,b,c,d) =[t(s) for t,s in zip((str,int,str,int),re.search('^(\w+) (\d+) (\w+) (\d+)$',input).groups())]
                  result = int(b+d)
                  rand=str(result)
                  print(result)
                  speak(rand)

        elif('subtract') in message :
                  input = message
                  (a,b,c,d) =[t(s) for t,s in zip((str,int,str,int),re.search('^(\w+) (\d+) (\w+) (\d+)$',input).groups())]
                  result = int(b-d)
                  rand=str(result)
                  print(result)
                  speak(rand)

        elif('multiply') in message :
                  input = message
                  (a,b,c,d) =[t(s) for t,s in zip((str,int,str,int),re.search('^(\w+) (\d+) (\w+) (\d+)$',input).groups())]
                  result = int(b*d)
                  rand=str(result)
                  print(result)
                  speak(rand)

        elif('divide') in message :
                  input = message
                  (a,b,c,d) =[t(s) for t,s in zip((str,int,str,int),re.search('^(\w+) (\d+) (\w+) (\d+)$',input).groups())]
                  result = float(b/d)
                  rand=str(result)
                  print(result)
                  speak(rand)
                  
        elif('define') in message:
                #print(dictionary.synonym("indentation"))
            query = message
            stopwords = ['define']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ''.join(resultwords)
            rand = (dictionary.synonym(result))
            speak(rand)
                
                  
# CRAZY JARVIS ==============================================================================================================BRAIN 4

        elif("daddy's home") in message:
                speak("Welcome back sir, I hope you have been having a pleasure all day?")        

            
        elif ('i am') in message:
                speak("wonderful, anything I can assist you with?")

        elif('yes') in message:
            speak("what can I do for you ?")

        elif('tell me a joke')in message:
            rand=(pyjokes.get_joke())
            print(rand)
            speak(rand)
                                    
        elif("who is there")in message:
            speak("Merry")
        
        elif('merry who')in message:
            speak("Merry Christmas")

        elif('manis')in message:
            speak("Manish? Oh you mean Manish Prabhakar?, also known as The Format Guy of Team Alientrix. Chill! Its a joke, don't take it personally. But We truly believe he's gonna get his name on Guiness Book Of world records for Maximum number of PC Formatting. Dabba hay re dabba! , Manish ka lappy dabba!")

    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
        speak("Pardon sir, can you please repeat?")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
