# Create a display window
# Created on 12.05.2017 by CB Fay

import pyglet

class GameWindow(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.set_location(400, 200)
		self.frame_rate= 1/60.0
		
	def on_draw(self):
		self.clear()
		
	def update(self, dt):
		pass
		
if __name__ == "__main__":
	window = GameWindow(640, 480, "My Window", resizable=False)
	pyglet.clock.schedule_interval(window.update, window.frame_rate)
	pyglet.app.run()
