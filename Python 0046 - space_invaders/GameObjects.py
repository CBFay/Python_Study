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
			
	def draw(self):
		self.sprite.draw()
		
	def update(self, dt):
		self.sprite.x += self.velx * dt
		self.sprite.y += self.vely * dt
		self.posx = self.sprite.x
		self.posy = self.sprite.y
