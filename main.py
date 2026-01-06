import psutil
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

bat = psutil.sensors_battery()

if bat is None:
    speak("Information Not Available")
else:
    p = bat.percent
    pl = bat.power_plugged

    if p == 100:
        speak("I am full")
    elif p <= 20:
        if pl:
            speak("I am eating and I am hungry")
        else:
            speak("I am hungry")
    else:
        if pl:
            speak(f"I am eating and I am {p} percent")
        else:
            speak(f"{p} percent")
