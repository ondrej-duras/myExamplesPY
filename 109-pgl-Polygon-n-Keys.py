#!/usr/bin/env python2
# https://stackoverflow.com/questions/54188353/how-do-i-make-3d-in-pyglet
import pyglet
from pyglet.gl import *

print "Klavesy W,S,A,D"

config = Config(sample_buffers=1, samples=8)
tela = pyglet.window.Window(height=500, width=500, config=config)

glViewport(0,0,500,500)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(35,1,0.1,1000)
glMatrixMode(GL_MODELVIEW)

@tela.event
def on_draw():
    glBegin(GL_POLYGON)
    glColor3ub(0,255,255)
    glVertex3f(10,10,0)
    glColor3ub(255,0,0)
    glVertex3f(100,10,0)
    glColor3ub(255,255,0)
    glVertex3f(50,100,0)
    glEnd()
    glFlush()

@tela.event
def on_key_press(s,m):
    tela.clear()
    if s == pyglet.window.key.W:
        glTranslatef(0,0,1)
    if s == pyglet.window.key.S:
        glTranslatef(0,0,-1)
    if s == pyglet.window.key.A:
        glRotatef(1,0,1,0)
    if s == pyglet.window.key.D:
        glRotatef(-1,0,1,0)

pyglet.app.run()
