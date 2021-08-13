import matplotlib.pyplot as plt

class AnimateWalk:

    def __init__(self):
        self.probability = 0 # The probability of meeting count/samples
        self.count = 0 # The number of meetings
        self.samples = 0 # The number of random walks
        self.X1 = []
        self.Y1 = []
        self.X2 = []
        self.Y2 = []


    def __call__(self, frame, fig, ax):
        # If walkers do not meet on grid, update samples and probability
        if frame == 'Not met':
            self.clear_vectors()
            self.samples += 1
            self.probability = self.count / self.samples
            ax.set_title(f' samples ={self.samples}, meetings ={self.count}, probability ={self.probability:.2f}')
            if ax.lines:
                ax.lines.clear()
            else:
                pass
        # If walkers meet show marker on grid, update probability, samples and meetings and then clear figure
        elif frame == 'Met':
            ax.plot(self.X1[-1], self.Y1[-1], markersize=20, marker='*', color='green')
            self.clear_vectors()
            self.samples += 1
            self.count += 1
            self.probability = self.count / self.samples
            ax.set_title(f' samples ={self.samples}, meetings ={self.count}, probability ={self.probability:.2f}')


        else:
            x1 = frame[0][0]
            y1 = frame[0][1]

            x2 = frame[1][0]
            y2 = frame[1][1]

            self.X1.append(x1)
            self.Y1.append(y1)
            self.X2.append(x2)
            self.Y2.append(y2)
            if ax.lines:
                ax.lines.clear()
            else:
                pass

            ax.plot(self.X1, self.Y1, linestyle='-', linewidth=6,color='red')
            ax.plot(self.X2, self.Y2, linestyle='-', linewidth=3,color='blue')
            ax.set_title(f' samples ={self.samples}, meetings ={self.count}, probability ={self.probability:.2f}')
            fig.tight_layout()

    def clear_vectors(self):
        self.X1.clear()
        self.Y1.clear()
        self.X2.clear()
        self.Y2.clear()

