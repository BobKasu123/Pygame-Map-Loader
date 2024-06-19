import pygame

# Fixed some stuff

Class MapLoader:
  def load_file_map(screen, file: str, images: dict, x: int, y: int, width: int, height: int):
    map = file.split("\n")
    if len(file) > 0:
      for row in map:
        for tile, img_num in zip(row, images):
          if tile == img_num:
            screen.blit(pygame.transform.scale(pygame.image.load(images[img_num]), (width, height)), (x, y))
          x += width
        y += height
    else:
      for tile, img_num in zip(map, images):
        if tile == img_num:
          screen.blit(pygame.transform.scale(pygame.image.load(images[img_num]), (width, height)), (x, y))
          
  def load_map(screen, map: list, images: dict, x, y):
    if len(map) > 0:
      for row in map:
        for tile, img_num in zip(row, images):
          if num == img_num:
            screen.blit(pygame.transform.scale(pygame.image.load(images[img_num]), (width, height)), (x, y))
          x += width
        y += height
    else:
      for tile, img_num in zip(map, images):
        if tile == img_num:
          screen.blit(pygame.transform.scale(pygame.image.load(images[img_num]), (width, height)), (x, y))
