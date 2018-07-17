import random
import time
import pycountry
import os
import os.path
import wikipedia
from weather import Weather
import re
import pyjokes
import requests
import wolframalpha
import webbrowser
import glob
from PyDictionary import PyDictionary
import tmdbsimple as tmdb
edm='https://www.youtube.com/watch?v=3RMywOVg3'
edml=['edm','dubstep','trance','electric']
app_id='XPAQWX-W5LAG5ELYL'
client=wolframalpha.Client(app_id)
tmdb.API_KEY = '60222ace6396c345f94cc42eaac5dae5'
doss = os.getcwd()
i=0
n=0
flag=0
dictionary=PyDictionary()
weather = Weather()
favcolor= ("purple")
brothersname=("jarvis")
ameye=("artificial intelligence")
my = []
tco = ()
iam=[]
lnames=[]
info = []
add1=()
add2=()
infa = []
lstn=()
ups = ()
clear = lambda: os.system('cls')
nxt = (0)
nxts =(4)
nogt = (0)
noot = (1)
myname = ("jarvia")
commands = []
action = []
print ("hello")
name = input ("what is your name>>> ")
print ("hello " + name)
while 1==1:
    response = input("Main>>> ")
    if response == "what time is it" or response=='what is the time':
        print(time.strftime("%I")+':'+time.strftime('%M %p'))
    elif response == ("what is your favorite color"):
        print("purple")
    elif response == ("who are you"):
        print ("jarvia")
    elif response == "what are you":
        print ("an AI")
    elif response == ("cool"):
        print ("mhm")
    elif ('what can you do') in response:
        rand = ('I can do Tasks as Playing Music, Videos, Opening any file, websites,Google Search,Movie Search, Put Computer to sleep, Arithmatic Operations, Normal Conversations, Jokes and many more')
    elif('goodbye')  in response:
        print('Ok goodbye')
        break
    elif('shutdown')in response:
        break
    elif ('thanks') in response or ('tanks') in response or ('thank you') in response:
        print('You are welcome', 'no problem')


    elif response == ('jarvia'):
        print('Yes Sir?', 'What can I do for you sir?')


    elif('how are you') in response or ('and you') in response or ('are you okay') in response:
        print('Im good, thanks')
    elif ('your name') in response:
        print("Im Jarvia")
    elif ('how old are you') in response :
        print("none of your buisness")
    elif('what is my location') in response or ('where am I') in response or ('where are you') in response :
        w = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1275004&appid=5fc29900336d19d1d912723dc3d1e117')
        json_object = w.json()
        loc_lon = (float(json_object['coord']['lon']))
        rand1 = str(loc_lon)
        loc_lat = (float(json_object['coord']['lat']))
        rand2 = str(loc_lat)
        print("The current position is "+rand1+" longitude and "+rand2+" latitude")
    elif('will you marry me') in response:
        print('I am sorry.. The person you are trying to contact is currently unavailable, please try again later or join the queue for your turn')
    elif('what is life') in response :
        print("Food")
#    elif ret.code==200:
#        webbrowser.open('http://'+response)
#        print ('Opening')
    elif 'open email' in response:
        if mail==1:
            webbrowser.open(email)
            print ('Opening mail')
        else:
            esite=input('What email site do you use: ')
            if 'gmail' in response:
                mail=1
                email='https://www.gmail.com'
                webbrowser.open(email)
            elif 'yahoo' in response:
                mail=1
                email='https://mail.yahoo.com'
                webbrowser.open(email)
            elif 'outlook' in response:
                mail=1
                email='https://outlook.live.com'
                webbrowser.open(email)

    elif ('google search') in response :
        query = response
        stopwords = ['google', 'search']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        webbrowser.get(Chrome).open('https://www.google.com/search?sourceid=chrome&ie=utf-8&oe=utf-8&aq=t&hl=&q='+result)
    elif ('google maps') in response:
        query = response
        stopwords = ['google', 'maps']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")


    elif ('install python module') in response:
        query = response
        stopwords = ['module']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        print("installing")
        os.system('python -m pip install ' + result)
    elif('subtract') in response :
        input = response
        (a,b,c,d) =[t(s) for t,s in zip((str,int,str,int),re.search('^(\w+) (\d+) (\w+) (\d+)$',input).groups())]
        result = int(b-d)
        print(result)

    elif('multiply') in response :
        input = response
        (a,b,c,d) =[t(s) for t,s in zip((str,int,str,int),re.search('^(\w+) (\d+) (\w+) (\d+)$',input).groups())]
        result = int(b*d)

        print(result)

    elif('divide') in response :
        input = response
        (a,b,c,d) =[t(s) for t,s in zip((str,int,str,int),re.search('^(\w+) (\d+) (\w+) (\d+)$',input).groups())]
        result = float(b/d)

        print(result)


    elif('define') in response:

        query = response
        stopwords = ['define']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ''.join(resultwords)
        rand = (dictionary.synonym(result))
        print(rand)


    elif('tell me a joke')in response:
        rand=(pyjokes.get_joke())
        print(rand)







    elif response == ("do you have a brother"):
        print("yes")
    elif response == "thanks" or response == "thank you":
        print("mhm")
    elif response == ("what is your brothers name"):
        print("jarvis")
    elif response == ("who created you"):
        print("zpit367")
    elif response == ("what language were you coded in"):
        print("python")
    elif response == "what is your name":
        print(myname)
    elif response == "clear":
        clear()
    elif response == "what is my name":
        print(name)
    elif "new list" in response:
        lname=input("list name>>> ")
        lnames.append(lname)
        f= open(lname+".txt","w+")
        f.close()
    elif "add " in response and "to list " in response:
        lstn=response.find("to list ")
        lstn=response[(lstn+8):len(response)]
        add1=(response.find("add")+4)
        add2=response.find(" to list ")
        if os.path.isfile(lstn)==True:
            f=open(lstn+".txt", "a+")
            f.write(response[add1:add2])
            f.close()
    elif response == "give me a random number":
        print (random.randint(1,100))
    elif response == "what is the date":
        print (time.strftime (" %A, %B %e, %Y"))
    elif "weather " in response:
        wthr=(response.find("weather"))
        if "weather in " in response:
            wthr=((response.find("weather in "))+2)
            if wthr not in pycountry.countries:
                location = weather.lookup_by_location(response[wthr:(len(response))])
                condition = location.condition
                print(condition.text)
            else:
                print("Must be at most a state")
        else:
            print("where?")
            location = weather.lookup_by_location(input("Location: "))
            condition = location.condition()
            print(condition.text())
    elif response=="change name":
        print ("what would you like to change the name to?")
        myname = input("new name: ")
    elif response == "change my name":
        print("what would you like to change your name to")
        name = input ("new name: ")
        print("hello, " + name)
    elif "hello" in response:
        print ("hi")
    elif response == ("how do you spell your name"):
        print ("j-a-r-v-i-a")
    elif response == "calculator":
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x - y
        def multiply(x, y):
            return x * y
        def divide(x, y):
            return x / y
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        choice = input("calculator>>> ")
        num1 = int(input("calculator(Number 1)>>> "))
        num2 = int(input("calculator(Number 2)>>> "))
        if choice == '1':
            print(num1,"+",num2,"=", add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=", subtract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=", multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=", divide(num1,num2))
        else:
            print("Invalid input")
    elif "hi" in response:
        print ("hello")
    elif response == ("hello "+ myname):
        print("hello " + name)
    elif response == ("hi " + myname):
        print ("hello " + name)
    elif response[0:5] == ("i am "):
        nxt = (0)
        nxts = (1)
        while response[nxt:nxts] != (""):
            nxt = (nxt+1)
            nxts=(nxts+1)
        ups = tco
        ups = (response[5:nxt])
    elif response == "what am i":
        tikr=(iam)
        print(ups)
    elif commands.count (response) == 1:
        spot = commands.index (response)
        print(action[spot])
    elif response[0:2] == ("my"):
        nxt = 0
        nxts = 4
        while response [nxt:nxts] != (" is "):
            nxt = (nxt +1)
            nxts = (nxts+1)
            dk=nxts
        jb=nxt
        cmld= response[3:nxt]
        nxts = (nxt+11)
        if response[(nxt+4):(nxts-2)] == ("named"):
            dilk= (nxts-1)
            nxt = (nxt+0)
            nxts =(nxts+1)
            while response[nxt:nxts] != (""):
                nxt = (nxt+1)
                nxts=(nxts+1)
            action.append("your " + cmld)
            commands.append("who is " + response[dilk:nxts])
        else:
            nxt = (0)
            nxts = (1)
            while response[nxt:nxts] != (""):
                nxt = (nxt+1)
                nxts=(nxts+1)
            commands.append("what is " + response[0:jb])
            action.append(response[dk:nxt])
    elif "info on" in response:
        try:
            response = response[(response.find("info on")+8):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "what is" in response and not commands.count (response) == 1:
        try:
            response = response[(response.find("what is")+8):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "who is" in response:
        response = response[(response.find("who is")+7):len(response)]
        try:
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print(response)
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "who was" in response:
        response = response[(response.find("who was")+8):len(response)]
        try:
            res=client.query(response)
            print(next(res.results).text)
        except:

            print (wikipedia.summary(response, sentences=2))
            print(response)
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "what are" in response:
        try:
            response = response[(response.find("what are")+9):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))

    elif "what was" in response:
        try:
            response = response[(response.find("what is")+9):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "information on" in response or 'information about' in response or 'info on' in response or 'info about' in response:
        try:
            response = response[(response.find("information on")+15):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:

            print (wikipedia.summary(response, sentences=2))
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    else:

        command = response
        response = input("i dont understand, would you like to add this as a new command>>> ")

        if "y" in response and not "no" in response:
            commands.append(command)
            actionk = input("what should i say in response>>> ")
            action.append(actionk)
        else:
            print("ok")












