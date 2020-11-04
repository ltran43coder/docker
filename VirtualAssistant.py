import speech_recognition
from gtts import gTTS
import os

#create brain for bot, first time it might be null
bot_brain = "";
#create ear for bot to listen
bot_ear = speech_recognition.Recognizer()

while True:
    with speech_recognition.Microphone() as mic:
        print("\nBot: I'm listening")
        #audio = bot_ear.listen(mic)
        audio = bot_ear.record(mic, duration= 3) #bot only listen within 3sec
        print("\nBot: ....")
    try:
        you = bot_ear.recognize_google(audio,language='en-EN')# nó sẽ lấy giọng của chị Google
        print("\nYou: "+you)
    except:
        you ="I did not understand what you said."
        print("\nBot: "+you)

    if "hi" in you:
        bot_brain = "Hello friend"
    elif "weather" in you:
        bot_brain = " today is wonderful day"
    elif "work" in you:
        bot_brain = "Yes, you have a lot of thing to do"
    elif "bye" in you:
        bot_brain = "Good bye. See you again"
        break;
    else:
        bot_brain = " I do not understand, please try again."
        print("\nBot: " + bot_brain)
    print("\nBot: " + bot_brain)


# def print_hi(name):
#     print(f'Hi, {name}')

# if __name__ == '__main__':
#     print_hi('PyCharm')