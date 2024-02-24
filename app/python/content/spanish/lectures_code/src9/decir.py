import cowsay
import pyttsx3

motor = pyttsx3.init()
esto = input("¿Qué es esto? ")
cowsay.cow(esto)
motor.say(esto)
motor.runAndWait()