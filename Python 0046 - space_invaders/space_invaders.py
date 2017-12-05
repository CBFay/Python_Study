# Experimentation with the pyglet module
# Created on 12.05.2017 by CB Fay

import pyglet
from pyglet.window import key
from GameObjects import GameObject

# classes can take objects as parameters to inherit from them
class GameWindow(pyglet.window.Window): 
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) # necessary to initialize subclasses?
		self.set_location(400, 200)
		self.frame_rate= 1/60.0
	
		self.player = GameObject(320, 20, 'PLAYER.png')
		# image = pyglet.image.load('res/sprites/PLAYER.png')
		# self.player = pyglet.sprite.Sprite(image, x=320, y=20)
		
	def on_draw(self):
		self.clear()
		self.player.sprite.draw()
		# self.player.draw()
		
	def update(self, dt):
		pass
		
if __name__ == "__main__":
	window = GameWindow(640, 480, "Space Invaders", resizable=False)
	pyglet.clock.schedule_interval(window.update, window.frame_rate)
	pyglet.app.run()