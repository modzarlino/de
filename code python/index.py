import random
import turtle
import time



print("Choisis le nombre de dés")
nbDes=input()


print("Choisis la taille des dés")
taille=input()

print("Choisis la couleur des dés")
couleur=input()

print("Choisis la couleur des points")
points=input()

turtle.penup()
turtle.goto(-900,0)

def lancer(taille, couleur, points, d, e):
    turtle.pencolor(couleur)

    turtle.penup()
    turtle.pendown()

    turtle.forward(taille)
    turtle.left(90)
    

    turtle.forward(taille) 
    turtle.left(90) 
    

    turtle.forward(taille)
    turtle.left(90) 
    
    turtle.forward(int(taille)) 
    turtle.left(90)



    turtle.penup()
    turtle.pendown()
    origine=turtle.pos()
    turtle.penup()
    turtle.goto(e, taille/2)
    for x in range(d):
        turtle.dot(int(taille)/25,points)
        turtle.penup()
        turtle.forward(int(taille)/10)
        turtle.pendown()
    turtle.penup()
    turtle.goto(origine)
    turtle.forward(taille*1.2)





for k in range (int(nbDes)):
    d=random.randint(1,6)
    e=-900+((int(taille)*1.2)*k-1)+int(taille)/2-int(taille)/20*(d-1)
    lancer(int(taille), couleur, points, d, e)
turtle.hideturtle()







