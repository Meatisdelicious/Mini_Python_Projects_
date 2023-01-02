from ursina import *

app = Ursina()
carmera.orthographic = True
camera.fov = 10

car = Entity(
    module='quad'
    texture='assets\car'
    collide='box',
    scale=(2,1),
    rotation_z=-90
)
app.run()