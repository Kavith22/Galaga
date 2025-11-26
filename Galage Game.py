import pgzrun
HEIGHT=500
WIDTH=500
ship=Actor('ship.png')
ship.x=(250)    
ship.y=(400)
score=0
x=(50)    
y=(50)
bullets=[]
aliens=[]
for row in range(5):
    for i in range(5):
        alien=Actor('wasp.png')
        aliens.append(alien)
        alien.y=y
        x=x+70
        aliens[-1].x=x
    x=50
    y=y-50
    
def draw():
    screen.clear()
    screen.fill('#414640')
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for alien in aliens:
        alien.draw()
    screen.draw.text(str(score),(10,10))
                                 

def update():
    global score
    if keyboard.left:
        ship.x=ship.x-4
    if keyboard.right:
        ship.x=ship.x+4
    if keyboard.space:
        bullet=Actor('bullet.png')
        bullet.x=(ship.x)
        bullet.y=(ship.y-43)
        if len(bullets)<=1:
            bullets.append(bullet)
    for i in bullets:
        i.y=i.y-5
        if i.y<0:
            bullets.remove(i)
    for alien in aliens:
        alien.y=alien.y+0.7 
        for bullet in bullets:
            if bullet.colliderect(alien) and len(aliens)>0:
                aliens.remove(alien)
                score=score+1
pgzrun.go()        