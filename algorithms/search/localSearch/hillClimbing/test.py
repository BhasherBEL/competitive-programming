import best
import stochastic
import firstchoice
import probability

if __name__ == '__main__':

    get_neighbors = lambda x: [x-2, x-1, x+1, x+2]
    f = lambda x: -(x + 5)**2 + 5
    
    print(best.hillClimbing(10, get_neighbors, f))
    print(stochastic.hillClimbing(10, get_neighbors, f))
    print(firstchoice.hillClimbing(10, get_neighbors, f))
    print(probability.hillClimbing(10, get_neighbors, f))