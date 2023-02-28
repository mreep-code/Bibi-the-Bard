import os
import random
from random import randint, choice
import math
import pygame
from os import listdir
from os.path import isfile, join
import time

pygame.init()

#Set screen dimensions
screen_width = 960
screen_height = 720
FPS = 24

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Speckled Soup")

#Set sprite sheets
def load_sprite_sheets(dir1, dir2, width, height):
    path = join("images", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.rotozoom(surface, 0, 8))

            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

# Define the Customer class
class Customer(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = 240
        self.rect.bottom = 648

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# Load the customer images
CUSTOMER_IMAGES = [pygame.image.load("images/customers/"f"customer{i}.png").convert_alpha() for i in range(1, 8)]

# Create the customers
customers = pygame.sprite.Group()
for image in CUSTOMER_IMAGES:
    customer = Customer(image)
    customers.add(customer)

# Randomly select a customer to show up
current_customer = random.choice(customers.sprites())

#Create forest
forest = pygame.image.load("images/background/forest.png").convert_alpha()
forest_rect = forest.get_rect()
forest_rect.bottom = 720

# Create serving counter
counter = pygame.image.load("images/background/counter.png").convert_alpha()
counter_rect = counter.get_rect()
counter_rect.bottom = 720

def main(screen):
    clock = pygame.time.Clock()
    clock.tick(FPS)

    rungame = True

    while rungame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                rungame = False
                break
    
        # Draw forest
        screen.blit(forest, forest_rect)

        # Draw customers
        screen.blit(current_customer.image, current_customer.rect)

        # Draw serving counter
        screen.blit(counter, counter_rect)

        pygame.display.update()

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(screen)
