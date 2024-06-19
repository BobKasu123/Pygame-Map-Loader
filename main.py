import pygame

Class MapLoader:
  def load_file_map(screen, file: str, images: dict, x: int, y: int):
    map = file.split("\n")
    if len(file) > 0:
      for row in map:
        for tile, img_num in zip(row, images):
          if tile == img_num:
            screen.blit(pygame.image.load(images[img_num]), (x, y)
          x += 5
        y += 5
    else:
      for tile, img_num in zip(map, images):
        if tile == img_num:
          screen.blit(pygame.image.load(images[img_num]), (x, y))
          
  def load_map(screen, map: list, images: dict, x, y):
    if len(map) > 0:
      for row in map:
        for tile, img_num in zip(row, images):
          if num == img_num:
            screen.blit(pygame.image.load(images[img_num]), (x, y))
          x += 5
        y += 5
    else:
      for tile, img_num in zip(map, images):
        if tile == img_num:
          screen.blit(pygame.image.load(images[img_num]), (x, y))
