import pyautogui as auto
from PIL import Image
import pygame
import keyboard as key


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Screen:
    def __init__(self):
        pass

    def screenshot(self):
        return auto.screenshot()

    def draw(self):
        # Screenshot
        screenshot = self.screenshot()

        screenshot.save("images/sys/screenshot.png")
        size = auto.size()
        pygame.init()
        window = pygame.display.set_mode(size, pygame.FULLSCREEN)

        # Load Background Image
        image = pygame.image.load("images/sys/screenshot.png")

        outer_rect = pygame.Rect(0, 0, size[0], size[1])

        cropped = False
        start_coordinates = None
        end_coordinates = None
        release = False

        while not cropped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        start_coordinates = Coordinate(auto.position()[0], auto.position()[1])

                elif event.type == pygame.MOUSEBUTTONUP:
                    if release is True:
                        release = False
                        continue
                    if event.button == 3:
                        start_coordinates = None
                        end_coordinates = None
                        release = True
                    else:
                        end_coordinates = Coordinate(auto.position()[0], auto.position()[1])
                        if start_coordinates.x == end_coordinates.x or start_coordinates.y == end_coordinates.y:
                            start_coordinates = None
                            end_coordinates = None
                        else:
                            cropped = True
                """elif event.type == pygame.:
                    end_coordinates = Coordinate(auto.position()[0], auto.position()[1])
                    cropped = True"""

                """start_coordinates = Coordinate(auto.position()[0], auto.position()[1])
                    while key.is_pressed(interruption_key):
                        end_coordinates = Coordinate(auto.position()[0], auto.position()[1])
                    if end_coordinates is not None:
                        cropped = True"""
            window.blit(image, (0, 0))
            if start_coordinates is not None:
                pos = auto.position()
                rectangle = pygame.Rect(start_coordinates.x, start_coordinates.y,
                                        pos[0]-start_coordinates.x, pos[1]-start_coordinates.y)
                pygame.draw.rect(window, (255, 255, 255), rectangle, 5)
            pygame.draw.rect(window, (255, 255, 255), outer_rect, 13)
            pygame.display.update()

        return start_coordinates, end_coordinates

    def crop(self, screenshot: Image.Image, start_coordinates: tuple, end_coordinates: tuple):
        coordinates = (start_coordinates[0], start_coordinates[1], end_coordinates[0], end_coordinates[1])
        return screenshot.crop(coordinates)

