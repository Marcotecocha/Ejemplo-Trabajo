import turtle
import time
import random

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

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo de la serpiente
segmentos = []

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    #Game Over: Bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder la cola de serpiente despues de perder
        for segmento in segmentos:
            segmento.goto(1000,1000)
        
        #Limpiar la cola
        segmentos.clear()



    #Colisiones con la comida
    if cabeza.distance(comida) < 20:
       x = random.randint(-280,280)
       y = random.randint(-280,280)
       comida.goto(x,y)

       nuevo_segmento = turtle.Turtle()
       nuevo_segmento.speed(0)
       nuevo_segmento.shape("square")
       nuevo_segmento.color("gray")
       nuevo_segmento.penup()
       segmentos.append(nuevo_segmento)

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    mov()
    time.sleep(posponer)

#Manera de perder: Tocando los bordes