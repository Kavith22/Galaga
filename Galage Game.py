import pgzrun
HEIGHT=500
WIDTH=500

ship=Actor('ship.png')
ship.x=250
ship.y=400

score=0
game_over = False    

bullets=[]
aliens=[]

x=50
y=50

for row in range(5):
    for i in range(5):
        alien=Actor('wasp.png')
        alien.y=y
        x=x+70
        alien.x=x
        aliens.append(alien)
    x=50
    y=y-50

def draw():
    screen.clear()
    screen.fill('#414640')

    if game_over:    
        screen.draw.text("GAME OVER", center=(250,250), fontsize=60, color="red")
        return

    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for alien in aliens:
        alien.draw()
    screen.draw.text(str(score),(10,10))

def update():
    global score, game_over

    if game_over:    
        return

    if keyboard.left:
        ship.x -= 4
    if keyboard.right:
        ship.x += 4

    if keyboard.space:
        bullet=Actor('bullet.png')
        bullet.x=ship.x
        bullet.y=ship.y-43
        if len(bullets)<=1:
            bullets.append(bullet)


    for b in bullets[:]:   
        b.y -= 5
        if b.y < 0:
            bullets.remove(b)


    for alien in aliens[:]:  
        alien.y += 0.7

        if alien.colliderect(ship):  
            game_over = True

        
        for b in bullets[:]:
            if b.colliderect(alien):
                aliens.remove(alien)
                bullets.remove(b)
                score += 1
                break

pgzrun.go()
