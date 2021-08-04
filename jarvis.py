#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options


import pyttsx3 # used to convert text to speech
import speech_recognition as sr #used to convert speech to text
import datetime  #To get current date and time
import os  # To start or run computer applications
import wikipedia # To search wikipedia
import webbrowser # To run applications on webbrowser
import pywhatkit # For whatsapp messages
import wolframalpha # Api used to search about anything and to perform calculations
import pyjokes # To find random jokes
import cv2 # to operate camera
import eyed3 # to play songs
import time # time module
from requests import get # requests method
from PyDictionary import PyDictionary #to use dictionary
import smtplib # For sending mails
import pyautogui # for switching screens
import requests # For sending requests
import random # To find random numbers
from email import encoders # for sending emails
from email.mime.multipart import MIMEMultipart # to send media files
from email.mime.text import MIMEText # to send  multimedia msg
from englisttohindi.englisttohindi import EngtoHindi # to translate english sentence to hindi
from email.mime.base import MIMEBase # to send multimedia msg
import instaloader # to open insta profiles or download profile pictures
import PyPDF2 #to read pdf
import sys #for system related operations
import psutil
import speedtest


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis_ui.jarvisui import Ui_MainWindow
import json


#********************************* twilio id *************************************************

account_sid = 'AC3e766182b94df0ad339f39094a1941a0'
auth_token = '5a5c1dab181f3edf4ce6b25e02757be1'
from twilio.rest import Client

client = Client(account_sid, auth_token)

#********************************* Setting up engine for speaking**********************************


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',178)

#*************************************wolframalpha api id******************************************


app_id = 'WGUU35-XVLU6GVAX3'


#************************************open weathermap api***********************************

weather_api_id = '52da3398c2669115baf8858f9953e328'



#*********************************** pdf reader function*******************************************


def pdf_reader():
    speak("Enter the path of book:")
    loc = input()
    book = open(loc,'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book are {pages}")
    speak("Please tell me the page number from where you would like me to read the pdf")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

#******************************* Function to send a email******************************************


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('agarwalgaurav060699@gmail.com', 'Drk@l@mide@l99')
    server.sendmail('agarwalgaurav060699@gmail.com', to, content)
    server.close()


#*********************************Function to calculate various things****************************

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None


#****************************Function to get date*******************************************

def date():
    """
    Just return date as string
    :return: date if success, False if fail
    """
    try:
        curr_date = datetime.datetime.now().strftime("%b %d %Y")
    except Exception as e:
        print(e)
        curr_date = False
    return curr_date


#******************************function to get current time********************************


def curr_time():
    """
    Just return time as string
    :return: time if success, False if fail
    """
    try:
        curr_time = datetime.datetime.now().strftime("%H:%M:%S")
    except Exception as e:
        print(e)
        curr_time = False
    return curr_time


#********************************* Speak function *******************************************************************


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#***************************************** Startup function*********************************************************

def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning")
    elif 12 < hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = curr_time()
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")

    # function to take command from user ( speech to text )



#************************************* GUI DESIGNING ******************************************

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    #**********************************To take command from user***********************************************

    def take_command(self) -> object:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout = 20,phrase_time_limit=5)

        try:
            print("Recognizing..")
            self.query1 = r.recognize_google(audio, language='en-in')
            print(f"User said :{self.query1}")

        except Exception as e:
            #speak("Sorry Can you please repeat..")
            return "none"
        return self.query1

    #************************function for all the tasks***********************************************

    def TaskExecution(self):
        startup()
        while True:
            self.query1 = self.take_command().lower()
            # logic building for jarvis

            # *************************************************to Open notepad ***************************************

            if "hello" in self.query1:
                speak("I am fine sir...")
                speak("what about you ...")

            elif "open notepad" in self.query1:
                speak("opening notepad for you sir")
                file_path = "C:\\WINDOWS\\system32\\notepad.exe"
                path = file_path.lower()
                os.startfile(path)

            # *********************************** to open chrome*****************************************************

            elif "open chrome" in self.query1:
                speak("Just wait for a while sir , opening chrome ")
                file_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                path = file_path.lower()
                os.startfile(path)

            # ************************************ to open visual studio *******************************************

            elif "open visual studio" in self.query1:
                speak("opening visual studio for you sir")
                file_path = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\Common7\\IDE\\devenv.exe"
                path = file_path.lower()
                os.startfile(path)

            # **********************************************to search something in wikipedia**********************************

            elif "tell me about" in self.query1 or "search wikipedia" in self.query1:
                speak("Searching in wikipedia , just wait for a while sir....")
                topic = self.query1.split(' ')[-1]
                results = wikipedia.summary(topic, sentences=2)
                speak("According to wikipedia")
                speak(results)


            # ********************************************open youtube*********************************************************

            elif "open youtube" in self.query1:
                webbrowser.open("www.youtube.com")



            # **************************************** to open youtube video***************************************************

            elif 'youtube' in self.query1:
                speak("which video you want me to play?")
                video = self.take_command().lower()
                speak(f"Okay sir, playing {video} on youtube")
                pywhatkit.playonyt(video)

            # ******************
            # ********************** to open college website************************************************

            elif "open my college website" in self.query1 or "open gbpec " in self.query1 or "open gbpiet website" in self.query1:
                speak("opening Your college website sir")
                webbrowser.open("http://www.gbpec.ac.in")


            # *************************************** to know current date**************************************************

            elif "date" in self.query1:
                curr_date = date()
                speak(f"The current date is {curr_date}")


            # *************************************To get current time ****************************************************

            elif "time" in self.query1:
                curr_time = time()
                speak(f"The current time is {curr_time}")


            # ***********************************To calculate any value using wolframalpha api****************************

            elif "calculate" in self.query1:
                question = self.query1
                answer = computational_intelligence(question)
                speak(answer)


            # **********************************To know about anything or anyone using wolframalpha***********************

            elif "what is" in self.query1 or "who is" in self.query1:
                question = self.query1
                answer = computational_intelligence(question)
                speak(answer)


            # **********************************To open facebook in browser***********************************************

            elif "open facebook" in self.query1 or "facebook" in self.query1 or "fb" in self.query1:
                webbrowser.open("www.facebook.com")


            # *********************************** To open instagram******************************************************

            elif "open instagram" in self.query1:
                webbrowser.open("www.instagram.com")


            # ********************************** To open google**********************************************************

            elif "open google" in self.query1 or "search in google" in self.query1 or "search on google" in self.query1:
                speak("Sir, what should i search on google")
                qw = self.take_command().lower()
                pywhatkit.search(qw)


            # ********************************** To get a random joke****************************************************

            elif "joke" in self.query1 or "jokes" in self.query1:
                speak("finding a joke for you sir")
                joke = pyjokes.get_joke(language="en", category="all")
                speak(joke)


            # ************************************To open microsoft word*************************************************

            elif "open microsoft word" in self.query1 or "open word" in self.query1 or "open ms word" in self.query1:
                pyttsx3.speak("Opening")
                pyttsx3.speak("MICROSOFT WORD")
                os.system("start winword")


            # **********************************To open microsoft excel*************************************************

            elif ("open microsoft excel" in self.query1) or ("open excel" in self.query1) or ("open ms excel" in self.query1) or (
                    "open sheet" in self.query1) or ("open winexcel" in self.query1):
                pyttsx3.speak("Opening")
                pyttsx3.speak("MICROSOFT EXCEL")
                os.system("start excel")

            # ******************************************To open cmd******************************************************

            elif "open cmd" in self.query1 or "open command prompt" in self.query1:
                os.system('start cmd')


            # ************************************************To open powerpoint*****************************************

            elif ("open slide" in self.query1) or ("open mspowerpoint" in self.query1) or ("open ppt" in self.query1) or (
                    "open powerpnt" in self.query1):
                pyttsx3.speak("Opening")
                pyttsx3.speak("MICROSOFT POWERPOINT")
                os.system("start powerpnt")


            # *********************************************To open msedge************************************************

            elif ("open ie" in self.query1) or ("open msedge" in self.query1) or ("open edge" in self.query1):
                pyttsx3.speak("Opening")
                pyttsx3.speak("MICROSOFT EDGE")
                os.system("start msedge")


            # *************************************To open camera**********************************************************


            elif "open camera" in self.query1:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            # ******************************************To play music******************************************************


            elif "play music" in self.query1 or "play songs" in self.query1 or "play song" in self.query1:
                speak("playing music for you sir")
                music_dir = "E:\songs"
                songs = os.listdir(music_dir)
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
                duration = eyed3.load(f'E:\\songs\\{song}').info.time_secs
                time.sleep(duration)


            # ***********************************************To find ip address********************************************


            elif "ip address" in self.query1:
                ip = get("https://api.ipify.org").text
                speak(f"Your IP address is{ip}")


            # ***************************************** To send a whatsapp message *******************************************


            elif "send a whatsapp message" in self.query1 or "send whatsapp message" in self.query1 or "whats up message" in self.query1:

                speak("Sir please enter the contact number...")
                name = input()
                phone_no = name
                speak("what would you like to say sir ?")
                msg = self.take_command().lower()
                h = int(datetime.datetime.now().hour)
                m = int(datetime.datetime.now().minute) + 2
                speak("Okay sir..just wait for a minute sending your message...It might take a minute "
                      "sir")

                pywhatkit.sendwhatmsg(phone_no, msg, h, m)
                speak("Successfully sent the message sir...")

            # *************************************To send a email with or with a file attached************************************


            elif 'email' in self.query1 or 'send mail' in self.query1 or "mail" in self.query1:
                try:
                    speak("please tell me the email subject sir")
                    sub = self.take_command().lower()
                    speak("What should I say?")
                    content = self.take_command()
                    speak("To whoom you would like to send the mail Can you please enter the email address in terminal")
                    m_id = input()
                    speak("would you like to attach any file?")
                    res = self.take_command().lower()

                    msg = MIMEMultipart()
                    msg['From'] = 'agarwalgaurav060699@gmail.com'
                    msg['To'] = m_id
                    msg['Subject'] = sub

                    msg.attach(MIMEText(content, 'plain'))
                    if 'yes' in res:  # to attach a file
                        speak("please enter the path of file to be sent in terminal")
                        file_location = input()
                        filename = os.path.basename(file_location)
                        attachment = open(file_location, "rb")
                        part = MIMEBase('applicatiojn', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', "attachment; filename=%s" % filename)

                        msg.attach(part)
                    text = msg.as_string()
                    sendEmail(m_id, text)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir, I am not able to send this email")


            # ********************************To close an app ********************************************************************

            elif 'close' in self.query1:
                app = self.query1.replace('close', "")
                speak(f"Okay sir,closing {app}")
                os.system(f"taskkill /f /im {app}.exe")


            # *******************************To shut down the system **************************************************************

            elif "shut down the system" in self.query1:
                os.system("shutdown /s /t s")


            # ***********************************************To restart the system**************************************************

            elif "restart the system" in self.query1:
                os.system("shutdown /r /t s")


            # ************************************************To sleep the system****************************************************

            elif "sleep the system" in self.query1:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


            # ***************************************************To switch screens*************************************************

            elif "switch screens" in self.query1 or "switch tabs" in self.query1 or "switch windows" in self.query1:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(3)
                pyautogui.keyUp("alt")


            # ******************************Using news api to get latest news********************************************************

            elif "tell me news" in self.query1 or "tell me today's news" in self.query1 or "current news" in self.query1 or "today's news" in self.query1:
                speak("what would you like to hear?tech or indian news ")
                type = self.take_command().lower()

                # *********************************************for technology news***************************************************

                if type == 'tech' or type == 'technology' or type == 'technical':
                    main_url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a46cb384eb564748948c1e60d13e0c76'


                # ***********************************************for indian news******************************************************

                else:
                    main_url = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=a46cb384eb564748948c1e60d13e0c76'

                main_page = requests.get(main_url).json()
                articles = main_page["articles"]
                head = []
                day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tenth']
                for ar in articles:
                    head.append(ar['title'])
                for i in range(len(day) - 1):
                    speak(f"today's {day[i]} news is: {head[i]}")




            # ******************* to find or know about anything or anyone using wolframalpha api********************************

            elif "where i am" in self.query1 or "where am i" in self.query1 or "current location" in self.query1:
                speak("Wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"Sir i am not sure ,but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("Sorry sir,Due to network issue i can't find your current location")
                    pass


            # *********************************Function to take anyone instagram profile pic*************************************

            elif "search instagram profile" in self.query1 or "search a profile on instagram" in self.query1:
                time.sleep(5)
                speak("Sir please enter the user name correctly")
                name = input("Enter username")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile pic of the user {name}")
                time.sleep(5)
                speak("Sir would you like to download profile picture of this account,")
                condition = self.take_command().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()  # install using pip install instaloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I am done sir,profile pic saved in our main folder.Now i m ready to perform another task")


            # *****************************************Function To take screen shot **********************************************

            elif "take screenshot" in self.query1 or "take ss" in self.query1:
                speak("Sir,please tell me name for this screenshot")
                name = self.take_command().lower()
                speak("Sir, please hold the screen for few seconds, i am taking the screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done sir, the screenshot is saved in our main folder")


            # ***********************************Read a pdf like audio book*******************************************************

            elif "read pdf" in self.query1:
                pdf_reader()


            # ********************************************************** Meaning Of any word using pydictionary******************

            elif "find the meaning" in self.query1 or "find meaning" in self.query1 or "get meaning" in self.query1 or "dictionary" in self.query1:
                dict = PyDictionary()
                speak("Which word's meaning you would like to find")
                word = self.take_command().lower()
                meaning = dict.meaning(word)
                speak(f"The meaning of {word} is: {meaning}")

            # *********************************************** Translate a sentence or word in hindi**********************************

            elif "translate" in self.query1 or "translate in hindi" in self.query1:
                speak("What would you like to translate sir")
                text_word = self.take_command().lower()
                res = EngtoHindi(text_word)
                speak("You can see the translation in console sir..")
                print(res.convert)
                time.sleep(5)


            # ***********************************************  hide files and folder****************************

            elif "hide all files" in self.query1 or "hide this folder" in self.query1 or "visible for everyone" in self.query1:
                speak("Sir please tell me you want to hide this folder or make it visible to everyone")
                condition = self.take_command().lower()
                if "hide" in self.query1:
                    os.system("attrib +h /s /d")
                    speak("Sir, all the files in this folder are hidden now")

                elif "visible" in self.query1:
                    os.system("attrib -h /s /d")
                    speak("Sir, all the files in this folder are now visible to everyone")

                elif "leave it" in self.query1 or "leave for now" in self.query1:
                    speak("Ok sir")

            # *****************************************Thanking jarvis******************************************

            elif "thank you" in self.query1 or "thanks" in self.query1:
                speak("My pleasure sir")

            # ********************************** to pause working jarvis ***************************************

            elif "sleep" in self.query1 or "you can sleep" in self.query1:
                speak("Okay sir, i am going to sleep you can call me anytime.")
                break;

            # *************************************** get current weather details ******************************

            elif "weather" in self.query1 or "current weather" in self.query1:
                speak("Tell the city name")
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                city = self.take_command().lower()
                complete_url = base_url + "appid=" + weather_api_id + "&q=" + city
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    round(current_temperature,2)
                    current_pressure = y["pressure"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(f" Temperature in celsius is {current_temperature-273.15}")
                    speak(f"Current atmospheric pressure is {current_pressure} hpa unit")
                    speak(f"humidity is {current_humidity} percent")
                    speak(f"overall it is {weather_description}")

                else:
                    speak(" City Not Found ")

            #***********************************current battery percentage***********************************

            elif "how much power left" in self.query1 or "power left" in self.query1 or "battery left" in self.query1 or "battery percentage" in self.query1:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"Sir our system have {percentage} percent battery left")
                if percentage>=75:
                    speak("We have enough power to continue our work")
                elif percentage>=30 and percentage<=75:
                    speak("You should connect the charger")
                else:
                    speak("We are very low on power sir.... Immediately connect the charger")

            #****************************************Speed test function**************************************

            elif "internet speed" in self.query1:
                speak("Checking sir..please wait for a while")
                st = speedtest.Speedtest()
                dl = st.download()
                dl = (dl*1.25)/10000000
                up = st.upload()
                up =(up*1.25)/10000000
                speak(f"Sir downloading speed is {round(dl,2)} MBp's")
                speak(f"Sir uploading speed is {round(up,2)} MBp's")

            # ****************************************Volume up and down*********************************
            elif 'volume up' in self.query1:
                pyautogui.press("volumeup")

            elif 'volume down' in self.query1:
                pyautogui.press("volumedown")

            elif "mute" in self.query1:
                pyautogui.press("volumemute")


           #*****************************************Sending a text message *******************************
            elif "text message" in self.query1:
                speak("Sir what should i say")
                msg = self.take_command()
                message = client.messages \
                .create(
                body=msg,
                from_='+18312788044',
                to='+917500573903'
                )
                speak("Message has been sent successfully sir...")

                # *****************************************Sending a text message *******************************
            elif "call" in self.query1:
                message = client.calls \
                    .create(
                    twiml='<Response><Say>Hello Gaurav.. This is a testing message of jarvis..</Say></Response>',
                    from_='+18312788044',
                    to='+917500573903'
                )
                speak("Calling sir...")

            elif "goodbye" in self.query1:
                 speak("Thanks for using me sir,have a nice day")
                 sys.exit()


#***************************************Main program******************************************************

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
         self.ui.movie = QtGui.QMovie("C:/Users/Dell/PycharmProjects/jarvis_project/gui_images/jarvis_img.gif")
         self.ui.label.setMovie(self.ui.movie)
         self.ui.movie.start()
         self.ui.movie = QtGui.QMovie("C:/Users/Dell/PycharmProjects/jarvis_project/gui_images/initializing_jarvis.gif")
         self.ui.label_2.setMovie(self.ui.movie)
         self.ui.movie.start()
         self.ui.movie = QtGui.QMovie("C:/Users/Dell/PycharmProjects/jarvis_project/gui_images/a1.gif")
         self.ui.label_3.setMovie(self.ui.movie)
         self.ui.movie.start()
         timer = QTimer(self)
         timer.timeout.connect(self.showTime)
         timer.start(1000)
         startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:m:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())












# if __name__ == "__main__":
#     startup()
#
#     while True:
#         permission = take_command()
#         if "wake up" in permission:
#             TaskExecution()
#         elif "goodbye" in permission:
#             speak("Thanks for using me sir,have a nice day")
#             sys.exit()



