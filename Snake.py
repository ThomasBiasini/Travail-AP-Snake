
from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
for i in range(15) :
    for j in range(30) :
        # les coordonnées de rectangle que l'on dessine
        x = 40*i+20*(j%2) # coordonnée x (colonnes) en pixels
        y = 20*j # coordonnée y (lignes) en pixels
        width = 20 # largeur du rectangle en pixels
        height = 20 # hauteur du rectangle en pixels
        rect = pg.Rect(x, y, width, height)
        # appel à la méthode draw.rect()
        color = (255, 0, 0) # couleur rouge
        pg.draw.rect(screen, color, rect)

score = 0
# les coordonnées du corps du serpent
snake = [(10, 15),(11, 15),(12, 15)]

direction = [1,0]

fruit=(randint(0,31), randint(0,31))
rect_fruit = pg.Rect(fruit[0]*20,fruit[1]*20, width, height)
pg.draw.rect(screen, [0, 0, 255], rect_fruit)
# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
tour=0
while running:
    tour+=1
    clock.tick(1)
    for i in range(1,len(snake)) :
        if snake[i]==snake[0] and tour>2  :
           
            running=False
    pg.display.set_caption(f"score:{score}")
    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_UP :
                n_direction = (0,-1)
            elif event.key == pg.K_DOWN :
                n_direction = (0,1)
            elif event.key == pg.K_LEFT :
                n_direction = (-1,0)
            elif event.key == pg.K_RIGHT :
                n_direction = (1,0)    
    
    
            if not (n_direction[0]!=0 and n_direction[0]==-direction[0]) or (n_direction[1]!=0 and n_direction[1]==-direction[1]) :
                direction=n_direction

    
    
    a=snake.pop()
    x=snake[0]
    x=(x[0]+direction[0], x[1]+direction[1])
    rect_a_recolorier = pg.Rect(a[0]*20, a[1]*20, width, height)
    if a[0]%2==a[1]%2 :
        color_recoloriage = [255, 0, 0]
    else :
        color_recoloriage = [0, 0 ,0]
    pg.draw.rect(screen, color_recoloriage, rect_a_recolorier)
    
    snake.insert(0,x)
    for i in range(len(snake)) :
        recti = pg.Rect(snake[i][0]*20, snake[i][1]*20, width, height)
        color_serp =  [255, 255, 255]
        pg.draw.rect(screen, color_serp, recti)
    
    if snake[0]==fruit :
        snake.insert(0,(fruit[0]+direction[0],fruit[1]+direction[1]))
        fruit=(randint(0,31),randint(1,31))
        score+=1

    rect_fruit = pg.Rect(fruit[0]*20,fruit[1]*20, width, height)
    pg.draw.rect(screen, [0, 0, 255], rect_fruit)

    
    

    pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()