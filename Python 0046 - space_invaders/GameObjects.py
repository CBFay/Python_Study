import pyglet

class GameObject:
	def __init__(self, posx, posy, image=None, hidden=False):
		self.posx = posx # position
		self.posy = posy
		self.velx = 0 # velocity
		self.vely = 0
		if image is not None:
			image = pyglet.image.load('res/sprites/'+image)
			self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)
