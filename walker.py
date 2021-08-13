import random

class Walker:
    '''
    A class that represents the random walker

    ...
    Attributes
    ----------
    x: int
        The x cartesian coordinate of the walker
    y: int
        The y cartesian coordinate of the walker
    start_location: list [int, int]
        The starting location of the walker
    speed: int
        The speed at which the walker moves on the grid
    '''

    def __init__(self, location, speed=1):
        self.x = location[0]
        self.y = location[1]
        self.start_location = [self.x, self.y]
        self.speed = speed

    def walk(self, board_size):
        '''
        Simulates the movement of the walker on the grid.
        Walkers starting in the left-bottom corner can only move
        up and right - visa versa
        If walkers hit the boundary of the board/grid the will
        move along the boundary.

        Parameters:
            board_size: int
                The size of the board/grid
        '''

        if self.start_location == [1,1]:
            if self.x == board_size:
                self.y += 1
            elif self.y == board_size:
                self.x += 1
            else:
                (dxi, dyi) = random.choice([(0, 1), (1, 0)])
                self.x += dxi
                self.y += dyi

        elif self.start_location == [board_size, board_size]:
            if self.x == 1:
                self.y += -1
            elif self.y == 1:
                self.x += -1
            else:
                (dxi, dyi) = random.choice([(0, -1), (-1, 0)])
                self.x += dxi
                self.y += dyi

    def reset_location(self):
        ''' Resets the walker position to its starting position '''
        self.x, self.y = self.start_location



