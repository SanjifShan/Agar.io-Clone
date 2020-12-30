# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19:30:52 2020

@author: sanjif
"""

import pygame
import math
import random
from queue import PriorityQueue

WIDTH = 800
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.init()
font = pygame.font.SysFont('comicsans', 30)
pygame.display.set_caption("Agar.io")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

def positive_or_negative():
    if random.random() < 0.5:
        return 1
    else:
        return -1

class Opponent:
	def __init__(self, x, y, size, color):
		self.x = x
		self.y = y
		self.size = size
		self.velocity = math.sqrt(size) * 5
		self.x_velocity = 0
		self.y_velocity = 0
		self.color = color

	def update_position(self):
		self.x_velocity = random.uniform(0, self.velocity) * positive_or_negative()
		self.y_velocity =  math.sqrt(math.pow(self.velocity,2) - math.pow(self.x_velocity,2)) * positive_or_negative()
		self.x += self.x_velocity
		self.y += self.y_velocity

	def get_position(self):
		return (self.x, self.y)
	
	def out_of_bounds(self):
		if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
			self.dead()
	
	def place_in_centre(self):
			self.size = 15
			self.x = WIDTH/2
			self.y = HEIGHT/2

	def dead(self):
		self.change_size(0)

	def get_size(self):
		return self.size

	def change_colour(self, colour):
		self.color = colour

	def change_size(self, size):
		self.size = size

	def draw_opponent(self, WIN):  
		pygame.draw.circle(WIN, self.color, (int(self.x), int(self.y)), self.size)


	def eat(self):
		for key, value in food.items():
			if distance(value, self.get_position()) < self.size:
				self.size += 5
				food[key] = (random.randint(0,WIDTH), random.randint(0,HEIGHT))
			
class Player:
	def __init__(self, x, y, size, color):
		self.x = x
		self.y = y
		self.size = size
		self.velocity = math.sqrt(size) * 2
		self.x_velocity = 0
		self.y_velocity = 0
		self.color = color

	def get_position(self):
		return (self.x, self.y)

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_velocity(self):
		return self.velocity
	
	def out_of_bounds(self):
		if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
			self.dead()

	def dead(self):
		self.change_size(0)

	def get_size(self):
		return self.size

	def change_colour(self, colour):
		self.color = colour

	def change_size(self, size):
		self.size = size

	def draw_player(self, WIN):  
		pygame.draw.circle(WIN, self.color, (int(self.x), int(self.y)), self.size)

	def eat(self):
		for key, value in food.items():
			if distance(value, self.get_position()) < self.size:
				self.size += 5
				food[key] = (random.randint(0,WIDTH), random.randint(0,HEIGHT))
	
	def collision(self, players):
		for i in range(0, 10):			
			if (distance(players[i].get_position(), self.get_position())) < players[i].get_size() + self.get_size():
				if players[i].get_size() > self.get_size():
					players[i].change_size(players[i].get_size() + self.get_size())
					self.change_size(15)
					self.dead()
				else:
					self.change_size(players[i].get_size() + self.get_size())
					players[i].change_size(15)
					players[i].dead()						
				
def distance(p0, p1):
    return math.sqrt(math.pow(p0[0]-p1[0],2) + math.pow(p0[1]-p1[1],2))

def draw_food(food):
	for value in food.values():
		pygame.draw.circle(WIN, WHITE, value, 5)

def collision(players):
	for i in range(0, 10):
		for j in range(i+1, 10):
			
			if (distance(players[i].get_position(), players[j].get_position())) < players[i].get_size() + players[j].get_size():
				if players[i].get_size() > players[j].get_size():
					players[i].change_size(players[i].get_size() + players[j].get_size())
					players[j].change_size(15)
					players[j].dead()
				else:
					players[j].change_size(players[i].get_size() + players[j].get_size())
					players[i].change_size(15)
					players[i].dead()

				
				#players[i].change_colour(BLUE)
				#players[j].change_colour(BLUE)	
							
def show_score(players):
	for key, value in players.items():
		print(value.get_size())

#Sanjif = Player(400, 400, 15, BLUE)
food = {k: (random.randint(0,WIDTH), random.randint(0,HEIGHT)) for k in range(50)}
players = {k: Opponent(random.randint(0,WIDTH),random.randint(0,HEIGHT), 15, PURPLE) for k in range(10)}

def main(WIN):
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()


		WIN.fill((0, 0, 0))
		text0 = font.render('Player_1: ' + str(players[0].get_size()), 1, WHITE)
		text1 = font.render('Player_2: ' + str(players[1].get_size()), 1, WHITE)
		text2 = font.render('Player_3: ' + str(players[2].get_size()), 1, WHITE)
		text3 = font.render('Player_4: ' + str(players[3].get_size()), 1, WHITE)
		text4 = font.render('Player_5: ' + str(players[4].get_size()), 1, WHITE)
		text5 = font.render('Player_6: ' + str(players[5].get_size()), 1, WHITE)
		text6 = font.render('Player_7: ' + str(players[6].get_size()), 1, WHITE)
		text7 = font.render('Player_8: ' + str(players[7].get_size()), 1, WHITE)
		text8 = font.render('Player_9: ' + str(players[8].get_size()), 1, WHITE)
		text9 = font.render('Player_10: ' + str(players[9].get_size()), 1, WHITE)
		WIN.blit(text0, (0,0))
		WIN.blit(text1, (0,30))
		WIN.blit(text2, (0,60))
		WIN.blit(text3, (0,90))
		WIN.blit(text4, (0,120))
		WIN.blit(text5, (0,150))
		WIN.blit(text6, (0,180))
		WIN.blit(text7, (0,210))
		WIN.blit(text8, (0,240))
		WIN.blit(text9, (0,270))

	
		draw_food(food)
		for key, value in players.items():

			value.update_position()
			value.draw_opponent(WIN)
			value.eat()
			value.out_of_bounds()

		
		collision(players)

		show_score(players)

		

		pygame.time.delay(100)
		pygame.display.update()

		
	


main(WIN)