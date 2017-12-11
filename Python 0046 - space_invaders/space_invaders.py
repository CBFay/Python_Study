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
	
		self.player = GameObject(80, 5, 'PLAYER.png')
		
		self.space_list = []
		for i in range(2):
			self.space_list.append(GameObject(0, i*160, 'SPACE.png'))
		
		for space in self.space_list:
			space.vely = -100
			
	def update_space(self, dt):
		for space in self.space_list:
			space.update(dt)
			if space.posy < -80:
				self.space_list.remove(space)
				self.space_list.append(GameObject(0, 80, 'SPACE.png')) 
				for spc in self.space_list:
					spc.vely = -200
				
	def on_key_press(self, symbol, modifiers):
		if symbol == key.RIGHT:
			self.player.velx = 200
		if symbol == key.LEFT:
			self.player.velx = -200
			
	def on_key_release(self, symbol, modifiers):
		if symbol in (key.RIGHT, key.LEFT):
			self.player.velx = 0
		
	def on_draw(self):
			self.clear()
			for space in self.space_list:
				space.draw()
			self.player.draw()
		
	def update(self, dt):
			self.player.update(dt) # 'data time'
			self.update_space(dt) # 'data time'

			
if __name__ == "__main__":
	window = GameWindow(192, 160, "Space Invaders", resizable=False)
	pyglet.clock.schedule_interval(window.update, window.frame_rate)
	pyglet.app.run()
