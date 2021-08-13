class Board:
    '''
    A class to simulate the grid on which the random walkers walk
    ...
    Attributes
    ----------
    board_size: int
        The board_size represents the size of the n*n grid
    inbounds: str
        'In boundary' - the random walkers are within the bounds
        of the grid
        'On boundary' - the random walkers are on the bounds of
        the grid - end condition for the simulation
    met: str
        'Not met' - the random walkers have not met on the grid
        'Met' - the random walkers met on the grid
    store_location: bool
        If store_location is True the paths of the walkers are stored
    walker_location: list
        List that stores walker paths

    '''
    def __init__(self, board_size=9, store_location=True):
        self.board_size = board_size
        self.inbounds = 'In boundary'
        self.met = 'Not met'
        if store_location:
            self.walker_location = []

    def simulate_walk(self, walker1, walker2):
        '''
        Simulates the random walk of the walkers on the grid
        Handles the speed of each walker

        Parameters:
                walker1: Walker object - location at the bottom left of grid
                walker2: Walker object - location at the top right of grid
        '''
        # append initial locations of random walkers to walker_location
        self.location_update(walker1, walker2)

        while self.inbounds == 'In boundary' and self.met == 'Not met':

            for speed in range(1, max(walker1.speed, walker2.speed)+1):

                if speed <= walker1.speed and speed <= walker2.speed:
                    walker1.walk(self.board_size)
                    walker2.walk(self.board_size)

                elif walker1.speed < speed <= walker2.speed:
                    walker2.walk(self.board_size)

                elif walker1.speed >= speed > walker2.speed:
                    walker1.walk(self.board_size)

                #Store locations of walkers on the board
                self.location_update(walker1, walker2)
                #Check if walkers are still within the boundary of the board or that they have met on the board
                self.end_walk_condition(walker1, walker2)
                if self.inbounds == 'On boundary' or self.met == 'Met':
                    break

    def end_walk_condition(self, walker1, walker2):
        '''
        Checks if the walkers have met of the grid or if they are still within bounds
            - modifies the inbounds and met attributes.
        Parameters:
                walker1: Walker object - location at the bottom left of grid
                walker2: Walker object - location at the top right of grid

        '''
        walk1_end = walker1.x == self.board_size and walker1.y == self.board_size
        walk2_end = walker2.x == 1 and walker2.y == 1
        if walk1_end or walk2_end:
            self.inbounds = 'On boundary'
        if [walker1.x, walker1.y] == [walker2.x, walker2.y]:
            self.met = 'Met'

    def location_update(self, walker1, walker2):
        '''
        Appends the location of the walkers to the walker location list

        Parameters:
                walker1: Walker object - location at the bottom left of grid
                walker2: Walker object - location at the top right of grid
        '''
        if self.store_location:
            self.walker_location.append([[walker1.x, walker1.y], [walker2.x, walker2.y]])
        else:
            pass
        
