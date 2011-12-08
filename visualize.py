import pygame
import sys
import re

pygame.init()

pygame.display.set_caption("Output")

done = False
map = pygame.image.load(sys.argv[1])
screen = pygame.display.set_mode(map.get_size())

pos = []
pos_file = open(sys.argv[2], 'r')
for line in pos_file:
	pos_split =  re.split(';', line.strip())
	pos.append([float(pos_split[0]), float(pos_split[1]), float(pos_split[2])])

screen.blit(map, [0,0])
for p in pos:
	screen.set_at([int(p[0]), int(p[1])], [255, 0, int(255*p[2])])

pygame.display.flip()
print(sys.argv[2])
print(re.split("\.",sys.argv[2]))
print(re.split("\.",sys.argv[2])[0])
pygame.image.save(screen, "V_"+re.split("\.",sys.argv[2])[0]+"_"+sys.argv[1])

pygame.quit ()

