from random import randint


class DirectedGraph:
    def __init__(self, number_of_vertices=0):
        self.__dict_in = {}
        self.__dict_out = {}

        for i in range(number_of_vertices):
            self.__dict_in[i] = []
            self.__dict_out[i] = []


    @property
    def dict_in(self):
        return self.__dict_in


    @property
    def dict_out(self):
        return self.__dict_out


    def is_vertex(self, vertex_to_check: int):
        if vertex_to_check not in self.__dict_in:
            return False

        return True


    def add_vertex(self, vertex_to_add: int):
        if self.is_vertex(vertex_to_add):
            raise ValueError('Vertex already in graph!')

        self.__dict_in[vertex_to_add] = []
        self.__dict_out[vertex_to_add] = []


    def remove_vertex(self, vertex_to_remove: int):
        if not self.is_vertex(vertex_to_remove):
            raise ValueError('Vertex does not exist!')

        for vertex in self.__dict_out[vertex_to_remove]:
            self.__dict_in[vertex].remove(vertex_to_remove)

        for vertex in self.__dict_in[vertex_to_remove]:
            self.__dict_out[vertex].remove(vertex_to_remove)

        del self.__dict_in[vertex_to_remove]
        del self.dict_out[vertex_to_remove]

    def is_edge(self, edge_to_check: tuple):
        start_point = edge_to_check[0]
        end_point = edge_to_check[1]

        if not self.is_vertex(start_point) or not self.is_vertex(end_point):
            return False

        # (x, y) should check if y is successor of x and x predecessor of y

        if start_point not in self.__dict_in[end_point]:
            return False

        if end_point not in self.__dict_out[start_point]:
            return False

        return True


    def add_edge(self, edge_to_add: tuple):
        start_point = edge_to_add[0]
        end_point = edge_to_add[1]

        if self.is_edge(edge_to_add):
            raise ValueError('Edge is already in graph!')

        self.__dict_out[start_point].append(end_point)
        self.__dict_in[end_point].append(start_point)


    def remove_edge(self, edge_to_remove: tuple):
        if not self.is_edge(edge_to_remove):
            raise ValueError('Edge does not exist!')

        # (x, y) -> remove y from Dout x
        # (x, y) -> remove x from Din y
        x, y = edge_to_remove

        self.__dict_in[y].remove(x)
        self.__dict_out[x].remove(y)


    def get_number_of_vertices(self):
        return len(self.__dict_in)


    def get_set_of_vertices(self):
        return list(self.__dict_in.keys())


    def get_in_degree(self, vertex: int):
        if not self.is_vertex(vertex):
            raise ValueError('Vertex not in graph!')

        return len(self.__dict_in[vertex])


    def get_out_degree(self, vertex: int):
        if not self.is_vertex(vertex):
            raise ValueError('Vertex not in graph!')

        return len(self.__dict_out[vertex])


    def get_in_bound_edges(self, vertex: int):
        edges = []

        for in_vertex in self.__dict_in[vertex]:
            edges.append((in_vertex, vertex))

        return edges


    def get_out_bound_edges(self, vertex: int):
        edges = []

        for out_vertex in self.__dict_out[vertex]:
            edges.append((vertex, out_vertex))

        return edges


    def get_all_edges(self):
        edges = []

        for vertex in self.get_set_of_vertices():
            for edge in self.get_out_bound_edges(vertex):
                edges.append(edge)

        return edges


    def make_copy(self):
        copy_graph = DirectedGraph()

        for vertex in self.get_set_of_vertices():
            copy_graph.add_vertex(vertex)

        for vertex in self.get_set_of_vertices():
            for edge in self.get_in_bound_edges(vertex):
                copy_graph.add_edge(edge)

        return copy_graph


def read_graph_from_file_1(filename: str):
    file = open(filename, 'rt')

    number_of_vertices, number_of_edges = [int(x) for x in file.readline().strip().split()]

    graph = DirectedGraph(number_of_vertices)

    for i in range(number_of_edges):
        x, y = map(int, file.readline().strip().split())

        graph.add_edge((x, y))

    print(graph.dict_in)
    print(graph.dict_out)

    file.close()

    return graph


def read_graph_from_file_2(filename: str):
    file = open(filename, 'rt')

    graph = DirectedGraph()

    for vertex in file.readline().strip().split():
        graph.add_vertex(int(vertex))

    for line in file.readlines():
        x, y = map(int, line.strip().split())

        graph.add_edge((x, y))

    return graph


def write_graph_to_file(filename: str, graph: DirectedGraph):
    file = open(filename, 'wt')

    nodes_as_string = [str(x) for x in graph.get_set_of_vertices()]

    file.write(' '.join(nodes_as_string))

    file.write('\n')

    for edge in graph.get_all_edges():
        file.write(f'{edge[0]} {edge[1]}\n')

    file.close()


def generate_random_graph(number_of_vertices: int, number_of_edges: int):
    graph = DirectedGraph(number_of_vertices)

    while number_of_edges != 0:
        x = randint(0, number_of_vertices - 1)
        y = randint(0, number_of_vertices - 1)

        try:
            graph.add_edge((x, y))
            number_of_edges -= 1
        except ValueError:
            continue
    return graph
