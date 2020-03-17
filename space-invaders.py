from tkinter import PhotoImage
import turtle
from turtle import Turtle, Screen, Shape
import os
import math
import random


window = turtle.Screen()
window.bgcolor('black')
window.title('Space Invaders')

gameover = turtle.Screen()
window.bgcolor('black')
window.title('Game Over')


border = turtle.Turtle()
border.speed(0)
border.color('white')
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
    border.hideturtle()


score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align='left',
                font=("Times New Roman", 14, 'normal'))
score_pen.hideturtle()


player = turtle.Turtle()
smallerPlayer = PhotoImage(file='boris.gif').subsample(3, 3)
window.addshape('larger', Shape('image', smallerPlayer))
player.shape('larger')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15


enemies = 10
enemies_list = []

for i in range(enemies):
    enemies_list.append(turtle.Turtle())

for enemy in enemies_list:
    smaller = PhotoImage(file='coronavirus.gif').subsample(3, 3)
    window.addshape('smaller', Shape('image', smaller))
    enemy.shape('smaller')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2


bullet = turtle.Turtle()
bullet.color('red')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 30
bullet_state = 'ready'


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def shoot_bullet():
    global bullet_state
    if bullet_state == 'ready':
        bullet_state = 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) +
                         math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


turtle.listen()
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')
turtle.onkeypress(shoot_bullet, 'space')


while True:
    for enemy in enemies_list:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if enemy.xcor() > 280:
            for e in enemies_list:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies_list:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = 'ready'
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align='left',
                            font=("Times New Roman", 14, 'normal'))

    if collision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print('Player 1 Died')
        break

    if bullet_state == 'fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

        if bullet.ycor() > 275:
            bullet.hideturtle()
            bullet_state = 'ready'


window.mainloop()
