import pygame

# Fixed some stuff
# To use: make a dictionary with integer keys and values of only the path of an image
# Then, make a list of the numbers you defined in the dictionary. this'll load the map using the numbers in the list
# If the number isnt defined in the dict itll automatically skip the number
# So you can use something like 0 to leave spaces (if u want)

class MapLoader:
  def load_file_map(self, screen, file: str, images: dict, x: int, y: int, width: int, height: int):
    f = open("file", "r")
    map = file.read().split("\n")
    if len(map) > 0:
      for row in map:
        for int(tile), img_num in zip(row, images):
          if tile in images:
            screen.blit(pygame.transform.scale(pygame.image.load(images[img_num]), (width, height)), (x, y))
          x += width
        y += height
    else:
      for int(tile), img_num in zip(map, images):
        if tile in images:
          screen.blit(pygame.transform.scale(pygame.image.load(images[img_num]), (width, height)), (x, y))
        x += width
          
  def load_map(self, screen, map: list, images: dict, x, y, width: int, height: int):
    if len(map) > 0:
      for row in map:
        for int(tile), img_num in zip(row, images):
          if num in images:
            screen.blit(pygame.transform.scale(pygame.image.load(images[img_num]), (width, height)), (x, y))
          x += width
        y += height
    else:
      for int(tile), img_num in zip(map, images):
        if tile in images:
          screen.blit(pygame.transform.scale(pygame.image.load(images[img_num]), (width, height)), (x, y))
        x += width
        
