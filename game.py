
import pygame, sys
from pygame.locals import *
from time import sleep
pygame.init()

import controller

gridDimensions = (85,55) # in cells
generationPeriod = 0.05 # pause between generations (in seconds)
delay = 0.01
scale = 9
gap = 10 # the gap is used to let black lines between the white rectangles

WINDOW = pygame.display.set_mode(map(lambda x: x*gap, gridDimensions)) 
# Set the window size based on the dimensions of the grid and the scale. The map part transforms (50,50) - the dimension of the grid in cells - to (300,300) - a appropriated dimension for the window in pixels
CAPTION = pygame.display.set_caption('Game of Life')
SCREEN = pygame.display.get_surface()

control = controller.Controller(gridDimensions)

print "Display Initialized"


pygame.display.update()

def drawGrid():
    for y in range(gridDimensions[1]):
        for x in range(gridDimensions[0]):
            pygame.draw.rect(SCREEN, (255, 255, 255), (x*gap,y*gap, scale, scale))
    cellList = control.getLiveCellList()
    for cell in cellList: pygame.draw.rect(SCREEN, (0, 100, 0), (cell[1]*gap,cell[0]*gap, scale, scale))


print "Starting Main Loop"

getRectCoordinates = lambda coor:map(lambda b: b*gap, map(lambda a: a/gap, coor))


getCellCoordinates = lambda coor: map(lambda a: a/gap, coor)

while True:
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        elif event.type ==  MOUSEBUTTONDOWN:
            rectCoor = getRectCoordinates(pos)
            cellCoor = getCellCoordinates(pos)
            control.toggleCellStatus(cellCoor)
        elif event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_r]:
                control.clearGrid()
            if pygame.key.get_pressed()[K_p]: 
                control.togglePause()
    
    control.update()
    drawGrid()
    
    pygame.display.update()
    sleep(generationPeriod)
