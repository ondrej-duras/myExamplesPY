
import random
from visual import *

scene.title='Pokusne jednofarebne kopceky ako plocha'
scene.height = 480; scene.width = 640
scene.x = 50
scene.y = 10
scene.z = 0
#scene.focus=(0,0,1)
scene.background=color.blue
#scene.fullscreen = True


body = [];
for z in range(0,100,1):
  body.append([])
  for x in range(0,100,1):
    body[z].append( vector(x, random.uniform(0.0,3.0), z) )

pole = [];
for z in range(0,99,1):
  for x in range(0,99,1):
    pole.extend( [ body[z][x], body[z][x+1], body[z+1][x], 
                   body[z+1][x], body[z][x+1], body[z+1][x+1] 
                 ])
fr = frame()
#plachta = faces(pos = pole, material = materials.plastic, color = color.green, normal = vector(0,0.5,-0.3))
#plachta = faces(pos = pole, material = materials.wood, color = color.green, normal = vector(0,0.5,-0.3))
plachta = faces(
            pos = pole, 
            material = materials.marble, 
            color = (0.99, 0.8, 0.3), 
            normal = vector(0,0.5,-0.3), 
            frame = fr
          )
plachta.make_twosided()

#for y in range(50, -50, -1):
#  rate(20)
#  fr.pos = (0,y/100.0,0)





