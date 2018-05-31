import math, random


def collide(p1, p2):
	dx = p1.x - p2.x
	dy = p1.y - p2.y
	
	dist = math.hypot(dx, dy)
	if dist < p1.size + p2.size:
		tangent = math.atan2(dy, dx)


		p1vf = p1.velocity + ((p2.mass * p2.velocity) / p1.mass)
		p2vf = (((p1.mass * p1.velocity) + (p2.mass * p2.velocity)) / p2.mass) - ((p1.mass * p1.velocity) / p2.mass)

		y = math.pi - (2 * (p1.direction - tangent))
		p1.direction += y
		y = math.pi - (2 * (p2.direction - tangent))
		p2.direction += y

		p1.dx = math.sin(p1.direction) * p1vf
		p1.dy = math.cos(p1.direction) * p1vf
		p2.dx = math.sin(p1.direction) * p2vf
		p2.dy = math.cos(p1.direction) * p2vf

		angle = 0.5 * math.pi + tangent
		p1.x += math.sin(angle)
		p1.y -= math.cos(angle)
		p2.x -= math.sin(angle)
		p2.y += math.cos(angle)



class Particle():
	"""docstring for Particle"""
	def __init__(self, x, y, size, mass=1):
		self.x = x
		self.y = y
		self.size = size
		self.mass = mass

		self.dx = 0
		self.dy = 0
		self.velocity = math.sqrt(self.dx**2 + self.dy**2)
		self.direction = math.atan2(self.dy, self.dx)
		self.colour = (0, 0, 255)
		self.thickness = 0

	def move(self):
		self.x = self.x + self.dx
		self.y = self.y + self.dy








class Universe:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.particles = []

		self.acceleration = 0

		self.colour = (255, 255, 255)
		self.elasticity = 0.5


		self.particle_functions = []
		self.function_dict = {
		'move': lambda p: p.move(),
		'bounce': lambda p: self.bounce(p),
		'accelerate': lambda p: p.accelerate(self.acceleration)
		}


	def addParticles(self, n=1, **kargs):
		for i in range(n):
			size = kargs.get('size', random.randint(10,20))
			mass = kargs.get('mass', random.randint(10,100))
			x = kargs.get('x', random.uniform(size, self.width-size))
			y = kargs.get('y', random.uniform(size, self.height-size))

			p = Particle(x, y, size, mass)
			p.dx = kargs.get('dx', random.randint(-1,1))
			p.dy = kargs.get('dy', random.randint(-1,1))
			p.colour = kargs.get('colour', (0,0,255))

			self.particles.append(p)
			
	def update(self):
		""" Moves particles and checks for collisions with walls/other particles """

		for i, particle in enumerate(self.particles):
			particle.move()
			#if self.acceleration:
			#	particle.accelerate(self.acceleration)
			self.bounce(particle)
			for particle2 in self.particles[i+1:]:
				collide(particle, particle2)

	def bounce(self, particle):
		""" Tests whether a particle has hit the bouncdary of the environment """

		if particle.x > self.width - (particle.size):
			particle.x += ((particle.x + particle.size) - self.width)
			particle.dx = particle.dx * -1
			particle.dx = int(particle.dx * self.elasticity)
			particle.dy = int(particle.dy * self.elasticity)
		elif particle.x < (particle.size):
			particle.x -= (particle.x - particle.size)
			particle.dx = particle.dx * -1
			particle.dx = int(particle.dx * self.elasticity)
			particle.dy = int(particle.dy * self.elasticity)

		if particle.y > self.height - (particle.size):
			self.y = 2 * (self.height - particle.size) - particle.y
			particle.dy = particle.dy * -1
			particle.dx = int(particle.dx * self.elasticity)
			particle.dy = int(particle.dy * self.elasticity)
		elif particle.y < (particle.size):
			self.y = 2 * particle.size - particle.y
			particle.dy = particle.dy * -1
			particle.dx = int(particle.dx * self.elasticity)
			particle.dy = int(particle.dy * self.elasticity)






