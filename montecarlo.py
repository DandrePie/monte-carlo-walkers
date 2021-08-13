from board import Board

class MonteCarlo(Board):
    '''
    A class to represent the MonteCarlo simulation of the random walk

    ...
    Attributes
    ----------
    n_samples : int
        The number of samples
    board_size: int
        The size of the grid that the random walkers move on
    store_location: bool
        If store_location is True, the paths of all the walkers
        stored to the walks dictionary
    count: int
        The number of times walkers have met on the grid
    probability: float
        The probability that the random walkers have met on the grid
    walks: dict
        A dict that stores the random walks and if the walk resulted
        in a meeting on the grid

    Methods
    -------
    MC_simulation(walker1, walker2)
        Performs montecarlo simulation
    probability_calculate()
        Modifies the probability attribute
    reset_board()
        Resets the board i.e. setting the walkers back to starting
        positions
    '''

    def __init__(self, n_samples=2500, board_size=9, store_location=False):
        Board.__init__(self, board_size, store_location)
        self.store_location = store_location # if t
        self.n_samples = n_samples
        self.count = 0
        self.probability = 0
        self.walks = {}

    def MC_simulation(self, walker1, walker2):
        '''
        Simulates n_samples of the random walkers to determine the probability that
        the walkers meet on the grid.
            Parameters:
                walker1: Walker object - location at the bottom left of grid
                walker2: Walker object - location at the top right of grid
        '''
        for sample in range(0, self.n_samples):
            self.simulate_walk(walker1, walker2)
            if self.met == 'Met':
                self.count += 1

            # Appending the walk to a dictionary and resetting board
            if self.store_location:
                self.walks['walk ' + str(sample+1)] = self.walker_location, self.met

            self.reset_board(walker1, walker2)
            # Resetting location of walkers to starting location

        self.probability_calculate()

    def probability_calculate(self):
        self.probability = self.count/self.n_samples

    def reset_board(self,walker1,walker2):
        '''
        Resets the board after each sample
        '''

        self.walker_location = []
        self.met = 'Not met'
        self.inbounds = 'In boundary'
        walker1.reset_location()
        walker2.reset_location()





