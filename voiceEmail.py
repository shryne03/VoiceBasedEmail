
import speech_recognition as sr
import smtplib
 
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
import playsound
  
tts = gTTS(text="Project: Voice based Email for the unsighted", lang='en')
ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/name.mp3") 
tts.save(ttsname)

playsound.playsound(ttsname, True)
os.remove(ttsname)

#login from os
login = os.getlogin
print ("You are logging from : "+login())


mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
mail.starttls() #security connection
mail.login('dummyvoicebasedemail@gmail.com','dummyvoicebasedemail123') #login part

tts = gTTS(text="Successfully logged in:", lang='en')
ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
tts.save(ttsname)
playsound.playsound(ttsname, True)
os.remove(ttsname)

#choices
print ("1. Compose a mail.")
tts = gTTS(text="option 1. compose a mail.", lang='en')
ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
tts.save(ttsname)

playsound.playsound(ttsname, True)
os.remove(ttsname)

print ("2. Check your inbox")
tts = gTTS(text="option 2. Check your inbox", lang='en')
ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3")
tts.save(ttsname)

playsound.playsound(ttsname, True)
os.remove(ttsname)

#this is for input choices
tts = gTTS(text="Your choice ", lang='en')
ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
tts.save(ttsname)

playsound.playsound(ttsname, True)
os.remove(ttsname)

#voice recognition part
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Your choice:")
    audio=r.listen(source)
    print ("ok done!!")

try:
    text=r.recognize_google(audio)
    print ("You said : "+text)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
    tts = gTTS(text="Google Speech Recognition could not understand audio", lang='en')
    ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    playsound.playsound(ttsname, True)
    os.remove(ttsname) 

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    tts = gTTS(text="Could not request results from Google Speech Recognition service", lang='en')
    ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    playsound.playsound(ttsname, True)
    os.remove(ttsname) 

#choices details
if text == '1' or text == 'One' or text == 'one':
    r = sr.Recognizer() #recognize
    with sr.Microphone() as source:
        print ("Your message :")
        tts = gTTS(text="Your message: ", lang='en')
        ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)

        playsound.playsound(ttsname, True)
        os.remove(ttsname)
        audio=r.listen(source)
        print ("ok done!!")
    try:
        text1=r.recognize_google(audio)
        print ("You said : "+text1)
        tts = gTTS(text="You said: ", lang='en')
        ttsname1=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello1.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname1)
        playsound.playsound(ttsname1, True)
        os.remove(ttsname1)
        tts = gTTS(text=text1, lang='en')
        ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello2.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)

        playsound.playsound(ttsname, True)
        os.remove(ttsname)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        tts = gTTS(text="Google Speech Recognition could not understand audio", lang='en')
        ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        playsound.playsound(ttsname, True)
        os.remove(ttsname)

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
        tts = gTTS(text="Could not request results from Google Speech Recognition service", lang='en')
        ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        playsound.playsound(ttsname, True)
        os.remove(ttsname) 


    tts = gTTS(text="Do you want to send this mail? ", lang='en')
    ttsname1=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello1.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname1)
    playsound.playsound(ttsname1, True)
    os.remove(ttsname1)

    tts = gTTS(text="Your choice: ", lang='en')
    ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    playsound.playsound(ttsname, True)
    os.remove(ttsname)

    #voice recognition part
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Your choice:")
        audio=r.listen(source)
        print ("ok done!!")
    try:
        text3=r.recognize_google(audio)
        print ("You said : "+text3)
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        tts = gTTS(text="Google Speech Recognition could not understand audio. ", lang='en')
        ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)

        playsound.playsound(ttsname, True)
        os.remove(ttsname)
     
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
        tts = gTTS(text="Could not request results from Google Speech Recognition service. ", lang='en')
        ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        playsound.playsound(ttsname, True)
        os.remove(ttsname)


    if text3 == 'Yes' or text3 == 'yes' or text3 == 'YES':
        msg = text1
        mail.sendmail('dummyvoicebasedemail@gmail.com','dummyvoicebasedemail@gmail.com',msg) #send part
        print ("Congrats! Your mail has been sent. ")
        tts = gTTS(text="Congrats! Your mail has been sent. ", lang='en')
        ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/send.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        playsound.playsound(ttsname, True)
        os.remove(ttsname)
        mail.close()
    if text3 == 'No' or text3 == 'no' or text3 == 'NO':  
        print ("Safely logging you out:")
        tts = gTTS(text="Safely logging you out: ", lang='en')
        ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/send.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        playsound.playsound(ttsname, True)
        os.remove(ttsname)
        mail.close()
    
if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' or text =='chew':
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
    unm = ('dummyvoicebasedemail@gmail.com')  #username
    psw = ('dummyvoicebasedemail123')  #password
    mail.login(unm,psw)  #login
    stat, total = mail.select('Inbox')  #total number of mails in inbox
    print ("Number of mails in your inbox :"+str(total))
    tts = gTTS(text="Total mails are :"+str(total), lang='en') #voice out
    ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/total.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    playsound.playsound(ttsname, True)
    os.remove(ttsname)
 

    #search mails
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
    raw_email = email_data[0][1].decode("utf-8") #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/mail.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    playsound.playsound(ttsname, True)
    os.remove(ttsname)
    
    #Body part of mails
    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)
    tts = gTTS(text="Body: "+txt, lang='en')
    ttsname=("C:/Users/gonsa/Desktop/VoiceBasedEmail/body.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    playsound.playsound(ttsname, True)
    os.remove(ttsname)
    mail.close()
    mail.logout()

