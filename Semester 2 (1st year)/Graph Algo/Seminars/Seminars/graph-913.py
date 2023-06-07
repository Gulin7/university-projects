import copy
import random
import time

class Graph:
    def __init__(self, n):
        '''Constructs a graph with n vertices numbered from 0 to n-1 and no edges
        '''
        self.__out = {}
        
        for i in range(n):
            self.__out[i] = []
        

    def add_edge(self, x, y):
        '''Adds an edge from x to y. Return True on success, False if the edge already exists. Precond: x and y exists
        '''
        
        if y in self.__out[x]:
            return False
            
        self.__out[x].append(y)
        return True

    def parseX(self):
        '''Returns something that can be iterated and produces all the vertices of the graph
        '''
        return list(self.__out.keys())
    
    def parseNOut(self, x):
        return list(self.__out[x])
        
        
    def parseNIn(self, x):
        neigh = []
        
        for node in self.__out:
            if x in self.__out[node]:
                neigh.append(node)
            
        return neigh
        
        
    def isEdge(self, x, y):
        return y in self.__out[x]

class GraphWithInNbh:
    def __init__(self, n):
        '''Constructs a graph with n vertices numbered from 0 to n-1 and no edges
        '''
        self.__out = {}
        self.__in = {}
        
        for i in range(n):
            self.__out[i] = []
            self.__in[i] = []
        

    def add_edge(self, x, y):
        '''Adds an edge from x to y. Return True on success, False if the edge already exists. Precond: x and y exists
        '''
        
        if y in self.__out[x]:
            return False
            
        self.__out[x].append(y)
        self.__in[y].append(x)
        return True

    def parseX(self):
        '''Returns something that can be iterated and produces all the vertices of the graph
        '''
        return list(self.__out.keys())
    
    def parseNOut(self, x):
        return list(self.__out[x])
        
        
    def parseNIn(self, x):
        return list(self.__in[x])
        
        
    def isEdge(self, x, y):
        return y in self.__out[x]
        
    def removeEdge(self, x, y):
        if not y in self.__out[x]:
            return False
            
        self.__out[x].remove(y)
        self.__in[y].remove(x)
        
        return True

def print_graph(g):
    print("Outbound")
    for x in g.parseX():
        print(x, ":", end='')
        for y in g.parseNOut(x):
            print(y, ' ', end='')
        print()
    print("Inbound")
    for x in g.parseX():
        print(x, ":", end='')
        for y in g.parseNIn(x):
            print(y, ' ', end='')
        print()

def parse_graph(g):
    before = time.time()
    for x in g.parseX():
        for y in g.parseNOut(x):
            pass
    after = time.time()
    print("Parse NOut: %sms" %((after-before)*1000, ))
    before = time.time()
    for x in g.parseX():
        for y in g.parseNIn(x):
            pass
    after = time.time()
    print("Parse NIn: %sms" %((after-before)*1000, ))

def create_small_graph(ctor=Graph):
    create_small_graph_with_costs(ctor)[0]

def create_small_graph_with_costs(ctor=Graph):
    g = ctor(6)
    cost = {(0,2):2, (1,0):1, (1,2):4, (2,3):2, (3,4):3, (4,2):1,(5,0):2,(5,4):2}
    for e in cost.keys():
        g.add_edge(e[0], e[1])
    return (g, cost)

def create_small_dag_and_cost(ctor=Graph):
    g = ctor(8)
    cost = {(0,3):2, (1,2):4, (3,2):1, (3,5):1, (4,0):3, (6,0):1,(6,1):3, (6,2):8, (2,7):2, (5,7):3,
        #(2,0): 1,
        }
    for e in cost.keys():
        g.add_edge(e[0], e[1])
    return g,cost

def create_random_graph(n, m, ctor=Graph):
    '''Creates a graph with n vertices and m edges, constructed with constructor 'ctor'
    '''
    g = ctor(n)
    if m > n*n:
        raise Exception("too many edges")
    before = time.time()
    if m * 2 < n * n:
        number_of_added_edges = 0
        failed_attempts_at_adding_an_edge = 0
        while number_of_added_edges < m:
            x = random.randrange(n)
            y = random.randrange(n)
            if g.add_edge(x,y):
                number_of_added_edges += 1
            else:
                failed_attempts_at_adding_an_edge +=1
        print(f"There were {failed_attempts_at_adding_an_edge} failed attempts at adding an edge")
    else:
        for i in range(n):
            for j in range(n):
                g.add_edge(i, j)
        
        number_of_edges = n * n
        while number_of_edges > m:
            x = random.randrange(n)
            y = random.randrange(n)
            output = g.removeEdge(x, y)
            if output:
                number_of_edges -= 1
                
    after = time.time()
    print(f"Generating the graph took {after-before} seconds")
    return g

def create_random_dag(n, m, ctor=Graph):
    '''Creates a graph with n vertices and m edges, constructed with constructor 'ctor'
    '''
    g = ctor(n)
    if m > n*(n-1)//2:
        raise Exception("too many edges")
    before = time.time()
    vertices = [x for x in range(n)]
    random.shuffle(vertices)
    number_of_added_edges = 0
    failed_attempts_at_adding_an_edge = 0
    while number_of_added_edges < m:
        #x = random.randint(0,n-2)
        #y = random.randint(x+1,n-1)
        a = random.randint(0,n-1)
        b = random.randint(0,n-2)
        if a > b:
            x = b
            y = a
        else:
            x = a
            y = b + 1
        if g.add_edge(vertices[x],vertices[y]):
            number_of_added_edges += 1
        else:
            failed_attempts_at_adding_an_edge +=1
    print(f"There were {failed_attempts_at_adding_an_edge} failed attempts at adding an edge")

    after = time.time()
    print(f"Generating the graph took {after-before} seconds")
    return g
    
class UndirectedGraph:
    def __init__(self, n):
        '''Constructs a graph with n vertices numbered from 0 to n-1 and no edges
        '''
        self.__nbh = {}
        
        for i in range(n):
            self.__nbh[i] = []
        

    def add_edge(self, x, y):
        '''Adds an edge from x to y. Return True on success, False if the edge already exists. Precond: x and y exists
        '''
        
        if y in self.__nbh[x]:
            return False
            
        self.__nbh[x].append(y)
        self.__nbh[y].append(x)
        return True

    def parseX(self):
        '''Returns something that can be iterated and produces all the vertices of the graph
        '''
        return list(self.__nbh.keys())
    
    def parseN(self, x):
        return list(self.__nbh[x])
        
    def parseNout(self, x):
        return self.parseN()
        
    def parseNIn(self, x):
        return self.parseN()
        
    def isEdge(self, x, y):
        return y in self.__nbh[x]

def create_small_undirected(ctor=UndirectedGraph):
    g = ctor(range(1,7))
    lst = [(1,2,3), (1,3,2), (1,4,4), (2,3,2), (2,6,1), (3,4,4),(3,5,3),(3,6,2),(4,5,5),(5,6,5)]
    cost={}
    for x,y,c in lst:
        g.add_edge(x,y)
        cost[x,y] = c
        cost[y,x] = c
    return g,cost

def main():
    n = 1000
    #g = create_small_graph(GraphWithInNbh)
    g = create_random_graph(n, n*n-5, GraphWithInNbh)
    #print_graph(g)
    parse_graph(g)

if __name__ == "__main__":
    main()