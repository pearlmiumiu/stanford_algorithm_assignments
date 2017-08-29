from math import sqrt
from math import factorial
from time import time
from pprint import pprint
from itertools import combinations


def euc_dist(city1, city2):
    #print city1, city2, 'city------'
    """Computes the Euclidean distance between 'city1' and 'city2', which are
    2-tuple of coordinates."""
    df1 = city1[0] - city2[0]
    df2 = city1[1] - city2[1]
    return df1*df1 + df2*df2
    #return sqrt(pow(city1[0] - city2[0], 2) + pow(city1[1] - city2[1], 2))


def n_choose_k(n, k):
    """Computes n choose k."""

    if n < k:
        return 0
    else:
        return factorial(n) / factorial(k) / factorial(n - k)


def n_choose_k_table(num_of_cities):
    """Computes a dictionary which caches all possible n choose k computations."""
    table = {}
    for n in range(num_of_cities):
        for k in range(1, n + 2):
            table[(n, k)] = n_choose_k(n, k)
    return table


def comb_index(comb_start, comb, nck_table):
    """
    Computes a dense index for a given subset 'comb' in all subsets that have
    the same number of elements as 'comb'. 'comb_start' is the minimum element in
    the set from which subset 'comb' is obtained.
    http://en.wikipedia.org/wiki/Combinatorial_number_system
      comb        index
    (1, 2, 3)  -->  0
    (1, 2, 4)  -->  1
    (1, 2, 5)  -->  4
    (1, 3, 4)  -->  2
    (1, 3, 5)  -->  5
    (1, 4, 5)  -->  7
    (2, 3, 4)  -->  3
    (2, 3, 5)  -->  6
    (2, 4, 5)  -->  8
    (3, 4, 5)  -->  9
    """
    return sum([nck_table[(y - comb_start, x + 1)]
                for x, y in enumerate(comb)])


def tsp(num_of_cities, cities_coor):
    """Computes the shortest travel distance for the traveling-salesman-problem,
    with dynamic programming approach.
    'current_min[s_index][j]' records the shortest distance from starting city,
    which is always 1, to city 'j' by visiting cities in subset 's' exactly once.
    's_index' is computed according to the combinatorial number system, thus dense
    indexed. And 'j' is sparsely ranged from 0 to 'num_of_cites', where only the
    ones can be used next iteration have meaningful values, otherwise zeros.
    'last_min' copys 'current_min' at the end of each iteration, so only needed
    values are stored. The base case for 'last_min[s_index][j]' is the edge distance
    from staring city, which is always 1, to every other city 'j'. Here 's_index'
    is a  dense index computed based on 1-element-comb from range(2, num_of_cities+1).
    After final iteration, 'last_min[0][2:]' contains all shortest distances from city
    1 to every other city(labeled as 2 to 'num_of_cities'), adding the edge distance
    from that city back to city 1 gives all the TSP distances. Note that the minimum
    TSP distance does not vary when staring city changes.
    https://class.coursera.org/algo2-002/forum/thread?thread_id=350"""

    #visited = set([1])
    unvisited = set(xrange(1, num_of_cities))
    arr = [0]
    costs = [0]
    for i in xrange(num_of_cities-1):
        if i % 50 == 0 :
            print i
        mindist = 2**32
        nextcity = -1
        curr_city_coordinate = cities_coor[arr[-1]]
        for city in unvisited:
            dist = euc_dist(curr_city_coordinate, cities_coor[city])
            if dist < mindist:
                nextcity = city
                mindist = dist
            elif dist == mindist:
                nextcity = min(city, nextcity)
        arr.append(nextcity)
        costs.append(sqrt(mindist))
        unvisited.remove(nextcity)

    # print arr
    # for i in arr:
    #     print cities_coor[i]
    # #print costs
    # print 'total cost is ', sum(costs) + sqrt(euc_dist(cities_coor[arr[-1]], cities_coor[0]))
    return sum(costs) + sqrt(euc_dist( cities_coor[arr[-1]], cities_coor[0]))

def main():
    city_num = 0
    cities = []
    dist_dict = {}
    #with open('test.txt') as file_in:
    with open('nn.txt') as file_in:
        next(file_in)
        for line in file_in:
            cities.append( map(float, line.strip().split(' '))[1:] )
            city_num += 1
    print cities[:10]

    # for x in xrange(city_num):
        
    #     xval = cities[x]
    #     for y in xrange(x+1, city_num):
    #         dist_dict[(x, y)] = euc_dist(xval, cities[y])
    #         dist_dict[(y, x)] = dist_dict[(x, y)]
    print 'num of cities', city_num
    #N = city_num
    N = 5000
    print int(tsp(N, cities[:N]))


if __name__ == '__main__':
    start = time()
    print main()
    print time() - start