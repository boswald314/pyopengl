import pygame
import random
import math




background_colour = (255, 255, 255)
(width, height) = (1200, 800)
elasticity = 0.5



def collide(p1, p2):
	dx = p1.x - p2.x
	dy = p1.y - p2.y
	
	dist = math.hypot(dx, dy)
	if dist < p1.size + p2.size:
		p1dxi = p1.dx
		p1dyi = p1.dy
		p2dxi = p2.dx
		p2dyi = p2.dy

		p1.dx = int((p1.mass*p1dxi + p2.mass*p2dxi) / p1.mass)
		p1.dy = int((p1.mass*p1dyi + p2.mass*p2dyi) / p1.mass)
		p2.dx = int((p1.mass*p1dxi + p2.mass*p2dxi) / p2.mass)
		p2.dy = int((p1.mass*p1dyi + p2.mass*p2dyi) / p2.mass)


class Particle():
	"""docstring for Particle"""
	def __init__(self, x, y, size, mass=1):
		self.x = x
		self.y = y
		self.size = size
		self.mass = mass

		self.dx = 0
		self.dy = 0
		self.colour = (0, 0, 255)
		self.thickness = 0

	def display(self):
		pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

	def move(self):
		self.x = self.x + self.dx
		self.y = self.y + self.dy

	def bounce(self):
		if self.x > width - (self.size*2):
			self.dx = self.dx * -1
			self.dx = int(self.dx * elasticity)
			self.dy = int(self.dy * elasticity)
		elif self.x < (self.size*2):
			self.dx = self.dx * -1
			self.dx = int(self.dx * elasticity)
			self.dy = int(self.dy * elasticity)

		if self.y > height - (self.size*2):
			self.dy = self.dy * -1
			self.dx = int(self.dx * elasticity)
			self.dy = int(self.dy * elasticity)
		elif self.y < (self.size*2):
			self.dy = self.dy * -1
			self.dx = int(self.dx * elasticity)
			self.dy = int(self.dy * elasticity)





screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 3')

number_of_particles = 50
my_particles = []


for n in range(number_of_particles):
	size = random.randint(10, 20)
	density = random.randint(1, 20)
	x = random.randint(size, width-size)
	y = random.randint(size, height-size)

	myparticle = Particle(x, y, size, density * size**2)

	myparticle.dx = random.randint(-10,10)
	myparticle.dy = random.randint(-2,2)
	myparticle.colour = (200 - density * 10, 200 - density * 10, 255)

	my_particles.append(myparticle)



running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(background_colour)

	for i, particle in enumerate(my_particles):
		particle.move()
		particle.bounce()
		for particle2 in my_particles[i+1:]:
			collide(particle, particle2)
		particle.display()
	pygame.display.flip()























