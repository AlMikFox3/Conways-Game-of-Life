from numpy import ones, zeros
from copy import deepcopy

class Grid:
    def __init__(self, dimensions):
        self.dimensions = dimensions 
        self.statusGrid = zeros(dimensions, bool)
    
    def getNeighbours(self, cell):
        neighbours=[]
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                xi=cell[0]+x
                yi=cell[1]+y
                if  (x or y) and xi>=0 and yi>=0 and xi<self.dimensions[0] and yi<self.dimensions[1]:
                    neighbours.append((xi,yi))
        return neighbours
    
    def getCellStatus(self,cell):
        return self.statusGrid[cell[0]][cell[1]]
    
    def runGame(self): 
        bufferStatusGrid = deepcopy( self.statusGrid )
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                neighbours = self.getNeighbours((i,j)) 
                neighboursCount = 0
                for c in neighbours:
                    if self.getCellStatus(c): neighboursCount+=1
                
                if self.statusGrid[i][j] == False:
                    if neighboursCount==3:
                        bufferStatusGrid[i][j] = True
                else:
                    if neighboursCount<2 or neighboursCount>3: bufferStatusGrid[i][j]=False
        
        self.statusGrid = bufferStatusGrid
