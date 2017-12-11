# Experimentation with the pyglet module
# Created on 12.05.2017 by CB Fay
# Updated on 12.10.2017

import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key, FPSDisplay
from GameObjects import GameObject, preload_image

# classes can take objects as parameters to inherit from them
class GameWindow(pyglet.window.Window): 
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) # necessary to initialize subclasses?
		self.set_location(400, 200)
		self.frame_rate= 1/60.
		self.fps_display = FPSDisplay(self)
		self.fps_display.label.font_size = 6
		self.fps_display.label.y = 5
		self.fps_display.label.x = 5

		self.right = False
		self.left = False
		self.player_speed = 100
			
		player_spr = Sprite(preload_image('PLAYER_10x.png'))
		self.player = GameObject(80, 5, player_spr)
		
		self.space_list = []
		self.space_img = preload_image('SPACE.png')
		for i in range(2):
			self.space_list.append(GameObject(0, i*160, Sprite(self.space_img)))
		
		for space in self.space_list:
			space.vely = -100
			
	def update_space(self, dt):
		for space in self.space_list:
			space.update(dt)
			if space.posy <= -160:
				self.space_list.remove(space)
				self.space_list.append(GameObject(0, 160,  Sprite(self.space_img)))
			space.vely = -100
				
	def on_key_press(self, symbol, modifiers):
		if symbol == key.RIGHT:
			self.right = True
		if symbol == key.LEFT:
			self.left = True
		if symbol == key.ESCAPE:
			pyglet.app.exit()
			
	def on_key_release(self, symbol, modifiers):
		if symbol == key.RIGHT:
			self.right = False
		if symbol == key.LEFT:
			self.left = False
		
	def on_draw(self):
			self.clear()
			for space in self.space_list:
				space.draw()
			self.player.draw()
			self.fps_display.draw()

	def update_player(self, dt):
		self.player.update(dt)
		if self.right and self.player.posx < 182:
			self.player.posx += self.player_speed * dt
		if self.left and self.player.posx > 1:
			self.player.posx -= self.player_speed * dt
		
	def update(self, dt):
			self.update_player(dt) # 'data time'
			self.update_space(dt) # 'data time'

			
if __name__ == "__main__":
	window = GameWindow(192, 160, "Space Invaders", resizable=False)
	pyglet.clock.schedule_interval(window.update, window.frame_rate)
	pyglet.app.run()
