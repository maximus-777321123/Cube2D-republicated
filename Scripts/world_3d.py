from ursina import *

def run():
    app = Ursina()

    player = Entity(model='cube', color=color.orange, scale_y=2)
    ground = Entity(model='plane', collider='box', scale=100, color=color.green)
    camera.parent = player
    camera.position = (0, 10, -30)
    camera.rotation_x = 30

    def update():
        speed = 5 * time.dt
        if held_keys['w']: player.z -= speed
        if held_keys['s']: player.z += speed
        if held_keys['a']: player.x -= speed
        if held_keys['d']: player.x += speed

    app.run()
