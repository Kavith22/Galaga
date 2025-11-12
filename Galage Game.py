import pgzrun
HEIGHT=500
WIDTH=500
ship=Actor('ship.png')
ship.x=(250)    
ship.y=(400)

bullets=[]
def draw():
    screen.clear()
    screen.fill('#414640')
    ship.draw()
    for bullet in bullets:
        bullet.draw()

def update():
    if keyboard.left:
        ship.x=ship.x-6
    if keyboard.right:
        ship.x=ship.x+6
    if keyboard.space:
        bullet=Actor('bullet.png')
        bullet.x=(ship.x)
        bullet.y=(ship.y-43)
        if len(bullets)<=1:
            bullets.append(bullet)
        
    for i in bullets:
        i.y=i.y-30
        if i.y<0:
            bullets.remove(i)

        


pgzrun.go()