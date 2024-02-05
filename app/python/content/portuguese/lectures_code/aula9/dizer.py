import cowsay
import pyttsx3

motor = pyttsx3.init()
isto = input("O que é isso? ")
cowsay.cow(isto)
motor.say(isto)
motor.runAndWait()