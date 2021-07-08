import turtle
import time

posponer = 0.1

#Configuración de Ventana
wn = turtle.Screen()
wn.title("Juego de Pong")
wn.bgcolor("Black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"


while True:
    wn.update()

    time.sleep(posponer)}
    cabeza.goto(0,200)
    

#Creación de Ventana del juego y cabeza de la serpiente
