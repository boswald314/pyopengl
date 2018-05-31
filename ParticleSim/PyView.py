import pygame
import PyParticles

pygame.display.set_caption("My First Particle Simulator")
(width, height) = (1200, 800)
screen = pygame.display.set_mode((width, height))

env = PyParticles.Universe(width,height)

env.addParticles(50)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	env.update()
	screen.fill(env.colour)

	for p in env.particles:
		pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, p.thickness)



	pygame.display.flip()

