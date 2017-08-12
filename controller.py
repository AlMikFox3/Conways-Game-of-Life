# Game of Life Controller

from engine import Grid

class Controller():
    def __init__(self, dimensions):
        self.dimensions = dimensions # dimensions of the grid
        self.paused = True # the game starts paused
        
        self.grid = Grid(dimensions)
    
    def toggleCellStatus(self, cell): # toggle between dead/alive
        if self.grid.statusGrid[cell[0]][cell[1]] == False:
            self.grid.statusGrid[cell[0]][cell[1]] = True
        else:
            self.grid.statusGrid[cell[0]][cell[1]] = False
    
    def togglePause(self):
        if self.paused == False: self.paused = True
        else: self.paused = False
    
    def clearGrid(self):
        self.grid = Grid(self.dimensions)
    
    def getLiveCellList(self):
        liveCells=[]
        for y in range(self.dimensions[0]):
            for x in range(self.dimensions[1]):
                if self.grid.statusGrid[y][x]: liveCells.append((x,y))
        return liveCells
    
    def update(self):
        if not self.paused: self.grid.runGame()
